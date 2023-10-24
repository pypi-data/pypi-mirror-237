import requests
import getpass
import json
import sys
import os
import re
import pandas as pd 
import influxdb_client

from datetime import datetime, timezone, timedelta
from .enums import CheckStatusCode, HTTPStatusCode

class SDTcloud():
    def __init__(self):
        self.url = f"http://datalake-internal-query-service.sdt-cloud.svc.cluster.local:8080"  # datalake url
        self.giteamanager_url = f'http://gitea-manager.sdt-cloud.svc.cluster.local:8010'  # gitea-manager url
        self.giteamanager_url_regex = r"((git|ssh|http(s)?)|(git@[\w\.]+))(:(//)?)([\w\.@\:/\-~]+)(\.git)(/)?"
        self.namespace = os.getenv("NAMESPACE")
        self.organizationId = ""
        self.id = ""
        self.email = ""
        self.name = ""
        self.minioBucket = ""
        self.minioAccessKey = ""
        self.minioSecretKey = ""
        # InfluxDB
        self.influxUrl = ""
        self.influxOrganization = ""
        self.influxToken = ""
        self.influxBucket = ""
        self.influxMeasurement = ""

        self.projectDataFrame = None  # project DataFrame
        self.assetDataFrame = None  # asset DataFrame

        self.currentProjectIdx = None  # current project idx
        self.currentProjectName = None  # current project name
        self.currentDevice = None  # current device

    def exceptionHandle(self, responseData, subtype):
        resp_dict = json.loads(responseData.content)
        if subtype == "500":
            errFormat = {
                "timestamp": resp_dict['timestamp'],
                "code": responseData.status_code,
                "error": resp_dict['error'],
                "message": resp_dict['error']
            }
        else:
            errFormat = {
                "timestamp": resp_dict['timestamp'],
                "code": resp_dict['code'],
                "error": resp_dict['error'],
                "message": resp_dict['message']
            }
        
        raise Exception(f"Failed!!!\n {errFormat}")
    

    def checkStatusCode(self, status_code):
        """ Check status code and return 0 or 1. 
            CheckStatusCode.FAILED.value(0) is fail.
            CheckStatusCode.OK.value(1) is 200(OK).
            HTTPStatusCode.CREATED.value(2) is 201(Created).
            CheckStatusCode.NO_CONTENT.value(3) is 204(No Content).

        Args:
            data (Dict): Response of api
            status_code (Int): Status code of resource
        """
        if status_code == HTTPStatusCode.INTERNAL_SERVER_ERROR.value:
            return CheckStatusCode.FAILED.value, f"Internal Server Error!!!, Status: {status_code}"
        elif status_code == HTTPStatusCode.OK.value:
            return CheckStatusCode.OK.value, f"Ok!!!, Status: {status_code}"
        elif status_code == HTTPStatusCode.CREATED.value:
            return CheckStatusCode.CREATED.value, f"Created!!!, Status: {status_code}"
        elif status_code == HTTPStatusCode.NO_CONTENT.value:
            return CheckStatusCode.NO_CONTENT.value, f"No Content!!!, Status: {status_code}"
        else:
            return CheckStatusCode.FAILED.value, ""

    # 초기화
    def init(self):
        """ login of stackbase. 

        Raises:
            Exception: _description_
        """
        
        # userId = input("ID: ")
        # userPassword = getpass.getpass("PW: ")

        headers = {
            "Content-Type": "application/json",
            "X-NS": self.namespace
        }
        
        response = requests.request('post',f"{self.url}/internal/datalake/v1/auth", headers=headers)
        respStatus, returnMessage = self.checkStatusCode(response.status_code)

        if respStatus == 0:
            self.exceptionHandle(response, returnMessage)
        
        result = json.loads(response.content)

        self.organizationId = result['organizationId']
        self.id = result['id']
        self.email = result['email']
        self.name = result['name']
        self.minioBucket = result['minioBucket']
        self.minioAccessKey = result['minioAccessKey']
        self.minioSecretKey = result['minioSecretKey']

        self.currentProjectIdx = None
        self.currentProjectName = None
        self.currentDevice = None

        print(returnMessage)

    def setDevice(self, assetCode):
        headers = {
            "Content-Type": "application/json",
            "X-ORG-CODE": self.organizationId
        }

        # projectDataFrame에서 idx로 projectCode 가져오기
        projectCode, _ = self.getProjectCodeByIdx(self.currentProjectIdx, self.projectDataFrame)

        response = requests.request('get',f"{self.url}/internal/datalake/v1/projects/{projectCode}/assets/{assetCode}", headers=headers)
        respStatus, returnMessage = self.checkStatusCode(response.status_code)

        if respStatus == 0:
            self.exceptionHandle(response, returnMessage)
        
        result = json.loads(response.content)

        self.influxUrl = result['url']
        self.influxOrganization = result['organization']
        self.influxToken = result['token']
        self.influxBucket = result['bucket']
        self.influxMeasurement = result['measurement']
        self.currentDevice = assetCode

        print('Current project name: {} \n Current device name : {}'.format(self.currentProjectName, self.currentDevice))

        print(f"[INFO] List of accessible DBs: InfluxDB")

    # 유저의 프로젝트 리스트 조회
    def getProject(self):
        """ Print list of project in sdt cloud

        Raises:
            Exception: _description_

        Returns:
            _type_: _description_
        """
        headers = {
            "Content-Type": "application/json",
            "X-ORG-CODE": self.organizationId
        }

        response = requests.request('get',f"{self.url}/internal/datalake/v1/projects", headers=headers)
        respStatus, returnMessage = self.checkStatusCode(response.status_code)

        if respStatus == CheckStatusCode.FAILED.value:
            self.exceptionHandle(response, returnMessage)
        elif respStatus == CheckStatusCode.NO_CONTENT.value:
            print(returnMessage)
            return 0

        result = json.loads(response.content)
        self.projectDataFrame = pd.DataFrame(result)
        
        print(returnMessage)
        
        return self.projectDataFrame

    def getProjectCodeByIdx(self, idx, df):
        """
            ProjectDataFrame에서 index로 project code 조회
        Args:
            idx (int): dataframe idx
            df (pd.DataFrame): project dataframe

        Returns:
            str: projectCode
        """        
        if df is not None and df.empty != True:
            return df.iloc[idx]['code'], df.iloc[idx]['name']

    # 프로젝트 선택
    def setProject(self, idx):
        """
            idx로 projectCode 조회하여 project에 속한 AssetData 가져오기
        Args:
            idx (_type_): project dataframe index

        Returns:
            _type_: _description_
        """

        headers = {
            "Content-Type": "application/json",
            "X-ORG-CODE": self.organizationId
        }

        # projectDataFrame에서 idx로 projectCode 가져오기
        projectCode, projectName = self.getProjectCodeByIdx(idx, self.projectDataFrame)

        response = requests.request('get',f"{self.url}/internal/datalake/v1/projects/{projectCode}/assets", headers=headers)
        respStatus, returnMessage = self.checkStatusCode(response.status_code)

        if respStatus == CheckStatusCode.FAILED.value:
            self.exceptionHandle(response, returnMessage)

        result = json.loads(response.content)
        self.assetDataFrame = pd.DataFrame(result)

        # 현재 선택한 프로젝트
        self.currentProjectIdx = idx
        self.currentProjectName = projectName

        # 현재 선택한 device는 무조건 초기화
        self.currentDevice = None

        print('Current project name: {}'.format(self.currentProjectName))

        print(returnMessage)
        return self.assetDataFrame
    
    def getData(self, dbType, startTime="-1h", stopTime="now()"):
        timezone_kst = timezone(timedelta(hours=9))
        client = influxdb_client.InfluxDBClient(
            url=self.influxUrl,
            token=self.influxToken,
            org=self.influxOrganization
        )
        query_api = client.query_api()

        query = f'from(bucket:"{self.influxBucket}")\
                |> range(start: {startTime}, stop: {stopTime})\
                |> filter(fn:(r) => r._measurement == "{self.influxMeasurement}")'

        result = query_api.query(org=self.influxOrganization, query=query)
        results = []
        for table in result:
            for record in table.records:
                results.append((record.get_field(), record.get_value(), record.get_time().astimezone(timezone_kst)))
        
        df = pd.DataFrame(results, columns=['field', 'value', 'time'])

        print('Current project name: {} \n Current device name : {}'.format(self.currentProjectName, self.currentDevice))

        return df

    def getUserRepository(self):
        headers = {
            'email': self.email
        }

        response = requests.request('GET',f"{self.giteamanager_url}/stackbase/v1/gitea-manager/repos", headers=headers)

        if response.status_code == HTTPStatusCode.OK.value:
            repository_list = response.json().get('content')

            results = []
            if len(repository_list) > 0:
                for repo in repository_list:
                    results.append((repo.get('name'), repo.get('default_branch'), repo.get('clone_url')))

                df = pd.DataFrame(results, columns=['repository_name', 'branch', 'clone_url'])
                pd.set_option('display.max_colwidth', None)
                return df
        else:
            return f'Failed!, Status: {response.status_code}, Message: {response.json()}' 

    def checkGiteaUrlRegex(self, url):
        pattern = re.compile(self.giteamanager_url_regex, re.IGNORECASE)
        result = pattern.match(url)
        
        if result:
            print('repository url verify!')
            return result.lastindex
        else:
            print('respotiroy url is not verify!')
            return 0

    def cloneUserRepository(self, clone_url):
        try:
            if clone_url != '':
                regex_result = self.checkGiteaUrlRegex(clone_url)
                if regex_result > 0:
                    result = os.system(f'git clone {clone_url}')

                    if result == 0:
                        print(f'Completed Clone Repository!, Status: {HTTPStatusCode.OK.value}')
                        return HTTPStatusCode.OK.value
                    else:
                        print(f'Failed Clone Repository!, Status: {HTTPStatusCode.INTERNAL_SERVER_ERROR.value}')
                        return HTTPStatusCode.INTERNAL_SERVER_ERROR.value
        except Exception as e:
            print(f'Error Raise! Reason: {e}, Status: {HTTPStatusCode.INTERNAL_SERVER_ERROR.value}')
            return HTTPStatusCode.INTERNAL_SERVER_ERROR.value

    def addStageFile(self, file_path_for_add_stage='.', full_flag=True):
        try:
            result = None
            if full_flag:
                result = os.system('git add -A .')
            else:
                result = os.system(f'git add {file_path_for_add_stage}')

            if result == 0:
                print('Completed! Add File to Stage')
                return HTTPStatusCode.OK.value
            else:
                print('Failed! Add File to Stage')
                return HTTPStatusCode.INTERNAL_SERVER_ERROR.value
        except Exception as e:
            print(f'Error Raise! Reason: {e}, Status: {HTTPStatusCode.INTERNAL_SERVER_ERROR.value}')
            return HTTPStatusCode.INTERNAL_SERVER_ERROR.value

    def commitRepository(self, commit_message):
        try:
            result = os.system(f'git commit -m {commit_message}')

            if result == 0:
                print('Commit Completed!')
                return HTTPStatusCode.OK.value
            else:
                print('Commit Failed!')
                return HTTPStatusCode.INTERNAL_SERVER_ERROR.value
        except Exception as e:
            print(f'Error Raise! Reason: {e}, Status: {HTTPStatusCode.INTERNAL_SERVER_ERROR.value}')
            return HTTPStatusCode.INTERNAL_SERVER_ERROR.value

    def pushRepository(self, push_file_path='.'):
        result = None
        if push_file_path == '.':
            result = os.system('git push')
        else:
            os.chdir(f'./{push_file_path}')
            result = os.system('git push')

        if result == 0:
            print('Push Completed!')
            return HTTPStatusCode.OK.value
        else:
            print('Push Failed!')
            return HTTPStatusCode.INTERNAL_SERVER_ERROR.value

    def pullRepository(self, repository_url, file_path):
        try:
            regex_result = self.checkGiteaUrlRegex(repository_url)

            if regex_result > 0:
                repository_name = repository_url.split('/')[len(repository_url.split('/')) - 1].split('.')[0]
                if os.path.exists(f'./{repository_name}'):
                    os.chdir(f'./{repository_name}')
                    result = os.system(f'git pull {repository_url}')
                    if result == 0:
                        print(f'Completed! Pull Repository: {repository_url}')
                        return HTTPStatusCode.OK.value
                    else:
                        print(f'Failed! Pull Repository: {repository_url}')
                        return HTTPStatusCode.INTERNAL_SERVER_ERROR.value
                else:
                    print('repository path does not exist in notebook file path \n')
                    clone_repository_status = self.cloneUserRepository(repository_url) 
                    return clone_repository_status
        except Exception as e:
            print(f'Error Raise! Reason: {e}, Status: {HTTPStatusCode.INTERNAL_SERVER_ERROR.value}')
            return HTTPStatusCode.INTERNAL_SERVER_ERROR.value

    # # 폴더 등록
    # def create_folder(self, storageId, parentId, dirName):
    #     """ Create folder in stackbase's storage

    #     Args:
    #         storageId (Str): Storage ID that create folder.
    #         parentId (Str): Folder ID that create folder. If you want to set root path, you have to enter "".
    #         dirName (Str): Folder name.

    #     Raises:
    #         Exception: _description_

    #     Returns:
    #         _type_: _description_
    #     """
    #     headers = {
    #         "Content-Type": "application/json",
    #         "Authorization": self.userToken
    #     }

    #     bodys = json.dumps({
    #         "parentId": parentId,
    #         "name": dirName,
    #         "storageId": storageId
    #     })

    #     response = requests.request('post',f"{self.url}/stackbase/v1/folder", headers=headers, data=bodys)
    #     respStatus, returnMessage = self.checkStatusCode(response.status_code)

    #     if respStatus == 0:
    #         self.exceptionHandle(response, returnMessage)

    #     result = json.loads(response.content)
    #     result['createdAt'] = datetime.fromtimestamp(int(result['createdAt']/1000), timezone(timedelta(hours=9)))
        
    #     print(returnMessage)
    
    # # 트리 검색
    # def get_tree(self, storageId, parentId):
    #     """ Print list of tree in stackbase.

    #     Args:
    #         storageId (Str): Storage ID
    #         parentId (Str): Folder ID. If you want to set root path, you have to enter "".

    #     Raises:
    #         Exception: _description_

    #     Returns:
    #         _type_: _description_
    #     """
    #     headers = {
    #         "Content-Type": "application/json",
    #         "Authorization": self.userToken
    #     }

    #     param = {
    #         "storageId": storageId,
    #         "parentId": parentId
    #     }

    #     response = requests.request('get',f"{self.url}/stackbase/v1/trees", headers=headers, params=param)
    #     respStatus, returnMessage = self.checkStatusCode(response.status_code)

    #     if respStatus == 0:
    #         self.exceptionHandle(response, returnMessage)
    #     elif respStatus == 3:
    #         print(returnMessage)
    #         return 0
            
    #     result = json.loads(response.content)
    #     df1 = pd.DataFrame(result)
    #     df2 = pd.DataFrame(result['trees'])
        
    #     df = pd.concat([df1.drop(['trees'], axis=1), df2], axis=1)
    #     for n in range(len(df)):
    #         df.loc[n, 'modifiedAt'] = datetime.fromtimestamp(int(df.loc[n, 'modifiedAt']/1000), timezone(timedelta(hours=9)))
        
    #     print(returnMessage)
    #     return df

    # # 폴더 수정
    # def update_folder(self):
    #     print("update")

    # # 폴더 삭제
    # def delete_folder(self):
    #     print("delete")

    # # 컨텐츠 조회
    # def get_content(self):
    #     print("get")

    # # 컨텐츠 수정
    # def update_content(self):
    #     print("test")
    
    # # 컨텐츠 삭제
    # def delete_content(self):
    #     print("test")

    # # 컨텐츠 다운로드
    # def fget_content(self, fileId, getPath):
    #     """ Download content(file) from stackbase.

    #     Args:
    #         fileId (Str): File ID
    #         getPath (Str): File save path.

    #     Raises:
    #         Exception: _description_
    #     """
    #     headers = {
    #         "Authorization": self.userToken
    #     }

    #     response = requests.request('get',f"{self.url}/stackbase/v1/contents/download/{fileId}", headers=headers)
    #     respStatus, returnMessage = self.checkStatusCode(response.status_code)

    #     if respStatus == 0:
    #         self.exceptionHandle(response, returnMessage)
        
    #     with open(getPath, "wb") as f:
    #         f.write(response.content)
        
    #     print(returnMessage)
    
    # # 컨텐츠 등록
    # def fput_content(self, storageId, folderId, filePath, fileVersion, fileFormat, fileTag):
    #     """ Upload content(file) in stackbase

    #     Args:
    #         storageId (Str): Storage ID
    #         folderId (Str): Folder ID
    #         filePath (Str): Path of upload file
    #         fileVersion (Str): Version of file
    #         fileFormat (Str): Format of file
    #         fileTag (Str): Tag of file

    #     Raises:
    #         Exception: _description_

    #     Returns:
    #         _type_: _description_
    #     """
    #     headers = {
    #         "Authorization": self.userToken
    #     }

    #     bodys = json.dumps({
    #         "storageId": storageId,
    #         "folderId": folderId,
    #         "version": fileVersion,
    #         "format": fileFormat,
    #         "tag": fileTag
    #     })

    #     file_open = open(filePath, 'rb')

    #     files={
    #         'request': (None, bodys, 'application/json'),
    #         "content": (filePath.split("/")[-1], file_open, 'application/octet-stream')
    #     }

    #     response = requests.request("POST", f"{self.url}/stackbase/v1/contents", headers=headers, files=files)
    #     respStatus, returnMessage = self.checkStatusCode(response.status_code)

    #     if respStatus == 0:
    #         self.exceptionHandle(response, returnMessage)

    #     result = json.loads(response.content)
    #     result['createdAt'] = datetime.fromtimestamp(int(result['createdAt']/1000), timezone(timedelta(hours=9)))
    #     result['modifiedAt'] = datetime.fromtimestamp(int(result['modifiedAt']/1000), timezone(timedelta(hours=9)))
        
    #     print(returnMessage)
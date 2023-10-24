import requests
import sys
import csv
import os
import boto3
from botocore.exceptions import ClientError
from requests_toolbelt.multipart.encoder import MultipartEncoder
import dateutil.parser
from datetime import datetime, timedelta, time, timezone
from pytz import UTC as utc
from tqdm.auto import tqdm

global g_username
global g_password
global g_api_url_base
global g_token

global g_s3_data_bucket_upload
global g_exec_t

class PSCommon:
    def __init__(self, env):
        self.env = env
        ps_set_env(env)

    def __str__(self):
        return  self.env

    def login(self):
        ps_login()

    def get_all_accounts(self):
        return ps_get_all_accounts()

    def get_all_mp_from_account(self, account):
        return ps_get_all_mp_from_account(account)

    def get_event_mp(self,accountId, mpId,startDate,endDate,deviceEventTypeId):
        return ps_get_event_mp(accountId, mpId,startDate,endDate,deviceEventTypeId)

    def get_mp(selfs, mp):
        return ps_get_mp(mp)

    def get_mp_trend(self,mp,payload):
        return ps_get_mp_trend(mp,payload)

    def get_mp_channel_def(self,mp):
        return ps_get_mp_channel_def(mp)

    def get_mp_by_serial(selfs,serialNumber):
        return ps_get_mp_by_serial(serialNumber)

    def get_exec_t(self):
        return g_exec_t


class PSS3:
    def __init__(self):
        self.s3_client = boto3.client('s3')
        self.s3_resource = boto3.resource('s3',region_name='us-east-1', aws_access_key_id=g_aws_key,aws_secret_access_key=g_aws_secret)
        self.bucket = g_s3_data_bucket_upload

    def get_bucket_name(self):
        return g_s3_data_bucket_upload

    def download_file(self, file_name, object_name=None):
        # If s3 object_name was not specified, use file_name
        if object_name is None:
            object_name = os.path.basename(file_name)
        try:
            response = self.s3_client.download_file(self.bucket, file_name, file_name)
            print(f's3 Download: {response}')
        except ClientError as e:
            print(f's3 download error {e}')
            return False
        return True

    def download_folder(self, local_folder):
        b = self.s3_resource.Bucket(self.bucket)
        try:
            for obj in b.objects.filter(Prefix=local_folder):
                if not os.path.exists(os.path.dirname(obj.key)):
                    os.makedirs(os.path.dirname(obj.key))
                b.download_file(obj.key, obj.key)  # save to same path

        except ClientError as e:
            print(f's3 download dir error {e}')
            return False
        return True

    def download_date_range(self,local_folder, beg_date,end_date):
        b = self.s3_resource.Bucket(self.bucket)
        try:
            keys = [
                o for o in b.objects.filter(Prefix=local_folder)
                if o.last_modified < end_date and o.last_modified >= beg_date
            ]
            total = len(keys)
            pbar = tqdm(range(total), position=0, leave=True)
            for i in pbar:
                b.download_file(keys[i].key,keys[i].key)
                pbar.set_description(f'{keys[i].key}')
                if i == (total -1): pbar.set_description(f'Downloading')

        except ClientError as e:
            print(f's3 download dir error {e}')
            return False
        return True


def ps_set_env(env):
    global g_username
    global g_password
    global g_api_url_base
    global g_s3_data_bucket_upload
    global g_aws_key
    global g_aws_secret
    global g_exec_t

    if env == "prod" or env == "production":
        g_username = 'louis.marchand@powerside.com'
        g_password = 'Allo123!'
        g_api_url_base = 'https://www.admin.cloud.powerside.com/v1/'
        g_s3_data_bucket_upload = 'insite-production-data-bucket-upload'
        g_aws_key = 'AKIAUPH3P2X4WPWRJIJ3'
        g_aws_secret = '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'

    elif env == "staging":
        g_username = "lmarchand07+sa@gmail.com"
        g_password = "Allo123!"
        g_api_url_base = 'https://staging.admin.cloud.powerside.com/v1/'
        g_s3_data_bucket_upload = 'insite-staging-data-bucket-upload'
        g_aws_key = 'AKIAXVVE4A3T53W5U5XI'
        g_aws_secret = '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'

    working_dir = './tmp'
    os.makedirs(working_dir, exist_ok=True)
    os.chdir(working_dir)

    g_exec_t = datetime.today().strftime('%Y%m%d-%H%M')
    print(g_exec_t)
    print(g_username)
    print(g_api_url_base)

def ps_login():
    global g_token
    print("Login")
    request = {
            "email": g_username,
            "password": g_password}

    response = requests.post(g_api_url_base + 'login', json=request)
    if response.status_code == 200:
        info = response.json()
        g_token = info["token"]
    else:
        print(response)
    return response.status_code


def ps_get_all_accounts():
    api_url = '{0}accounts?count={1}'.format(g_api_url_base, 100000)
    accounts = []

    header = {'authorization': 'Bearer ' + g_token}
    response = requests.get(api_url, headers=header)
    if response.status_code == 200:
        accounts = response.json()
    else:
        print(response)

    return accounts

def ps_get_all_mp_from_account(account):
    '''
    Measurement Point
    {'accountId': 252, 'accountName': 'Dominion Energy', 'partnerId': 252, 'partnerName': 'Dominion Energy', 'measurementPointId': 15802, 'measurementPointTypeId': 1, 'measurementPointStatusId': 8, 'measurementPointTypeName': 'QubeScan', 'measurementPointStatusName': 'commissioned', 'mainImageId': None, 'commissionedWhen': '2023-01-30T20:35:00.000Z', 'lastCommunicationTime': '2023-10-04T18:20:00.000Z', 'isLocked': 1, 'mpId': 'Afton Chemical 2.5', 'serialNumber': 'P3018306', 'pqubeModel': 'PQube3', 'notes': '', 'locationId': 1895, 'createdWhen': '2023-01-30T20:34:53.000Z', 'locationName': 'Afton Chemical', 'locationShortname': 'Afton Chemical', 'address1': '500 Spring Street', 'address2': '', 'city': 'Richmond', 'state': 'VA', 'zipCode': '23219', 'country': 'United States', 'latitude': 37.541115523, 'longitude': -77.44778955, 'siteInformation': None, 'timezone': 'America/New_York', 'summaryKpi': '#FF0000', 'acInputKpi': '#FF0000', 'psuKpi': '#4BB050', 'dcBusKpi': '#4BB050', 'acOutputKpi': '#4BB050', 'severeEventCount': 3}
    '''
    mps = []
    if type(account) is dict:
        acId = account["id"]
        if acId == 2: #getting rid of Powerside Manufacturing
            return mps
    elif type(account is int):
        acId = account
    else:
        return mps
    header = {'authorization': 'Bearer ' + g_token}
    api_url = '{0}measurementPoints/hierarchy?accountId={1}{2}'.format(g_api_url_base, acId,"&excludeMeasurementPoints=false&excludeMeasures=true&includeRetired=false" )

    response = requests.get(api_url, headers=header)
    if response.status_code == 200:
        #Parse json
        customersList = []
        keepCustomers = True
        mpinfoDict = response.json()
        #hierarchie call return diff structure based on partner or customer.
        if "partners" in mpinfoDict:
            if len(mpinfoDict["partners"]) == 1:
                customersList = mpinfoDict["partners"][0]["customers"]
            else:
                print(f'Error long partner list {mpinfoDict["partners"]}')
            keepCustomers = False

        elif "customers" in mpinfoDict:
            customersList = mpinfoDict["customers"]

        if customersList != None:
            for custDict in customersList:
                for mp in custDict["measurementPoints"]:
                    if mp['accountId'] == mp['partnerId'] or keepCustomers == True: #this is to avoid adding mp from a customer with a partner twice.
                        mps.append(mp)

    else:
        print(response)
    return mps


def ps_get_mp(mpId):
    '''
    parameter p:
    get the measurement point information
    {
        "mpId": "Rada Entrance - 01",
        "roomId": 7,
        "measurementPointTypeId": 2,
        "measurementPointStatusId": 8,
        "commissionedWhen": "2019-11-22T22:46:52.000Z",
        "crmCode": null,
        "notes": "",
        "accountId": 5,
        "city": "Delson",
        "country": "Canada",
        "timezone": "America/Toronto",
        "accountName": "Rada Industries",
        "measurementPointTypeName": "In-Site",
        "measurementPointStatusName": "commissioned",
        "locationName": "sitename",
        "serialNumber": "P3001234"


    }
    '''
    header = {'authorization': 'Bearer ' + g_token}
    api_url = f'{g_api_url_base}measurementPoint/{mpId}'

    response = requests.get(api_url, headers=header)
    if response.status_code == 200:
        mp = response.json()
        mp['measurementPointId'] = mp['roomId']         #addind this field since most of other calls are using measurementPointId, not roomId
        return mp
    else:
        print(f'get_mp: {response}')
        return None


def ps_get_mp_channel_def(mp):
    '''
    {
      "pqubeModel": "PQube 3e",
      "nominalFrequency": "60",
      "nominalPhaseToNeutralVoltage": "346.4",
      "powerConfiguration": "Wye/Star",
      "channels": {
        "0": {
          "3": {
            "channelScalar": 0.03509521484375,
            "unitOffset": 3,
            "isConfigurable": false,
            "name": "N-E 3PLD2",
            "units": "V",
            "trendTable": {
              "oneminute": [
                "c_3_min_v",
                "c_3_avg_v",
                "c_3_max_v"
              ]
            },
            "meterParam": "c_3_inst_v"
          },
    '''
    header = {'authorization': 'Bearer ' + g_token}
    api_url = f'{g_api_url_base}channelDefinition/{mp}?eligibleForTrendAlertsOnly=false'

    response = requests.get(api_url, headers=header)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'ps_get_mp_channel_def: {response}')
        return None


def ps_get_mp_by_serial(serialNumber):
    header = {'authorization': 'Bearer ' + g_token}
    api_url = f'{g_api_url_base}device/{serialNumber}/measurementPointInfo'

    response = requests.get(api_url, headers=header)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'ps_get_mp_by_serial: {response}')
        return None


def ps_post_cmd(mpId,cmd):
    print(f'post_cmd_getdiaglog mpId:{mpId}')
    sessionId=""

    # todo to test
    #mp_encoder = MultipartEncoder(fields={'parameters':f'\'{"commandId":{cmd}}\''})
    mp_encoder = MultipartEncoder(fields={'parameters': '{"commandId":7}'})

    header = {'authorization': 'Bearer ' + g_token, 'Content-Type': mp_encoder.content_type}
    url = f'{g_api_url_base}measurementPoint/{mpId}/maintenance'

    response = requests.post(url, data=mp_encoder, headers=header)

    if response.status_code == 200:
        info = response.json()
        sessionId = info["id"]
    else:
        print(f'ps_post_cmd:{mpId}')
        print(response)
    return sessionId


def ps_export_list_to_CSV(f,the_list,field_names, write_header=True, mode='w'):
    t = datetime.today().strftime('%Y%m%d-%H%M')
    file_name = f'{f}-{t}.csv'
    with open(file_name, mode, encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        if write_header:
            writer.writeheader()

        writer.writerows(the_list)
        csvfile.close()
    return


def ps_get_event_mp(accountId, mpId,startDate,endDate,deviceEventTypeId):
    '''
    [
      {
        "documentId": 2628579,
        "deviceEventId": 359793,
        "triggeredWhen": "2023-10-04T15:20:26.741Z",
        "deviceEventTypeId": 2,
        "eventMagnitude": null,
        "eventMagnitudeTag": null,
        "channel": null,
        "channelId": null,
        "duration": null,
        "isSevere": 0,
        "deviceEventType": "snapshot",
        "defaultDisplayName": null,
        "timezone": "America/St_Johns",
        "gifDocumentExists": 1,
        "pqdDocumentExists": 0,
        "csvDocumentExists": 1,
        "waveformDocumentId": 2628581,
        "rmsDocumentId": 2628583,
        "deviceEventStatus": "unread",
        "isCleared": 0,
        "sagDirectionPrediction": null,
        "sagDirectionProbability": null
      }
    ]
    '''

    header = {'authorization': 'Bearer ' + g_token}
    if deviceEventTypeId != 0:
        api_url = f'{g_api_url_base}events/measurementPoint/{mpId}?accountId={accountId}&dateRangeStart={startDate}&dateRangeEnd={endDate}&deviceEventTypeId={deviceEventTypeId}&severeOnly=false&includeRetired=false&offset=0&count=100000'
    else:
        api_url = f'{g_api_url_base}events/measurementPoint/{mpId}?accountId={accountId}&dateRangeStart={startDate}&dateRangeEnd={endDate}&severeOnly=false&includeRetired=false&offset=0&count=100000'

    response = requests.get(api_url, headers=header)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'get_mp: {response}')
        return None


def  ps_get_mp_trend(mpId ,payload):
    '''
    :param mpId: measurement Point as integer
    :param payload: the request
    :return: url or json object depending of the request in the payload
    '''
    api_url = f'{g_api_url_base}trends/measurementPoint/{mpId}'
    header = {'authorization': 'Bearer ' + g_token}

    res = requests.post(api_url, json=payload, headers=header)
    if  res.status_code !=  200:
        print(res.status_code)
        print(res.headers)
        print(res.reason)
        print(payload)
        return None
    return res.text


def ps_download_file(file_name, bucket, object_name=None):
    '''
    Upload a file to an s3 bucket
    :param file_name: File to download
    :param bucket: Bucket to upload to
    :param object_name: s3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    '''

    # If s3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.download_file(bucket, file_name, file_name)
        #print(f's3 Download: {response}')
    except ClientError as e:
        print(f's3 download error {e}')
        return False
    return True


def ps_convert_date_to_iso(date_str):
    '''
    #assume date into that format yyyy-mm-ddTHH:MM:SS.MMMZ, will return yyyy-mm-dd HH:MM:SS

    :param date_str:
    :return date in iso format:
    '''
    begin = date_str[0:10]
    end = date_str[11:19]
    return begin + " " + end


def ps_build_start_end_date_from_now(days=1):
    req_endtime = datetime.utcnow()
    delta = timedelta(days=days)
    req_starttime = req_endtime - delta

    req_endtime_str = req_endtime.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    req_starttime_str = req_starttime.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    return req_starttime_str, req_endtime_str

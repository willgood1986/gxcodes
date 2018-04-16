import urllib
import requests
import re
from bs4 import BeautifulSoup  
import gzip
import sys
import json


class HelpUtil:
    @staticmethod
    def wash_data(_pure_data):
        mid_str = _pure_data
        while mid_str.find(",,") > 0:
            mid_str = mid_str.replace(",,", ",666666,", 1)

        return mid_str

    @staticmethod    
    def get_raw_json_content(json_data):
        start_str = 'kfdatas:'
        end_str = ',fbdatas'

        start_index = json_data.find(start_str)
        end_index = json_data.find(end_str)

        print('start_index:{}, end_index:{}'.format(start_index, end_index))

        if min([start_index, end_index]) > 0:
            pure_data = json_data[start_index + len(start_str):end_index]
            return pure_data

        return None

class FundData:
    def __init__(self, src_data, is_file = False):
        self.src_data = src_data
        self.is_file = is_file
        self.fund_lst = []
        self.is_parsed = False

    def get_content_from_file(self):
        try:
            with open(self.src_data) as f:
                file_content = f.read()
                return file_content
        except Exception as e:
            print('Unable to open the file, please check the argument of src_data ...')

    def __get_raw_content(self):
        fixed_header = 'var dbCache='
        self.raw_content = self.src_data
        if self.is_file:
           self.raw_content = self.get_content_from_file()

        if len(self.raw_content) > 0:
            return self.raw_content
        else:
            return None

    # @staticmethod
    # def wash_data(_pure_data):
    #     mid_str = _pure_data
    #     while mid_str.find(",,") > 0:
    #         mid_str = mid_str.replace(",,", ",666666,", 1)

    #     return mid_str

    # @staticmethod    
    # def __get_raw_json_content(json_data):
    #     start_str = 'kfdatas:'
    #     end_str = ',fbdatas'

    #     start_index = json_data.find(start_str)
    #     end_index = json_data.find(end_str)

    #     print('start_index:{}, end_index:{}'.format(start_index, end_index))

    #     if min([start_index, end_index]) > 0:
    #         pure_data = json_data[start_index + len(start_str):end_index]
    #         return pure_data

    #     return None


    def __parse_data(self):
        self.is_parsed = True
        raw_content = self.__get_raw_content()
        if raw_content:
            raw_json_content = HelpUtil.get_raw_json_content(raw_content)
            if raw_json_content:
                washed_data = HelpUtil.wash_data(raw_json_content)
                self.try_to_load(washed_data)
        else:
            print('Failed to get raw_content ...')

    def try_to_load(self, json_data):
        try:
            self.fund_lst = json.loads(json_data)
            print('Load json format data successfully, the length is:{}'.format(len(self.fund_lst )))
        except Exception as e:
            print('Faile to load json data ..., source data is:{}'.format(json_data))

    def get_struct_data(self):
        if not self.is_parsed:
            self.__parse_data()

        return self.fund_lst

class UpRateData:
    def __init__(self, src_data, is_file = False):
        self.src_data = src_data
        self.is_file = is_file
        self.fund_lst = []
        self.is_parsed = False

    def get_content_from_file(self):
        try:
            with open(self.src_data) as f:
                file_content = f.read()
                return file_content
        except Exception as e:
            print('Unable to open the file, please check the argument of src_data ...')

    def __get_raw_content(self):
        fixed_header = 'var dbCache='
        self.raw_content = self.src_data
        if self.is_file:
           self.raw_content = self.get_content_from_file()

        if len(self.raw_content) > 0:
            return self.raw_content
        else:
            return None

    @staticmethod
    def wash_data(_pure_data):
        mid_str = _pure_data
        while mid_str.find(",,") > 0:
            mid_str = mid_str.replace(",,", ",666666,", 1)

        return mid_str

    @staticmethod    
    def __get_raw_json_content(json_data):
        start_str = 'kfdatas:'
        end_str = ',fbdatas'

        start_index = json_data.find(start_str)
        end_index = json_data.find(end_str)

        print('start_index:{}, end_index:{}'.format(start_index, end_index))

        if min([start_index, end_index]) > 0:
            pure_data = json_data[start_index + len(start_str):end_index]
            return pure_data

        return None


    def __parse_data(self):
        self.is_parsed = True
        raw_content = self.__get_raw_content()
        if raw_content:
            raw_json_content = HelpUtil.get_raw_json_content(raw_content)
            if raw_json_content:
                washed_data = HelpUtil.wash_data(raw_json_content)
                self.try_to_load(washed_data)
        else:
            print('Failed to get raw_content ...')

    def try_to_load(self, json_data):
        try:
            self.fund_lst = json.loads(json_data)
            print('Load json format data successfully, the length is:{}'.format(len(self.fund_lst )))
        except Exception as e:
            print('Faile to load json data ..., source data is:{}'.format(json_data))

    def get_struct_data(self):
        if not self.is_parsed:
            self.__parse_data()

        return self.fund_lst


common_headers = {
"__RequestVerificationToken": "9EbS6CZbi9p77EIhfuNbp5aK5c1WdcZrC4KHTE9W24v8oakFXl6iUu770gTaeW-Y0D2KjDDba4Lzyz3PWpBEiwG9F_k1",
'_deviceType': 'Web',
'_domainName': 'passport.eastmoney.com',
'_productType': 'UserPassport',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
'Connection': 'keep-alive',
"Content-Length": "57",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"Cookie": 'st_pvi=37314769394701; st_si=24205021338198; __RequestVerificationToken=9AvLBYCR__LlGJbEEsIsLEhmfCLhhJWLr7WafWxXlbgg0Pufm2BkvqZEK1NktVrjiLJ_da-BnrwtnCmSGNlnz5bS_FI1; qgqp_b_id=ea201329d54f2398273b9b0777bb6bf2; RequestData={"agentPageUrl":"https://passport.eastmoney.com/pub/LoginAgent","redirectUrl":"http://fund.eastmoney.com/favor.html?0.8012498411202804","callBack":"LoginCallBack","redirectFunc":"PageRedirect","data":{"domainName":"passport.eastmoney.com","deviceType":"Web","productType":"UserPassport","versionId":"0.0.1"}}',
"Host": "exaccount2.eastmoney.com",
"Origin": "https://exaccount2.eastmoney.com",
"Referer": "https://exaccount2.eastmoney.com/home/Login?rc=1297144009",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
"X-Requested-With": "XMLHttpRequest"
           }

def login_ex(_data):
    s = requests.session()
    after_url = 'http://fund.eastmoney.com/Data/FavorCenter_v3.aspx?o=r&rnd=1523713075514'
    up_info_url = 'http://fund.eastmoney.com/Data/FavorCenter_v3.aspx?o=r&rnd=1523885446559'
    login_url = 'http://exaccount2.eastmoney.com/JsonAPI/Login'
    login_ret = s.post(login_url, data=_data, headers=common_headers)
    if login_ret.status_code == 200:
        ret = s.get(after_url)
        ret_up = s.get(up_info_url)
    else:
        print('Failed to login ...')
        return None
    # print('Is it the data:{}'.format(ret.text))
    _content = (ret.text, ret_up.text)

    return _content

def save_content(_content):
    with open('my_content.html', 'w+') as f:
        f.write(_content)

def parse_data(json_data):
    start_str = 'kfdatas:'
    end_str = ',fbdatas'

    start_index = json_data.find(start_str)
    end_index = json_data.find(end_str)

    print('start_index:{}, end_index:{}'.format(start_index, end_index))

    if min([start_index, end_index]) > 0:
        pure_data = json_data[start_index + len(start_str):end_index]
        print('pure data is:{}'.format(pure_data))
        washed_data = __wash_data(pure_data)
        dict_data = json.loads(washed_data)
        print('type of dict_data is:{}'.format(type(dict_data)))
        return dict_data

    return None

def __wash_data(raw_data, place_holder = -9999):
    mid_str = raw_data
    while mid_str.find(",,") > 0:
        mid_str = mid_str.replace(",,", ',' + str(place_holder) + ',', 1)

    return mid_str


def main():
    login_data = {
        'username': '13926991859',
        'password': '547583658',
        'vcode': '',
        'x': 794,
        'y': 430
    }

    _head = 'var dbCache='

    _content = login_ex(login_data)
    fd = FundData(_content[0])
    urd = UpRateData(_content[1])
    # print('up info:{}'.format(_content[1]))
    ret = fd.get_struct_data()
    ur_ret = urd.get_struct_data()
    print('The struct data is, unit_net_val:{}, culculating_val:{}, day_up_rate:{}'.format(ret[1][18], ret[1][19], ret[1][23]))
    print('The struct data is, day_up_rate:{}'.format(ur_ret[1][-8]))  

if __name__ == '__main__':
    main()
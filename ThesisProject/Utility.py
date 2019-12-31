__author__ = 'admin'
import datetime
import time
import xlrd
import xlsxwriter
import openpyxl
import random
import requests
import configparser
import os
import pymysql
import sys
import numpy as np

cf = configparser.ConfigParser()
cf.read('Configure.ini')

execPath = os.path.dirname(os.path.abspath(__file__)) + "\\"
host = 'localhost'
user = 'root'
pwd = 'admin'
dbName = 'thesisdatasset'
class TestUtility:

    strFileName = execPath + str(datetime.date.today().strftime("%Y_%m_%d")) + '.txt'
    print(strFileName)
    # def __init__(self):
        #filePath = cf['LogFile']['userPWD']
    def getDBCountryList():
        conn = pymysql.connect(host,user,pwd,dbName,cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor()
        cursor.execute("select *from DevelopedCountry where `Country Name` = 'Australia'")
        counResult = cursor.fetchall()
        counResult[0].pop("Country Name")
        counResult[0].pop("Country Code")
        counDic = counResult[0]
        cursor.close()
        conn.close()
        return counDic

    def getCountryByNameList(countryName):

        conn = pymysql.connect(host, user, pwd, dbName, cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor()
        sqlStr = "select *from DevelopedCountry where `Country Name` = '{CouName}'" .format(
            CouName = countryName
        )
        cursor.execute(sqlStr)
        counResult = cursor.fetchall()
        counResult[0].pop("Country Name")
        counResult[0].pop("Country Code")
        counDic = counResult[0]
        couYList = list(counDic.values())
        couYList = list(map(float, couYList))
        yItem = []
        for i in couYList:
            yItem.append(int(i))

        cursor.close()
        conn.close()
        return yItem

    def convFlStr(self,val):
        if isinstance(val,float):
            val = str(int(val))
        return val

    def getExcelFile(path):
        try:
            xls = xlrd.open_workbook(path)
            # print(len(xls.sheets()))
            value_rows = []
            sheetOne = xls.sheets()[0]
            rows = sheetOne.nrows
            for r in range(1,rows):
                strVal =sheetOne.row_values(r)
                value_rows.append(strVal)
        except:
            print(path)
        return value_rows
    def creaComFile(fileName):
        getFile = execPath +  fileName

        if(os.path.exists(getFile)):
            return
        else:
            f = open(getFile,'w')
            f.close()
        return

    def creaLogFile():
        print(TestUtility.strFileName)
        print(os.path.exists(TestUtility.strFileName))
        if(os.path.exists(TestUtility.strFileName)):
            return
        else:
            f = open(TestUtility.strFileName,'w')

            f.close()
        return
    def renameFile(src,dsc):
        os.rename(src, dsc)
    def removeFile(strPositionFile):
        os.remove(strPositionFile)
    def removeFileOneRow(strPositionFile):
        with open(strPositionFile, 'r') as fcopy:
            rowlist = fcopy.readlines()
            delrow = rowlist[0]
        strTemp = r'D:\PythonProj\Aarena\NewList.txt'
        fp = open(strTemp, 'w', encoding='utf-8')
        for l in rowlist:
            if not l.__eq__(delrow):
                fp.write(l)
        fp.close()
        TestUtility.removeFile(strPositionFile)
        TestUtility.renameFile(strTemp,strPositionFile)


    #

    def readFileOneRow(strPositionFile):
        with open(strPositionFile, 'r') as fin:
            dalist = fin.readlines()
            data = dalist[0]
        return data

    def getFileRows(strPositionFile):
        rows = 0
        rows = len(open(strPositionFile, 'rU').readlines())
        return rows
    def wrPositions(strGet,strPositionFile):
        fp = open(strPositionFile,'a',encoding = 'utf-8')
        fp.write(strGet)
        fp.close()

    def resLog(strTCName,strRes):
        timeStamp = str(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))
        try:
            strIni = 'TestResLog : ' + strTCName
            resLog = strIni + '_' + strRes
            finaStr = resLog + '__' + timeStamp + '\n'
            fp = open(TestUtility.strFileName,'a',encoding='utf-8')
            fp.write(finaStr)
            fp.close()
        except:
            print('System Exception Error!')
        return

    def infoLog(strMsg):
        timeStamp = str(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))
        try:
            strIni = '---------> '
            msgLog = 'TestMsgLog:__' + strMsg
            finaStr = strIni + msgLog + '__' + timeStamp + '\n'
            fp = open(TestUtility.strFileName,'a',encoding='utf-8')
            fp.write(finaStr)
            fp.close()
        except:
            print('System Exception Error!')
        return

    def getFile(path):
        file = open(path)
        for line in file:
            print(line.strip())
        return

    def getPhoneNum(*args):
        prelist=["130","131","132","133","134","135","136","137","138","139","147","150","151","152","153","155","156","157","158","159","186","187","188"]
        return random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8))
    def getVerifyCode(self,strPhoneNumber):
        registUrl = 'http://13.124.220.217:8010/Account/GetCheckCode?phoneNum=' + strPhoneNumber
        regisCode = requests.get(registUrl)
        return regisCode.text

    # def get_ele_times(self,driver,times,func):
    #     return WebDriverWait(driver,times).until(func)

    # def get_Jenkins():
    #     JenkinsServer = jenkins.Jenkins('http://localhost:8080',username='admin',password = 'Admin')
    #     print('Here')
    #     user = JenkinsServer.get_whoami()
    #     print(user['fullName'])
    #     version = JenkinsServer.get_version()
    #     print('Hello %s from Jenkins %s' % (user,version))
    #     return












'''
    def CommonUserLogin(self,):
        MTWeb.txtUserName().click()
        MTWeb.txtUserName().send_keys(cf['UserInfo']['userName'])
        MTWeb.txtPWD().click()
        MTWeb.txtPWD().send_keys(cf['UserInfo']['userPWD'])
        MTWeb.btnLogin().click()
        sleep(3)
'''


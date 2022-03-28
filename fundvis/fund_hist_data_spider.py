'''
    爬取指定基金的历史数据
    - 单位净值
    - 累计净值
    - 日增长率
'''
import csv

import prettytable as pt
import requests
from bs4 import BeautifulSoup


def spider(code,start,end):
    tb = pt.PrettyTable(['净值日期', '单位净值', '累计净值', '日增长率','申购状态','赎回状态'])
    result=[]
    url='http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code='+code+'&page=1&sdate='+start+'&edate='+end+'&per=20'
    res=requests.get(url)
    pageNum=int(res.text.split(',')[-2].split(':')[1])
    bsobj=BeautifulSoup(res.text,'lxml')
    tds=bsobj.findAll('td')
    cur_row=[]
    # print(tds)
    # f=open('./templates/dat/'+code+'.csv', 'w', newline='')
    # csv_writer=csv.writer(f)
    for td in tds:
        if td.get_text() == '':
            # print(cur_row)
            if len(cur_row) == 6:
                tb.add_row(cur_row)
                result.append(cur_row)
                # csv_writer.writerow(cur_row)
            cur_row=[]
        else:
            cur_row.append(td.get_text())



    for page in range(2,pageNum+1):
        url='http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code='+code+'&page='+str(page)+'&sdate='+start+'&edate='+end+'&per=20'
        res=requests.get(url)
        bsobj = BeautifulSoup(res.text, 'lxml')
        tds = bsobj.findAll('td')
        cur_row = []
        for td in tds:
            if td.get_text() == '':
                if len(cur_row) == 6:
                    tb.add_row(cur_row)
                    result.append(cur_row)
                    # print(cur_row)
                    # csv_writer.writerow(cur_row)
                cur_row = []
            else:
                cur_row.append(td.get_text())

    # print(tb)

    # result=result[::-1]
    # print(result)
    # print(result)
    # csv_writer.writerow(['日期','单位净值','累计净值','涨跌幅','申购状态','赎回状态'])
    # for item in result:
    #     csv_writer.writerow(item)
    # f.close()

    return result

def fund_hist_data_run(fundcode, start, end):
    return spider(fundcode,start,end)
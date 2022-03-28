import csv


def read_hist_data(fund_code):
    data=[]
    with open('./templates/dat/'+fund_code+'.csv', 'r') as f:
        data=[line.split(',')[0:-2] for line in f]
    # print(data)

    MAN = 5
    for idx in range(MAN-1, len(data)):
        MA5 = 0
        x = 0
        while x != MAN:
            MA5 = MA5 + float(data[idx-x][1])
            x = x + 1
        MA5 = MA5 / MAN
        data[idx].append('%.4f' % MA5)
        bias5 = (float(data[idx][1]) - MA5) / MA5 * 100
        data[idx].append('%.3f' % bias5)

    MAN=10 # MAN日均线参数
    for idx in range(MAN-1, len(data)):
        MA10=0
        x=0
        while x!=MAN:
            MA10=MA10+float(data[idx-x][1])
            x=x+1
        MA10=MA10/MAN
        data[idx].append('%.4f' % MA10)
        bias10 = (float(data[idx][1]) - MA10) / MA10 * 100
        data[idx].append('%.4f' % bias10)

    MAN=30
    for idx in range(MAN-1, len(data)):
        MA30=0
        x=0
        while x!=MAN:
            MA30=MA30+float(data[idx-x][1])
            x=x+1
        MA30 = MA30 / MAN
        data[idx].append('%.4f' % MA30)
        bias30 = (float(data[idx][1]) - MA30) / MA30 * 100
        data[idx].append('%.4f' % bias30)

    MAN=60
    for idx in range(MAN-1, len(data)):
        MA60=0
        x=0
        while x!=MAN:
            MA60=MA60+float(data[idx-x][1])
            x=x+1
        MA60=MA60/MAN
        data[idx].append('%.4f' % MA60)
        bias60=(float(data[idx][1]) - MA60) / MA60 * 100
        data[idx].append('%.4f' % bias60)
        data[idx].append(0) # 插入0线数据，作为BIAS（乖离率）基准线



    # print(data)
    with open('./templates/dat/'+fund_code+'MA.csv','w',newline='')as fp:
        csv_writer=csv.writer(fp)
        csv_writer.writerow(['日期','单位净值','累计净值','跌涨幅','MA5', 'BIAS5','MA10','BIAS10','MA30','BIAS30','MA60','BIAS60','0线'])
        for item in data[MAN:]:
            csv_writer.writerow(item)

def MA(fund_code):
    read_hist_data(fund_code)

pool = ['519674','001579','501048','161725','001790','050026','320007','161726','002611']

for fd in pool:
    MA(fd)
# MA('001790')
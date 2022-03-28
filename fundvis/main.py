# from cal_MA import MA
from colorprint import Colored
from fund_hist_data_spider import fund_hist_data_run

'''
    ----------------------------------------------------------------
    |**************************************************************|
    |--------------         交易系统入口           ----------------|
    |**************************************************************|
    |--------------------------------------------------------------|
'''

color = Colored()

if __name__ == '__main__':
    while True:

        print('----------------------------------------------------------------------------------------------------------\n---------------------'+color.yellow('Trade System')+'--------------------\n----------------------------------------------------------------------------------------------------------\n')
        option = int(input('输入选项：\n2. 获取历史数据，计算均线\n'))
        # if option == 1:
        #     spider()
        #     display_fund()
        #     save_data()
        if option == 2:
            # 爬取个基的历史数据
            start = input('输入数据的开始日期：')
            end = input('输入数据的结束日期：')
            with open('fund_pool.txt', 'r') as f:
                for fund_code in f:
                    fund_hist_data_run(fund_code.strip('\n'), start, end) # 爬取基金的历史数据
                    # MA(fund_code.strip('\n'))
                    print(color.red('计算数据成功，数据保存到'+fund_code.strip('\n')+'.csv文件中!'))
        else:
            print('Exit successfully !!!\n')
            break
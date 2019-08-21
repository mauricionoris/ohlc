#import numpy as np
#import pandas as pd
#from pandas_datareader import data as wb
import titulos_negociaveis as tn
import cotahist as ch


# define an empty list
places = []

# with open('data/titneg.tsv', 'w') as filehandle:
#     for listitem in p:
#         filehandle.write('%s\t' % listitem)
#
# with open('data/emp.tsv', 'w') as filehandle:
#     for listitem in e:
#         filehandle.write('%s\t' % listitem)
#

param = {
    'cotahist':{'zipPath': '/media/sf_repo/ohlc/cotahist/COTAHIST_A2019.ZIP', 'file': 'COTAHIST_A2019.TXT'}
,   'titneg':{'zipPath': '/media/sf_repo/ohlc/titneg/Titulos_Negociaveis.zip', 'file': 'TITULOS_NEGOCIAVEIS.TXT'}
}


p , e = tn.getItems(param['titneg']['zipPath'], param['titneg']['file'])
c = ch.getItems(param['cotahist']['zipPath'], param['cotahist']['file'])

for i in p:
    print(i)

for i in c:
    print(i)



#
# TickerA='ITSA4.SA'
# TickerB='FLRY3.SA'
# TickerC='LREN3.SA'
# prices=pd.DataFrame()
# tickers = [TickerA, TickerB, TickerC]
# for t in tickers:
#     prices[t]=wb.DataReader(t, data_source='yahoo', start='2010-1-1')['Adj Close']


#import os
#print(os.environ.get("PATH"))

import pandas_datareader as web
import datetime

start = datetime.datetime(2015, 9, 1)
end = datetime.datetime(2021, 2, 12)

df = web.DataReader("msft", 'yahoo', start, end)   

df.to_csv('MSFT_Historical_Data.csv')
from sqlalchemy import create_engine
from sqlalchemy.types import *
import pandas as pd


server = '140.134.25.164'  # DESKTOP-2LNIJAK\SQLEXPRESS'  :57226
username = r'Vivian'  #DESKTOP-2LNIJAK\Vivian
password = 'L102210221022'
database_name = 'traing_result'
port = 1433

conn_str = f'mssql+pymssql://{username}:{password}@{server}:{port}/{database_name}'
engine = create_engine(conn_str)
# conn = engine.connect()

resultDF = pd.read_csv('./data/Step_0_ANN_Two_Result.csv', index_col=False)
resultDF['learning_rate'] = resultDF['learning_rate'].map('{:.20f}'.format)  # Suppressing scientific notation in pandas
resultDF['score'] = resultDF['score'].map('{:.2f}'.format)
resultDF['rmse'] = resultDF['rmse'].map('{:.2f}'.format)
resultDF['spendTime'] = resultDF['spendTime'].map('{:.2f}'.format)
resultDF.to_sql('ANN_Two_Result', engine, if_exists='replace', index=False,
                dtype={'modelName': NVARCHAR(30),
                       'score': Float(),
                       'rmse': Float(),
                       'spendTime': Float(),
                       'executionTime_s': DateTime(),
                       'startDate': Date(),
                       'endDate': Date(),
                       'random_seed': SmallInteger(),
                       'Dense1Units': SmallInteger(),
                       'Dense2Units': SmallInteger(),
                       'learning_rate': Float(),
                       'decay': Float(),
                       'momentum': Float(),
                       'nesterov': NVARCHAR(10),
                       'optimizer': NVARCHAR(10),
                       'loss': NVARCHAR(20),
                       'epochs': SmallInteger(),
                       'verbose': SmallInteger(),
                       'batch_size': SmallInteger(),
                       'machine': NVARCHAR(20),
                       'runProcess':  NVARCHAR(20),
                       }
                )
print('End')


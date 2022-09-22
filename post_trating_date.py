import pandas as pd
import datetime as dt

class trating_date:
    def __init__(self, path, file_, colunm_date):

        print('***********************')
        print('Start Code Trating date')
        self.df = f'{path}/{file_}'
        self.path = path
        self.column = colunm_date

    def run(self):

        df_final = pd.read_csv(f'{self.df}', sep=';')
        df_final['Data'] = pd.to_datetime(df_final['Data'], dayfirst=True)
        df_final['Month_Year'] = df_final['Data'].dt.strftime("%m-%Y")
        df_final['Year'] = df_final['Data'].dt.strftime("%Y")
        df_final.to_csv(f'{self.path}/new_columns.csv', index=False)
        print('End Code Trating date')
        print('***********************')


trating_date('C:/Users/user/OneDrive/Documents', 'to_tranform_in_date_time.csv', 'Data').run()
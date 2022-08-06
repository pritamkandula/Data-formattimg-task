import pandas as pd
import datetime as dt
import json


def user_data(json_file):
        with open(json_file,'r') as f:
                    saat = json.load(f)

        epoch_time = []
        users = []
        for ep in saat:
                epoch = saat[ep]['redeemed_at']
                epoch_time.append(epoch)

        for i in range(len(epoch_time)):
                epoch_time[i] = epoch_time[i]/1000

        proper = []
        for i in range(len(epoch_time)):
                extracted_date = dt.datetime.fromtimestamp(epoch_time[i])
                proper_date = extracted_date.strftime("%b-%Y")
                proper.append(proper_date)

        for user in saat:
            us = saat[user]['user_id']
            users.append(us)

        df=pd.DataFrame(zip(users,proper))
        df.rename(columns = {0: 'User_ids', 1: 'Dates'}, inplace = True)

        df1 = pd.DataFrame(columns = df['Dates'].unique())
        for date in df['Dates'].unique():
            df1[date] = df.where(df['Dates'] == date).dropna()['User_ids'].value_counts(sort = False)
        df1.index.names = ['User_ids']
        return df1

    
#user_data("SampleData.json")   
#df1.to_csv("C:\\Users\\User\\Desktop\\assignments\\saathealth\\user_data_op.csv")   
    



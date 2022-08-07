import pandas as pd
import datetime as dt
import json


def user_data(json_file):
        #loading the json file
        with open(json_file,'r') as f:
                    saat = json.load(f)

        epoch_time = []
        users = []
        #storing all the epoch timestamps in the epoch_time list
        for ep in saat:
                epoch = saat[ep]['redeemed_at']
                epoch_time.append(epoch)
        
        #conversion of timestamps to seconds
        for i in range(len(epoch_time)):
                epoch_time[i] = epoch_time[i]/1000

        proper = []
        #conversion timestamps to the required date format
        for i in range(len(epoch_time)):
                extracted_date = dt.datetime.fromtimestamp(epoch_time[i])
                proper_date = extracted_date.strftime("%b-%Y")
                proper.append(proper_date)
        
        #storing all the user_ids from the json file in a list
        for user in saat:
            us = saat[user]['user_id']
            users.append(us)
        
        #creating a dataframe by taking user_ids and the proper date list as an input and aggregating them as a tuple
        df=pd.DataFrame(zip(users,proper))
        df.rename(columns = {0: 'User_ids', 1: 'Dates'}, inplace = True)
        
        #creating another dataframe with all the unique dates as columns
        df1 = pd.DataFrame(columns = df['Dates'].unique())
        #iterating over every date in the df dataframe to match with the date of df1 dataframe and to count the transactions done by every user_id in every unique date 
        #here index is set to User_ids
        for date in df['Dates'].unique():
            df1[date] = df.where(df['Dates'] == date).dropna()['User_ids'].value_counts(sort = False)
        df1.index.names = ['User_ids']
        #output of the final dataframe
        return df1

    
#user_data("SampleData.json")   
#df1.to_csv("C:\\Users\\User\\Desktop\\assignments\\saathealth\\user_data_op.csv")   
    



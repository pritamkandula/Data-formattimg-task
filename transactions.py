from overview import user_data

trans = user_data('SampleData.json')
for i in range(len(trans.index)):
     print('The User_id {} has made {} transactions in the 10 months period.'.format(trans.iloc[i].name,trans.iloc[i].sum()))

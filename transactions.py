from overview import user_data

trans = user_data('SampleData.json')
for i in range(len(trans.index)):
     print('The User_id {} has made {} transactions in the 10 months period.'.format(trans.iloc[i].name,trans.iloc[i].sum()))

with open("Sampledata.json",'r') as f:
    saat = json.load(f)
  
merchants = []
for i in saat:
    if (saat[i]['user_id']) == (saat[i]['k_user_id']):
        merchants.append(saat[i]['user_id'])
        
print('\nUser_ids who utilized the Merchant or K_user service in the 10 months period are:\n',merchants)

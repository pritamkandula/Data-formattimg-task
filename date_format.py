import json
import datetime as dt


def format_dates(json_file):
        with open(json_file,'r') as f:
            saat = json.load(f)

        epoch_time = []

        for ep in saat:
            epoch = saat[ep]['redeemed_at']
            epoch_time.append(epoch)


        for i in range(len(epoch_time)):
            epoch_time[i] = epoch_time[i]/1000
        
        proper = []
        for i in range(len(epoch_time)):
            extracted_date = dt.datetime.fromtimestamp(epoch_time[i])
            proper_date = extracted_date.strftime("%d-%b-%Y")
            proper.append(proper_date)

        
        print('List of dates in proper format:\n', proper )
        print('Total values in epoch_time:', len(epoch_time))
        print('Total values in proper:', len(proper))

        # with open('date_format_op.txt','w') as file:
        #     for row in proper:
        #         s = " ".join(map(str, row))
        #         file.write(s+'\n')

format_dates('SampleData.json')
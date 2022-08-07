import json
import datetime as dt


def format_dates(json_file):
        #loading the json file
        with open(json_file,'r') as f:
            saat = json.load(f)

        epoch_time = []
        #extracting all the epoch timestamps and storing it as a list in epoch_time empty list
        for ep in saat:
            epoch = saat[ep]['redeemed_at']
            epoch_time.append(epoch)

        #converting all the timestamps in the list to seconds
        for i in range(len(epoch_time)):
            epoch_time[i] = epoch_time[i]/1000
        
        proper = []
        #performing the conversion of the epoch timestamps to a proper date format using the datetime module
        for i in range(len(epoch_time)):
            extracted_date = dt.datetime.fromtimestamp(epoch_time[i])
            proper_date = extracted_date.strftime("%d-%b-%Y")
            proper.append(proper_date)

        #output
        print('List of dates in proper format:\n', proper )
        #checking if the number of values before conversion and after conversion are equal
        print('Total values in epoch_time:', len(epoch_time))
        print('Total values in proper:', len(proper))

        # with open('date_format_op.txt','w') as file:
        #     for row in proper:
        #         s = " ".join(map(str, row))
        #         file.write(s+'\n')

format_dates('SampleData.json')

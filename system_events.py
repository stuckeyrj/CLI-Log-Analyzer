#This is the parser for system events
import os
import csv

#DATA_DIR = "data"
#file_path = os.path.join(DATA_DIR,"system_events.csv")

def system_events_parser(file_path):
    missing_data = []
    good_data = []
    critical_data = []

    with open(file_path,'r') as csvfile:
        reader = csv.DictReader(csvfile) 
        for row in reader:
            if not row['timestamp'] or not row['system'] or not row['event_code']  or not row['severity'] or not row['message']:
                missing_data.append(row)
            
            if row['severity'] == 'WARN' or  row['severity'] == 'ERROR':
                critical_data.append(row)
            else:
                good_data.append(row)
            
        
    print(f"Good data reads: {len(good_data)}")
    print(f"Bad data reads: {len(critical_data)}")

    print(f"--------------- GOOD DATA ---------------")
    for entry in good_data:
        print (entry)

    print(f"--------------- BAD DATA ---------------")
    for entry in critical_data:
        print ("timestamp: " + entry['timestamp'] + ", Severity: " + entry['severity'], "Incident: " + entry['message'])
            
              
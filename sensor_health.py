#This is the parser for sensor health data
import os
import csv

#DATA_DIR = "data"
#file_path = os.path.join(DATA_DIR,"sensor_health.csv")

def sensor_health_parser(file_path):
    missing_data = []
    good_data = []
    bad_data = []

    with open(file_path,'r') as csvfile:
        reader = csv.DictReader(csvfile) 
        for row in reader:
            if not row['timestamp'] or not row['sensor_id'] or not row['temperature_c']  or not row['voltage_v'] or not row['health_status']:
                missing_data.append(row)
            
            if row['health_status'] == 'CRITICAL' or  row['health_status'] == 'WARN':
                bad_data.append(row)
            else:
                good_data.append(row)
            
        
    print(f"Good data reads: {len(good_data)}")
    print(f"Bad data reads: {len(bad_data)}")

    print(f"--------------- GOOD DATA ---------------")
    for entry in good_data:
        print (entry)

    print(f"--------------- BAD DATA ---------------")
    for entry in bad_data:
        print (entry)
            


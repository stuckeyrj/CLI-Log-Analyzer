# this is the parser for mission telemetry data
import os
import csv 

#DATA_DIR = "data"

#file_path = os.path.join(DATA_DIR, "mission_telemetry.csv")
#file_path = "/data/mission_telemetry.csv"
def mission_telemetry_parser(file_path):
    missing_data = []
    good_data = []
    bad_data = []
    # Add parsing logic here
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if not row['timestamp'] or not row['vehicle_id'] or not row['altitude_m'] or not row['speed_mps'] or not row['fuel_pct'] or not row['status']:
                missing_data.append(row)
            
            if row['status'] == 'OK' and int(row['altitude_m']) > 0:
                good_data.append(row)

            else: 
                bad_data.append(row)
    print(f"Missing Data Entries: {len(missing_data)}")
    print(f"Good Data Entries: {len(good_data)}")
    print(f"Bad Data Entries: {len(bad_data)}")
    print("--------------------------------------------------------------")
    print("Bad data")
    for entry in bad_data:
        print("Timestamp: " + entry['timestamp'] + ", vehicle_id " + entry['vehicle_id'])
    print ("--------------------------------------------------------------")
    print("Missing data")
    for entry in missing_data:
        print(entry)
    print("--------------------------------------------------------------")
    print("Good data")
    for entry in good_data:
        print(entry)
    







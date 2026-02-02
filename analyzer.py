import os
import mission_telemetry
import operator_commands
DATA_DIR = "data"

def main():
    print("Starting analysis...\n")

    for filename in os.listdir(DATA_DIR):
        file_path = os.path.join(DATA_DIR, filename)

        # Skip non-files
        if not os.path.isfile(file_path):
            continue

        if filename == "mission_telemetry.csv":
            print(f"Routing {filename} to telemetry analyzer")
            mission_telemetry(filename)
        elif filename == "system_events.csv":
            print(f"Routing {filename} to system event analyzer")
            operator_commands(filename)
        elif filename == "operator_commands.csv":
            print(f"Routing {filename} to operator command analyzer")
        
        elif filename == "sensor_health.csv":
            print(f"Routing {filename} to sensor health analyzer")

        else:
            print(f"Unknown file type: {filename}")


    





if __name__ == "__main__":
    main()
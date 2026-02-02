import os
from sensor_health import sensor_health_parser
from system_events import system_events_parser
from mission_telemetry import mission_telemetry_parser
from operator_commands import operator_commands_parser
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
            mission_telemetry_parser(file_path)
        elif filename == "system_events.csv":
            print(f"Routing {filename} to system event analyzer")
            system_events_parser(file_path)
        elif filename == "operator_commands.csv":
            print(f"Routing {filename} to operator command analyzer")
            operator_commands_parser(file_path)
        elif filename == "sensor_health.csv":
            print(f"Routing {filename} to sensor health analyzer")
            sensor_health_parser(file_path)
        else:
            print(f"Unknown file type: {filename}")


    





if __name__ == "__main__":
    main()
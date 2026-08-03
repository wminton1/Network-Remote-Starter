#still working on it
from fordpass import Vehicle
import sys

# --- CONFIGURATION ---
# app login strings here
USER_EMAIL = "@gmail.com"
USER_PASS  = ""
VEHICLE_VIN = ""


print("Connecting to Ford Cloud servers...")

try:
    # 1. Initialize the authenticated vehicle channel
    my_car = Vehicle(USER_EMAIL, USER_PASS, VEHICLE_VIN)
    
    # The initialization handles the complex client_id rotation under the hood.
    print("Auth Success! Checking  odometer mileage...")
    car_status = my_car.status()
    
    # Grab a generic telemetry metric to prove data parsing works
    odometer = car_status.get("odometer", {}).get("value", "Unknown")
    print(f" Odometer Reading: {odometer} miles")
    
    # 2. Trigger the physical starter command
    print("Sending car start command...")
    
    my_car.start()
    
    print("Command executed successfully!")

except Exception as e:
    print(f"Error encountered: {str(e)}")
    sys.exit(1)

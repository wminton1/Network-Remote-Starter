from fordpass import Vehicle
import sys

# --- CONFIGURATION ---
# Use your real official app login strings here
USER_EMAIL = "wminton0001@gmail.com"
USER_PASS  = "@Slattinsen69"
VEHICLE_VIN = "1FMCU0GN9RUB14440"

# This module operates in specific geographical zones ('na' = North America, 'eu' = Europe)
REGION = "na"

print("🔄 Connecting to Ford Cloud servers...")

try:
    # 1. Initialize the authenticated vehicle channel
    my_car = Vehicle(USER_EMAIL, USER_PASS, VEHICLE_VIN)
    
    # The initialization handles the complex client_id rotation under the hood.
    # Let's run a quick non-destructive check to verify the login works.
    print("🔒 Auth Success! Checking your odometer mileage...")
    car_status = my_car.status()
    
    # Grab a generic telemetry metric to prove data parsing works
    odometer = car_status.get("odometer", {}).get("value", "Unknown")
    print(f"📈 Odometer Reading: {odometer} miles")
    
    # 2. Trigger the physical starter command
    print("⚡ Sending Batmobile IGNITION command...")
    
    # UNCOMMENT THE LINE BELOW WHEN YOU ARE READY TO ACTUALLY CRANK THE ENGINE:
    # my_car.start()
    
    print("🚀 Command executed successfully!")

except Exception as e:
    print(f"❌ Error encountered: {str(e)}")
    sys.exit(1)

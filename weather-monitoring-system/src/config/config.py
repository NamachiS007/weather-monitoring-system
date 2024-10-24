import os

class Config:
    OPENWEATHERMAP_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
    POLL_INTERVAL =300  # Every 5 minutes
    ALERT_THRESHOLD = 35  # Temperature threshold for alerts in Celsius
    LOCATIONS = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

# Debugging print
print("API Key from Environment:", Config.OPENWEATHERMAP_API_KEY)
print()

# ==================================== Note ==============================================
# Note: if you are getting the output like 'None', check the environment variable is User Variable and add new User Variable "OPENWEATHERMAP_API_KEY = 'eab736a1b42c0fc051619ae25cba96db'" 
# see the third line below and run the command you will get the output :-)

# To run the script in debug mode, you can use the following command:
# PS D:\Visual Studio Code For Practicing\weather-monitoring-system\src\config> python -u "d:\Visual Studio Code For Practicing\weather-monitoring-system\src\config\config.py"
# API Key from Environment: None
# PS D:\Visual Studio Code For Practicing\weather-monitoring-system\src\config> $env:OPENWEATHERMAP_API_KEY = 'eab736a1b42c0fc051619ae25cba96db'; python -u "d:\Visual Studio Code For Practicing\weather-monitoring-system\src\config\config.py"
# API Key from Environment: eab736a1b42c0fc051619ae25cba96db
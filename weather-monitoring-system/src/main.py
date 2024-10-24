import time
from datetime import datetime
from services.api_service import APIService
from services.weather_summary import WeatherSummary
from services.alert_service import AlertService
from data.database import Database
from config.config import Config

def main():
    db = Database()
    summary = WeatherSummary()
    alert_service = AlertService()

    while True:
        print(f"Fetching weather data for locations: {Config.LOCATIONS}")
        
        for location in Config.LOCATIONS:
            weather_data = APIService.get_weather(location)
            
            # Print the fetched weather data for each location
            if weather_data.get("main"):
                current_temp = weather_data["main"]["temp"]
                main_condition = weather_data["weather"][0]["main"]
                date = datetime.now().date().isoformat()

                print(f"Weather data for {location}: Temperature: {current_temp}°C, Condition: {main_condition}")

                summary.add_weather_data(date, current_temp, main_condition)

                # Check and print alerts
                alert_message = alert_service.check_alert(current_temp)
                if alert_message:
                    print(alert_message)

        # Calculate and print daily summaries
        daily_summaries = summary.calculate_daily_summary()
        for date, data in daily_summaries.items():
            print()
            print(f"Daily Summary for {date}:")
            # Format the average temperature to one decimal place
            avg_temp_formatted = f"{data['average_temp']:.2f}"
            max_temp_formatted = f"{data['max_temp']:.2f}"
            min_temp_formatted = f"{data['min_temp']:.2f}"
            
            print(f"Avg Temp: {avg_temp_formatted}°C, Max Temp: {max_temp_formatted}°C, Min Temp: {min_temp_formatted}°C, Dominant Condition: {data['dominant_condition']}")
            print()
            
            # Store the summary in the database
            db.insert_daily_summary(date, data['average_temp'], data['max_temp'], data['min_temp'], data['dominant_condition'])

        print(f"Waiting for {Config.POLL_INTERVAL} seconds before fetching data again...")
        time.sleep(Config.POLL_INTERVAL)

if __name__ == "__main__":
    main()
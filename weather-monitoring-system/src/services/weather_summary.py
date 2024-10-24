from collections import defaultdict

class WeatherSummary:
    def __init__(self):
        self.daily_data = defaultdict(list)

    def add_weather_data(self, date, temp, condition):
        self.daily_data[date].append((temp, condition))

    def calculate_daily_summary(self):
        summaries = {}
        for date, records in self.daily_data.items():
            temperatures = [temp for temp, _ in records]
            conditions = [condition for _, condition in records]
            summaries[date] = {
                'average_temp': sum(temperatures) / len(temperatures),
                'max_temp': max(temperatures),
                'min_temp': min(temperatures),
                'dominant_condition': max(set(conditions), key=conditions.count)  # Most common condition
            }
        return summaries

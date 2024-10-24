from config.config import Config

class AlertService:
    def __init__(self):
        self.last_temp = None

    def check_alert(self, current_temp):
        if self.last_temp is not None and current_temp > Config.ALERT_THRESHOLD:
            return f"Alert! Temperature exceeded {Config.ALERT_THRESHOLD}°C: Current temperature is {current_temp}°C"
        self.last_temp = current_temp
        return None
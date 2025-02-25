class FloodRiskAnalyzer:
    def __init__(self, rainfall, river_level, wind_speed):
        self.rainfall = rainfall  # in mm
        self.river_level = river_level  # in meters
        self.wind_speed = wind_speed  # in km/h
        self.alerts = []

    def check_rainfall(self):
        if self.rainfall > 100:
            self.alerts.append("⚠️ Heavy Rainfall Alert! Risk of flooding.")
    
    def check_river_level(self):
        if self.river_level > 5:
            self.alerts.append("🚨 River Level Critical! Flood warning issued.")

    def check_wind_speed(self):
        if self.wind_speed > 80:
            self.alerts.append("🌪️ High Wind Speed Alert! Risk of storm-related flooding.")

    def check_urban_flood_risk(self):
        if self.rainfall > 80 and self.river_level > 4:
            self.alerts.append("⚠️ Urban Drainage Overflow Warning! Increased flood risk.")

    def check_combined_risk(self):
        if len(self.alerts) >= 2:
            self.alerts.append("🚨🚨 EMERGENCY ALERT! Multiple flood risk factors detected!")

    def analyze(self):
        self.check_rainfall()
        self.check_river_level()
        self.check_wind_speed()
        self.check_urban_flood_risk()
        self.check_combined_risk()

        return self.alerts if self.alerts else ["✅ No immediate flood risks detected."]


# Example: Input weather conditions
rainfall = 120  # mm
river_level = 5.5  # meters
wind_speed = 90  # km/h

# Run Flood Risk Analyzer
analyzer = FloodRiskAnalyzer(rainfall, river_level, wind_speed)
alerts = analyzer.analyze()

# Display results
for alert in alerts:
    print(alert)

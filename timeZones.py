from datetime import datetime
import pytz

#For more Time-Zones visit: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

def timeZone(city_name: str, city_time_zone: str):
    """Print the date of an specific time-zone"""
    city_timezone = pytz.timezone(city_time_zone)
    city_date = datetime.now(city_timezone)
    print(f"{city_name}: " + city_date.strftime("%d/%m/%Y, %H:%M:%S"))


def run():
    timeZone("Bogotá", "America/Bogota")

if __name__ == "__main__":
    run()





import random

# Simulated Sensor Data
def get_temperature():
    return round(random.uniform(25.0, 35.0), 2)

def get_ph():
    return round(random.uniform(5.5, 7.5), 2)

def get_tds():
    return round(random.uniform(800, 1500), 2)

def get_humidity():
    return round(random.uniform(60.0, 90.0), 2)

def get_water_level():
    return random.choice(["High", "Medium", "Low"])

# Sensor Logs
def get_temperature_log():
    return [get_temperature() for _ in range(10)]

def get_ph_log():
    return [get_ph() for _ in range(10)]

def get_tds_log():
    return [get_tds() for _ in range(10)]

def get_humidity_log():
    return [get_humidity() for _ in range(10)]

def get_water_level_log():
    return [get_water_level() for _ in range(10)]

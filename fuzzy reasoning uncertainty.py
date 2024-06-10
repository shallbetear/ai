import numpy as np
def trimf(x, params):
    a, b, c = params
    epsilon = 1e-10
    return np.maximum(0, np.minimum( x-a / max( b-a, epsilon), c-x / max( c-b, epsilon)))

temperature_values = fan_speed_values = humidity_values = np.arange(0, 101, 1)

temperature_low = trimf(temperature_values, [0, 0, 50])
temperature_medium = trimf(temperature_values, [0, 50, 100])
temperature_high = trimf(temperature_values, [50, 100, 100])

humidity_low = trimf(humidity_values, [0, 0, 50])
humidity_medium = trimf(humidity_values, [0, 50, 100])
humidity_high = trimf(humidity_values, [50, 100, 100])

fan_speed_low = trimf(fan_speed_values, [0, 0, 50])
fan_speed_medium = trimf(fan_speed_values, [0, 50, 100])
fan_speed_high = trimf(fan_speed_values, [50, 100, 100])

def fuzzy_rule(temperature, humidity):
    if temperature <= 50 or humidity <= 50:
        return 'low'
    elif 50 < temperature <= 100 and 50 < humidity <= 100:
        return 'medium'
    else:
        return 'high'

temperature = 75
humidity = 40
output_fan_speed = fuzzy_rule(temperature, humidity)
print('Fan speed:', output_fan_speed)

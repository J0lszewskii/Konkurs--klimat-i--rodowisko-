#!/usr/bin/python
#---------------------------------------------------------------------
#    ___  ___  ___  
#   / _ \/ _ \/ _ \ 
#  /  __/  __/  __/
# /____/\___/\___/
#
#           combined_sensors.py
# Read data from BH1750 light sensor and BMP280 temperature/pressure sensor
#
# Based on code by Matt Hawkins and Pimoroni
#---------------------------------------------------------------------
import time
from smbus2 import SMBus
from bmp280 import BMP280

# BH1750 constants
DEVICE     = 0x23 # Default device I2C address
POWER_DOWN = 0x00 # No active state
POWER_ON   = 0x01 # Power on
RESET      = 0x07 # Reset data register value

# Start measurement at 1lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_HIGH_RES_MODE_1 = 0x20

# Initialize I2C bus and BMP280
bus = SMBus(1)  # Rev 2 Pi uses 1
bmp280 = BMP280(i2c_dev=bus)

def convert_to_number(data):
    """Convert BH1750 data bytes to light level in lx"""
    result = (data[1] + (256 * data[0])) / 1.2
    return result

def read_light(addr=DEVICE):
    """Read light level from BH1750"""
    data = bus.read_i2c_block_data(addr, ONE_TIME_HIGH_RES_MODE_1)
    return convert_to_number(data)

def read_temperature():
    """Read temperature from BMP280"""
    return bmp280.get_temperature()

def read_pressure():
    """Read pressure from BMP280"""
    return bmp280.get_pressure()

def main():
    print("""Combined Sensors Reader
Reading from BH1750 (light) and BMP280 (temperature/pressure)
Press Ctrl+C to exit!
""")
    
    try:
        while True:
            # Read all sensor values
            light = read_light()
            temperature = read_temperature()
            pressure = read_pressure()
            
            # Print formatted output
            print(
                f"Light Level: {light:.2f} lx  |  "
                f"Temperature: {temperature:.2f}°C  |  "
                f"Pressure: {pressure:.2f}hPa"
            )
            
            # Wait before next reading
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nProgram stopped by user")
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        # Clean up
        bus.close()

if __name__ == "__main__":
    main()

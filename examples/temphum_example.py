#!/usr/bin/env python3
"""This example shows how to use the Temp&Hum Click wrapper of the LetMeCreate
library.

It reads the temperature from the sensor and exits.

The Temp&Hum Click must be inserted in Mikrobus 2 before running this program.


"""

from letmecreate.core import i2c
from letmecreate.core.common import MIKROBUS_2
from letmecreate.click import temphum


# Initialise I2C on Mikrobus 2
i2c.init()
i2c.select_bus(MIKROBUS_2)

# Read temperature
temphum.enable()
temp, hum = temphum.get_temperature()
print('{} degrees celsius'.format(temp))
print('{} % humidity'.format(hum))
temphum.disable()

# Release I2C
i2c.release()

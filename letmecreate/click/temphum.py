#!/usr/bin/env python3
"""Python binding of Temp&Hum Click wrapper of LetMeCreate library.

You must configure and select the right I2C bus before using any of these
functions.
"""
import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')


def enable():
    """Enable Temp&Hum Click.

    add_bit: A jumper is present on the Temp&Hum Click which modifies the I2C
    slave address of the chip. Set this variable to 0 or 1 according to the
    state of the jumper.

    Note: An exception is thrown if it fails to enable the Temp&Hum Click.
    """
    ret = _LIB.temphum_click_enable()
    if ret < 0:
        raise Exception("temphum click enable failed")


def get_temperature():
    """Returns temperature and Humidity measure.

    Note: An exception is thrown if it fails to read the temperature from the
    chip.
    """
    temperature = ctypes.c_float(0)
    humidity = ctypes.c_float(0)
    ret = _LIB.temphum_click_get_temperature(ctypes.byref(temperature), ctypes.byref(humidity))
    if ret < 0:
        raise Exception("temphum click get temperature failed")
    return temperature.value, humidity.value


def disable():
    """Disable Temp&Hum Click.

    Note: An exception is thrown if it fails to disable the chip.
    """
    ret = _LIB.temphum_click_disable()
    if ret < 0:
        raise Exception("temphum click disable failed")


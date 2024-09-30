"""
Conversion Functions
"""


def temperature_convert(temperature, unit):
    """
    Convert between F and C

    :param temperature:
    :param unit:
    :return:
    """
    if unit not in ["c", "f"]:
        raise ValueError("Unknown unit of temperature")

    if unit.lower() == "c":
        return (temperature - 32) * 5 / 9
    else:
        return temperature * 9 / 5 + 32

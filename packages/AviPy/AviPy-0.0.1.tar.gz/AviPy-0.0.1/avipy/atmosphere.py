from . import constants as const


def get_temp(height: float) -> float:
    """
    Returns the temperature at a height in meter [°K]
    """

    temp_at_height_k = const.Atm.SL.temp - const.Atm.lapse_rate * height

    return temp_at_height_k


def get_pressure(temp: float) -> float:
    """
    Returns the pressure at a given atmospheric temperature in Kelvin [Pa]
    """

    pressure_at_temp = const.Atm.SL.pressure * (temp / const.Atm.SL.temp) ** (
        const.Earth.gravity / (const.Atm.lapse_rate * const.Atm.r_air)
    )

    return pressure_at_temp


def get_density(height: float) -> float:
    """
    Returns the pressure at a given height in meter [kg / m^3]
    """

    temp_at_height = get_temp(height)
    pressure_at_height = get_pressure(temp_at_height)
    density_at_height = pressure_at_height / (const.Atm.r_air * temp_at_height)

    return density_at_height

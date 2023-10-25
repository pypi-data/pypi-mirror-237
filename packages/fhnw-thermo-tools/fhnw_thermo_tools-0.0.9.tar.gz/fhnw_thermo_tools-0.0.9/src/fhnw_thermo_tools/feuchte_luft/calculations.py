"""Berechnungen für feuchte Luft. Die Berechnungen sind entweder mit CoolProp umgesetzt 
oder aus dem Thermodynamik-Skript entnommen. Die Klasse FeuchteLuft verwendet diese
Funktionen, um die Zustandspunkte zu berechnen. Die Funktionen können aber auch
unabhängig von der Klasse verwendet werden.
"""


from CoolProp import CoolProp as CP
from fhnw_thermo_tools.data.globals import CW, CpL, CpW, hfg0


def get_p_sat(theta: float) -> float:
    """Berechnung des Sättigungsdrucks von Wasser bei gegebener Temperatur

    Args:
        theta (float): Temperatur [°C]

    Returns:
        p_sat (float): Sättigungsdruck [bar]"""

    p_sat = CP.PropsSI("P", "T", theta + 273.15, "Q", 1, "Water") / 1e5
    return p_sat


def get_x_sat(p: float, p_sat: float) -> float:
    """Berechnung der absoluten Luftfeuchte im gesättigten Zustand

    Args:
        p (float): Luftdruck [bar]
        p_sat (float): Sättigungsdruck [bar]

    Returns:
        x_sat (float): absolute Luftfeuchte [kg Wasser / kg trockene Luft]"""

    x_sat = 0.622 * p_sat / (p - p_sat)
    return x_sat


def get_h1x(theta: float, x: float, p: float):
    """Berechnung der Enthalpie von feuchter Luft bei gegebener Temperatur und
    relativer Luftfeuchte. In kJ/kg

    Args:
        theta (float): Temperatur [°C]
        x (float): absolute Luftfeuchte [kg Wasser / kg trockene Luft]
        p (float): Luftdruck [bar]

    Returns:
        h1x (float): Enthalpie feuchter Luft [kJ/kg]"""

    p_sat = get_p_sat(theta)
    x_sat = get_x_sat(p, p_sat)

    if x > x_sat:
        return CpL * theta + x_sat * (hfg0 + CpW * theta) + (x - x_sat) * CW * theta
    else:
        return CpL * theta + x * (hfg0 + CpW * theta)


def get_x(phi, p, p_sat):
    """Berechnung der absoluten Luftfeuchte in kg Wasser pro kg trockener Luft

    Args:
        phi (float): relative Luftfeuchte [-]
        p (float): Luftdruck [bar]
        p_sat (float): Sättigungsdruck [bar]

    Returns:
        x (float): absolute Luftfeuchte [kg Wasser / kg trockene Luft]"""

    x = 0.622 * phi * p_sat / (p - phi * p_sat)
    return x


def get_theta_dew(phi, p_sat, theta):
    """Berechnung der Taupunkttemperatur in °C

    Args:
        phi (float): relative Luftfeuchte [-]
        p_sat (float): Sättigungsdruck [bar]
        theta (float): Temperatur [°C]

    Returns:
        theta_dew (float): Taupunkttemperatur [°C]"""

    p_w = phi * p_sat * 1e5
    if p_w < 611.655:
        theta_dew = CP.HAProps("Tdp", "T", theta + 273.15, "P", 1e5, "R", phi) - 273.15
    else:
        theta_dew = CP.PropsSI("T", "P", p_w, "Q", 1, "Water") - 273.15

    return theta_dew


def get_theta_wet_bulb(theta: float, phi: float, p: float) -> float:
    """Berechnung der Nasskugeltemperatur in °C

    Args:
        theta_dry (float): Trockenkugeltemperatur [°C]
        phi (float): relative Luftfeuchte [-]
        p (float): Luftdruck [bar]

    Returns:
        theta_wet (float): Nasskugeltemperatur [°C]
    """
    # theta_wb = wet_bulb_temperature(
    #     p * units.bar, theta * units.degC, theta_dew * units.degC
    # ).magnitude
    return CP.HAPropsSI("Twb", "T", theta + 273.15, "P", p * 1e5, "R", phi) - 273.15


def get_phi(theta: float, p: float, x: float) -> float:
    """Berechnung der relativen Luftfeuchte [-] (0-1)

    Args:
        theta (float): Temperatur [°C]
        p (float): Luftdruck [bar]
        x (float): absolute Luftfeuchte [kg Wasser / kg trockene Luft]

    Returns:
        phi (float): relative Luftfeuchte [-] (0-1)
    """
    return CP.HAPropsSI("R", "T", theta + 273.15, "P", p * 1e5, "W", x)

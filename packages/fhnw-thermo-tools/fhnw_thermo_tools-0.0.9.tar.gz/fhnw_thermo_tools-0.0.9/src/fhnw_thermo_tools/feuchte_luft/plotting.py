import itertools
from typing import List

import CoolProp.CoolProp as CP
import matplotlib.pyplot as plt
import numpy as np
from fhnw_thermo_tools.feuchte_luft import FeuchteLuft
from fhnw_thermo_tools.data.globals import CW, CpL, CpW, hfg0


def get_psy_plot(
    state_points: List[FeuchteLuft],
    pressure: float = 1.01325,
    connect_points: bool = True,
):
    """
    Plotte die Zustandspunkte der feuchten Luft in einem h,x-Diagramm

    Args:
        state_points (List): Liste der Zustandspunkte der feuchten Luft
        pressure (float): Luftdruck für das Mollier-Diagramm [bar] Default: 1.01325
        connect_points (boolean): Verbinde die Zustandspunkte mit Pfeilen. Default: True
    Returns:
        (matplotlib.pyplot.figure): Plot der Zustandspunkte
    """

    if type(state_points) == FeuchteLuft:
        state_points = [state_points]

    if len(state_points) > 5:
        raise ValueError("Mehr als 5 Zustandspunkte sind nicht erlaubt")

    if type(state_points) != list:
        raise TypeError(
            "state_points muss entweder ein einzelner state_point, oder eine Liste sein"
        )

    marker = itertools.cycle(("o", "s", "v", "p", "*"))

    fig = get_mollier_diagram(pressure)
    ax = fig.gca()

    points = []

    for i, point in enumerate(state_points):
        point_y = point.h1x - 2500 * point.x
        ax.plot(point.x, point_y, marker=next(marker), label=point.name, markersize=7)

        points.append((point.x, point_y))

        if i > 0 and connect_points is True:
            ax.annotate(
                text="",
                xy=points[i - 1],
                xytext=points[i],
                arrowprops=dict(arrowstyle="->", color="black", linewidth=2),
            )

    fig.legend()

    return fig


def get_mollier_diagram(p: float = 1.01325):
    """Erstellt ein Mollier-h,x-Diagramm für feuchte Luft bei gegebenem Druck
    wenn p nicht angegeben wird, wird der Standarddruck von 1.01325 bar verwendet.

    Args:
        p (float, optional): Luftdruck [bar]. Defaults to 1.01325.

    Returns:
        fig: matplotlib figure object
    """
    x = np.linspace(0.001, 0.1, 200)
    phi = np.linspace(0.1, 1, 10)
    theta_isenthalp = np.linspace(0.0, 350.0, 36)
    theta = np.linspace(0.0, 200.0, 41)
    # Nehmen den minimale Wert für die Isotherme als fcn von x
    isotherm_plot = np.minimum(get_isotherm(theta, x), get_isotherm_sat(theta, x, p))

    fig = plt.figure()

    plt.plot(x, get_isenthalp(theta_isenthalp, x), "g--")
    plt.plot(x, get_isofeucht(phi, x, p), "b--")
    plt.plot(x, isotherm_plot, "r")

    plt.ylim(0, 100)
    plt.xlim(0.001, 0.1)
    plt.title(f"Mollier-h,x-Diagramm bei p = {p} bar")
    plt.xlabel("absolute Feuchtigkeit [kg Wasser/kg tr. Luft]")
    plt.ylabel("h$_{1+x}$ [kJ/kg]")
    plt.ion()

    return fig


def get_isenthalp(theta: np.ndarray, x: np.ndarray) -> List[float]:
    """Berechnet für jede abs. Luftfeuche x die y-Werte bei den Temperaturen theta,
    die für eine Isenthalpe benötigt werden.

    Args:
        theta (np.ndarray): Shape (n,1) Temperatur [°C]
        x (np.ndarray): Shape (n,1) absolute Luftfeuchte [kg Wasser / kg trockene Luft]

    Returns:
        List: Y-Werte für Isenthalpe
    """
    return [CpL * theta - hfg0 * x_i for x_i in x]


def get_isotherm(theta: float, x: float) -> List[float]:
    """Berechnet für jede abs. Luftfeuche x die y-Werte bei den Temperaturen theta,
    die für eine Isotherme benötigt werden.

    Args:
        theta (np.ndarray): Shape (n,1) Temperatur [°C]
        x (np.ndarray): Shape (n,1) absolute Luftfeuchte [kg Wasser / kg trockene Luft]

    Returns:
        List: Y-Werte für Isotherme
    """
    return [CpL * theta + x_i * (hfg0 + CpW * theta) - hfg0 * x_i for x_i in x]


def get_isotherm_sat(theta: np.ndarray, x: np.ndarray, p: float) -> List[float]:
    """Berechnet für jede abs. Luftfeuche x die y-Werte bei den Temperaturen theta,
    die für eine Isotherme im gesättigten Zustand benötigt werden.

    Args:
        theta (np.ndarray): Shape (n,1) Temperatur [°C]
        x (np.ndarray): Shape (n,1) absolute Luftfeuchte [kg Wasser / kg trockene Luft]
        p (float): Luftdruck [bar]

    Returns:
        List: Y-Werte für Isotherme im gesättigten Zustand
    """
    p_sat = CP.PropsSI("P", "T", theta + 273.15, "Q", 1, "water") / 1e5
    x_sat = 0.622 * p_sat / (p - p_sat)

    return [
        CpL * theta
        + x_sat * (hfg0 + CpW * theta)
        + (x_i - x_sat) * CW * theta
        - hfg0 * x_i
        for x_i in x
    ]


def get_isofeucht(phi: np.ndarray, x: np.ndarray, p: float) -> List[float]:
    """Berechnet für jede abs. Luftfeuche x die y-Werte bei den relativen Luftfeuchten phi,
    die für eine Isofeuchte benötigt werden.

    Args:
        phi (np.ndarray): Shape (n,1) relative Luftfeuchte [-] (0-1)
        x (np.ndarray): Shape (n,1) absolute Luftfeuchte [kg Wasser / kg trockene Luft]
        p (float): Luftdruck [bar]

    Returns:
        List: Y-Werte für Isofeuchte
    """
    isofeucht_list = []
    for x_i in x:
        p_sat = x_i * p / (phi * (0.622 + x_i))
        theta = CP.PropsSI("T", "P", p_sat * 1e5, "Q", 1, "water") - 273.15  # in °C
        isofeucht_list.append(CpL * theta + x_i * (hfg0 + CpW * theta) - hfg0 * x_i)

    return isofeucht_list

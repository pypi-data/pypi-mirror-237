import numpy as np
from fhnw_thermo_tools.feuchte_luft.calculations import (
    get_h1x,
    get_p_sat,
    get_phi,
    get_theta_dew,
    get_theta_wet_bulb,
    get_x,
    get_x_sat,
)


class FeuchteLuft:
    """Klasse für die Abbildung eines Zustandpunkts von feuchter Luft.

    Attributes:
    ----------
    theta : float
        Temperatur [°C]
    phi : float
        relative Luftfeuchte [-] (0-1)
    p : float
        Luftdruck [bar]
    x : float
        absolute Luftfeuchte [kg Wasser / kg trockene Luft]
    h1x : float
        Enthalpie feuchter Luft [kJ/kg]
    theta_dew : float
        Taupunkttemperatur [°C]
    theta_wet_bulb : float
        Nasskugeltemperatur [°C]
    name : str
        Name des Objekts.

    Methods:
    ----------
    from_x(cls, theta: float, p: float, x: float, name: str = None) -> "FeuchteLuft":
        Initialisierung der Klasse FeuchteLuft über die absolute Luftfeuchte x.
        Kann verwendet werden, um Punkte im Nebelbereich zu initialisieren.
    """

    def __init__(
        self,
        theta: float,
        p: float,
        x: float = None,
        phi: float = None,
        name: str = None,
    ):
        """
        Initialisierung der Klasse FeuchteLuft über die relative Luftfeuchte phi.
        Um Punkte im Nebelbereich zu initialisieren, kann die absolute Luftfeuchte x
        an die Methode from_x übergeben werden. (siehe from_x)

        Args:
        ----------
        theta (float): Temperatur [°C]
        p (float): Luftdruck [bar]
        phi (float) :  relative Luftfeuchte [-] (0-1)
        name (str, optional): Name des Objekts.
        """

        if x is None and phi is None:
            raise ValueError("Either x or phi need to be passed to the constructor")

        self.theta = theta
        self.phi = phi
        self.p = p
        self.T = self.theta + 273.15  # [K] Temperatur

        self.name = name if name is not None else f"FL_{theta}°C_{phi*100}%_{p}bar"

        self.p_sat = get_p_sat(self.theta)  # [bar] Sättigungsdruck
        self.x_sat = get_x_sat(self.p, self.p_sat)

        self.x = (
            x if x is not None else get_x(self.phi, self.p, self.p_sat)
        )  # [kg Wasser / kg trockene Luft] absolute Luftfeuchte

        self.h1x = get_h1x(
            self.theta, self.x, self.p
        )  # [kJ/kg] Enthalpie feuchter Luft

        self.theta_dew = get_theta_dew(
            self.phi,
            self.p_sat,
            self.theta,
        )  # [°C] Taupunkttemperatur

        self.theta_wet_bulb = get_theta_wet_bulb(
            self.theta, self.phi, self.p
        )  # [°C] Nasskugeltemperatur

    def __str__(self):
        return f"""{self.name}: {self.theta} °C, {self.phi*100} %, {self.p} bar, 
        x: {np.round(self.x, 4)} kg Wasser/kg trockene Luft, 
        h1x: {np.round(self.h1x, 2)} kJ/kg, 
        theta_dew: {np.round(self.theta_dew, 2)} °C, 
        theta_wet_bulb: {np.round(self.theta_wet_bulb, 2)} °C"""

    def __repr__(self):
        class_name = type(self).__name__
        return (
            f"{class_name}(theta={self.theta}, phi={self.phi}, p={self.p}, x={self.x})"
        )

    @classmethod
    def from_x(
        cls, theta: float, p: float, x: float, name: str = None
    ) -> "FeuchteLuft":
        """Initialisierung der Klasse FeuchteLuft über die absolute Luftfeuchte x.
        Kann verwendet werden, um Punkte im Nebelbereich zu initialisieren.

        Args:
            theta (float): Temperatur [°C]
            p (float): Luftdruck [bar]
            x (float): absolute Luftfeuche [kg/kg tr. Luft]
            name (str, optional): Name des Objekts.

        Returns:
            FeuchteLuft: Objekt der Klasse FeuchteLuft
        """
        phi = get_phi(p, theta, x)
        return cls(theta=theta, p=p, x=x, phi=phi, name=name)

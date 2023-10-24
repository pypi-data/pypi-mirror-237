import math
from typing import Literal

from . import constants as const
from . import qty


class Coord:
    def __init__(self, latitude: float, longitude: float, unit: Literal["deg", "rad"] = "deg"):
        if unit.lower() == "deg":
            self.lat = latitude
            self.lon = longitude
        elif unit.lower() == "rad":
            self.lat = math.degrees(latitude)
            self.lon = math.degrees(longitude)
        else:
            raise ValueError("Invalid unit. Unit must be degrees (deg) or radians (rad)")

    def degrees(self):
        return self.lat, self.lon

    def radians(self):
        return math.radians(self.lat), math.radians(self.lon)

    def is_nearby(self, coordinate: "Coord"):
        """
        Returns whether the coordinate instance is nearby the given other coordinate
        """

        if (coordinate.lat - 0.5 < self.lat < coordinate.lat + 0.5) and (
            coordinate.lon - 0.5 < self.lon < coordinate.lon + 0.5
        ):
            return True
        return False

    def __str__(self):
        return f"lat: {self.lat}°, lon: {self.lon}°"


def distance_between_points(point1: Coord, point2: Coord) -> float:
    """
    Return meters of distance between point 1 and point 2

    source: https://www.movable-type.co.uk/scripts/latlong.html
    """

    lat1, lon1 = point1.radians()
    lat2, lon2 = point2.radians()

    delta_lon = lon2 - lon1

    distance = (
        math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(delta_lon))
        * const.Earth.radius
    )

    return distance


def bearing_between_points(point1: Coord, point2: Coord) -> float:
    """
    Returns the inital bearing between point 1 and point 2

    source: https://www.movable-type.co.uk/scripts/latlong.html
    """
    lat1, lon1 = point1.radians()
    lat2, lon2 = point2.radians()

    y = math.sin(lon2 - lon1) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(lon2 - lon1)

    bearing_rad = math.atan2(y, x)
    bearing_deg = (math.degrees(bearing_rad) + 360) % 360

    return bearing_deg


def coord_of_next_point(point1: Coord, dist: qty.Distance, bearing_deg: float) -> Coord:
    """
    Returns the coordinate of a next point, given a first point and a bearing and distance to the next point

    source: https://www.movable-type.co.uk/scripts/latlong.html
    """

    lat1, lon1 = point1.radians()
    bearing = math.radians(bearing_deg)
    angular_dist = dist / const.Earth.radius

    lat2 = math.asin(
        math.sin(lat1) * math.cos(angular_dist) + math.cos(lat1) * math.sin(angular_dist) * math.cos(bearing)
    )

    lon2 = lon1 + math.atan2(
        math.sin(bearing) * math.sin(angular_dist) * math.cos(lat1),
        math.cos(angular_dist) - math.sin(lat1) * math.sin(lat2),
    )

    return Coord(lat2, lon2, unit="rad")


if __name__ == "__main__":
    print("Running geo.py")

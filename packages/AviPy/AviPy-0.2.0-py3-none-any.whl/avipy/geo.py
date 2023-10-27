import math
from typing import Literal

from . import constants as const
from . import qty


class Coord:
    __lat = None
    __lon = None

    def __init__(self, lat: float, lon: float, unit: Literal["deg", "rad"] = "deg"):
        self.set_lat(lat, unit)
        self.set_lon(lon, unit)

    def __repr__(self):
        return f"lat: {self.__lat}, lon: {self.__lon}"

    def __str__(self):
        return f"Latitude: {self.__lat:.2f}°, Longitude: {self.__lon:.2f}°"

    def set_lat(self, lat: float, unit: Literal["deg", "rad"] = "deg") -> "Coord":
        """
        Sets the latitude of the coordinate
        """
        if unit.lower() not in ["deg", "rad"]:
            raise TypeError("Unit not of supported type")

        if unit.lower() == "rad":
            lat = math.degrees(lat)

        if not (-90 <= lat <= 90):
            raise ValueError("Latitude must be in range [-90, 90]")

        self.__lat = lat

        return self

    def set_lon(self, lon: float, unit: Literal["deg", "rad"] = "deg") -> "Coord":
        """
        Sets the longitude of the coordinate
        """
        if unit.lower() not in ["deg", "rad"]:
            raise TypeError("Unit not of supported type")

        if unit.lower() == "rad":
            lon = math.degrees(lon)

        if not (-180 <= lon <= 180):
            raise ValueError("Longitude must be in range [-180, 180]")

        self.__lon = lon

        return self

    def get_lat(self, unit: Literal["deg", "rad"] = "deg") -> float:
        """
        Returns the latitude of the coordinate
        """
        if unit.lower() not in ["deg", "rad"]:
            raise TypeError("Unit not of supported type")

        if unit == "rad":
            return math.radians(self.__lat)

        return self.__lat

    def get_lon(self, unit: Literal["deg", "rad"] = "deg") -> float:
        """
        Returns the longitude of the coordinate
        """
        if unit.lower() not in ["deg", "rad"]:
            raise TypeError("Unit not of supported type")

        if unit == "rad":
            return math.radians(self.__lon)

        return self.__lon

    def get_latlon(self, unit: Literal["deg", "rad"] = "deg") -> tuple[float, float]:
        """
        Returns a tuple of the latitude and longitude of the coordinate (lat, lon)
        """
        if unit.lower() not in ["deg", "rad"]:
            raise TypeError("Unit not of supported type")

        if unit == "rad":
            return (math.radians(self.__lat), math.radians(self.__lon))

        return (self.__lat, self.__lon)

    def is_nearby(self, coord: "Coord") -> bool:
        """
        Returns whether the coordinate is nearby the given other coordinate
        """
        lat, lon = coord.get_latlon()

        if (lat - 0.5 < self.__lat < lat + 0.5) and (lon - 0.5 < self.__lon < lon + 0.5):
            return True
        return False

    def get_distance(self, coord: "Coord") -> qty.Distance:
        """
        Return meters of distance between point 1 and point 2

        source: https://www.movable-type.co.uk/scripts/latlong.html
        """
        lat1, lon1 = self.get_latlon("rad")
        lat2, lon2 = coord.get_latlon("rad")

        delta_lon = lon2 - lon1

        distance = (
            math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(delta_lon))
            * const.Earth.radius
        )

        return qty.Distance(distance)

    def get_bearing(self, coord: "Coord") -> qty.Distance:
        """
        Returns the inital bearing between point 1 and point 2

        source: https://www.movable-type.co.uk/scripts/latlong.html
        """
        lat1, lon1 = self.get_latlon("rad")
        lat2, lon2 = coord.get_latlon("rad")

        y = math.sin(lon2 - lon1) * math.cos(lat2)
        x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(lon2 - lon1)

        bearing_rad = math.atan2(y, x)
        bearing_deg = (math.degrees(bearing_rad) + 360) % 360

        return bearing_deg

    def get_next_coord(self, dist: qty.Distance, bearing_deg: float) -> "Coord":
        """
        Returns the coordinate of a next point, given a first point and a bearing and distance to the next point

        source: https://www.movable-type.co.uk/scripts/latlong.html
        """

        lat1, lon1 = self.get_latlon("rad")
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

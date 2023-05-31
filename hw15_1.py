def convert_miles_to_km(miles: int | float) -> int | float:
    if miles < 0:
        raise ValueError

    km = miles * 1.6
    return km

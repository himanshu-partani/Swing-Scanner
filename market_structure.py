def find_swing_points(data, window):
    swing_lows = []
    swing_highs = []
    for i in range(window, len(data) - window):
        current_low = float(data["Low"].iloc[i])
        if (
            current_low < data["Low"].iloc[i-1]
            and current_low < data["Low"].iloc[i-2]
            and current_low < data["Low"].iloc[i+1]
            and current_low < data["Low"].iloc[i+2]
        ):
            swing_lows.append({"index": i, "price": current_low})
        current_high = float(data["High"].iloc[i])
        if (
            current_high > data["High"].iloc[i-1]
            and current_high > data["High"].iloc[i-2]
            and current_high > data["High"].iloc[i+1]
            and current_high > data["High"].iloc[i+2]
        ):
            swing_highs.append({"index": i, "price": current_high})
    return swing_lows, swing_highs


def group_swing_points(swing_points, threshold_percent=1):
    zones = []

    for swing in swing_points:
        # Create first zone
        if not zones:
            zones.append({
                "zone_low": swing["price"],
                "zone_high": swing["price"],
                "average_price": swing["price"],
                "touches": 1,
                "swing_points": [swing]
            })
            continue

        zone_found = False

        # Check every existing zone
        for zone in zones:

            distance_low = (
                abs(swing["price"] - zone["zone_low"])
                / zone["zone_low"]
            ) * 100

            distance_high = (
                abs(swing["price"] - zone["zone_high"])
                / zone["zone_high"]
            ) * 100

            if (
                distance_low <= threshold_percent
                or distance_high <= threshold_percent
            ):

                zone["swing_points"].append(swing)
                zone["touches"] += 1

                prices = [
                    point["price"]
                    for point in zone["swing_points"]
                ]

                zone["zone_low"] = min(prices)
                zone["zone_high"] = max(prices)
                zone["average_price"] = (
                    sum(prices) / len(prices)
                )

                zone_found = True
                break

        if not zone_found:
            zones.append({
                "zone_low": swing["price"],
                "zone_high": swing["price"],
                "average_price": swing["price"],
                "touches": 1,
                "swing_points": [swing]
            })

    for zone in zones:
        if zone["touches"] >= 3:
            zone["strength"] = "Strong"
        elif zone["touches"] == 2:
            zone["strength"] = "Medium"
        else:
            zone["strength"] = "Weak"

    return zones

def filter_zones(zones, minimum_touches):
    """
    Filters support/resistance zones based on minimum number of touches.
    Parameters:
        zones (list): List of zone dictionaries.
        minimum_touches (int): Minimum touches required to keep a zone.
    Returns:
        list: Filtered list of zones.
    """
    filtered_zones = []
    for zone in zones:
        if zone["touches"] >= minimum_touches:
            filtered_zones.append(zone)
    return filtered_zones

def find_nearest_zones(support_zones,resistance_zones,current_price):
    nearest_support = None
    nearest_resistance = None
    for zone in support_zones:
        if zone["average_price"] < current_price:
            if (
                nearest_support is None
                or
                zone["average_price"] > nearest_support["average_price"]
            ):
                nearest_support = zone
    for zone in resistance_zones:
        if zone["average_price"] > current_price:
            if (
                nearest_resistance is None
                or
                zone["average_price"] < nearest_resistance["average_price"]
            ):
                nearest_resistance = zone
    return nearest_support, nearest_resistance

def calculate_zone_distance(nearest_support,nearest_resistance,current_price,):
    support_distance = None
    resistance_distance = None

    if nearest_support is not None:
        support_distance = (
            (current_price - nearest_support["average_price"])
            / current_price
        ) * 100
    if nearest_resistance is not None:
        resistance_distance = (
            (nearest_resistance["average_price"] - current_price)
            / current_price
        ) * 100

    return (
        round(support_distance, 2) if support_distance is not None else None,
        round(resistance_distance, 2) if resistance_distance is not None else None,
    )

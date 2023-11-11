def convert(feet, inch):
    feet_to_meter = float(feet * 0.3048)
    inch_to_meter = float(inch * 0.0254)
    meters_result = feet_to_meter + inch_to_meter
    return meters_result
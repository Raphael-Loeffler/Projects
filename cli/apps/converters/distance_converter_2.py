from argparse import ArgumentParser
MIL_TO_KM: float = 1.60934
parser = ArgumentParser(description="Distance Converter - Options")
parser.add_argument('--distance_in_miles', type=float, help="Distance in miles")

arguments = parser.parse_args()
distance_mil = arguments.distance_in_miles
distance_km = distance_mil * MIL_TO_KM
print(f"{distance_mil:.02f} mil = {distance_km:.02f} km")
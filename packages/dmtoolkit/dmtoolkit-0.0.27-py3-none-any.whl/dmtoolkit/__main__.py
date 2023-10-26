import argparse
from dmtools import generator


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument(
    "-r",
    "--regions",
    help="How many regions would you like to generate?",
    type=int,
    default=1,
)
arg_parser.add_argument(
    "-f",
    "--factions",
    help="How many factions would you like to generate for each region?",
    type=int,
    default=1,
)
arg_parser.add_argument(
    "-l",
    "--locations",
    help="How many POIs would you like to generate for each region?",
    type=int,
    default=1,
)
arg_parser.add_argument(
    "-c",
    "--cities",
    help="How many cities would you like to generate for each region?",
    type=int,
    default=1,
)
args = arg_parser.parse_args()
generator(args.regions, args.factions, args.locations, args.cities)

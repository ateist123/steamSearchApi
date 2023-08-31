import requests, argparse

arg_parser = argparse.ArgumentParser("Steam search API")

arg_parser.add_argument('-p', '--start-price')
arg_parser.add_argument('-P', '--end-price')

arg_parser.add_argument('--start-page')
arg_parser.add_argument('--end-page')

arg_parser.add_argument('-t', '--item-type')


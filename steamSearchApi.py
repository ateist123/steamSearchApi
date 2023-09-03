from pprint import pprint
from bs4 import BeautifulSoup
from urllib.parse import quote
import requests, argparse

def prepare_args():
    arg_parser = argparse.ArgumentParser("Steam search API")

    arg_parser.add_argument('-p', '--start-price')
    arg_parser.add_argument('-P', '--end-price')

    arg_parser.add_argument('--start-page')
    arg_parser.add_argument('--end-page')

    arg_parser.add_argument('-t', '--item-type')
    arg_parser.add_argument('-f', '--output-format')
    arg_parser.add_argument('-s', '--search-sort', required=True)

    
    return arg_parser.parse_args()

def control_args(args):
    if not args.search_sort in ['price_desc', 'price_asc', 'quantity_desc', 'quantity_desc', 'name_asc', 'name_desc']:
        raise RuntimeError('typed bad sort type.\nAvalible types is:\n[\'price_desc\', \'price_asc\', \'quantity_desc\', \'quantity_desc\', \'name_asc\', \'name_desc\']')

    if not args.output_format in ['json', 'yaml', None]:
        raise RuntimeError('typed bad output format.\nAvalible formats is:\n[\'json\', \'yaml\'] or don\'t use this arg')

#aria-invalid="false", autocomplete="off", class_="Textinput-Control"

def main(args): 
    res = []
    for x in range(int(args.start_page), int(args.end_page)+1):
        get_str = 'https://steamcommunity.com/market/search?appid=440#p%s_%s' % (x, args.search_sort)
        get_res = requests.get(get_str)

        if get_res.status_code != 200:
            pprint('Headers:\n'+str(get_res.headers))
            raise RuntimeError('Bad request status, avalible status: 200, get status: ' + str(get_res.status_code))

        get_res = BeautifulSoup(get_res.text, 'html5lib')
        
        for y in range(0, 10):
            
            predata = {}
            frame = get_res.find(id='resultlink_%s' % y)
            predata['name'] = frame.find(id='result_%s_name' % y)

            predata['count'] = frame.find(class_="market_listing_num_listings_qty").text
            predata['price'] = frame.find(class_='normal_price').text
            predata['price'] = predata['price'][predata['price'].find('$')+1:predata['price'].find('U')]
            predata['price'] = float(predata['price'])*96.0
            print(predata['count'])
            


args = prepare_args()
control_args(args)
main(args)



from logging import raiseExceptions
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



def main(args): 
    res = []
    for x in range(int(args.start_page), int(args.end_page)+1):
        get_str = 'steamcommunity.com/market/search?appid=440#p%s_%s' % (x, args.search_sort)
        get_res = requests.get(get_str)
        
        if get_res.status_code != 200:
            raise RuntimeError('Bad request status, avalible status: 200, get status: ' + str(get_res.status_code))

        get_res = get_res.text
        print(get_res)


args = prepare_args()
control_args(args)
main(args)
print(args)


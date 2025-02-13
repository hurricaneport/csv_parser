import argparse
import pandas as pd
import sys


def main():
    args = get_args()
    try:
        csv_file = pd.read_csv(args.csv_file, usecols=args.column)
    except FileNotFoundError:
        print(f'File \'{args.csv_file}\' does not exist.', file=sys.stderr)
        return
    
    print(csv_file.to_csv(index=False))
    

def get_args():
    parser = argparse.ArgumentParser(
        prog='csv_parser.py',
        description='Process CSV file.'

    )
    parser.add_argument('csv_file', help='file path or URL to CSV file to be parsed')
    parser.add_argument('-c', '--column', help='columns to select from CSV file',
                        nargs='*', metavar='COLUMN')
    parser.add_argument('-v', '--verbose', help='print logging messages',
                        action='store_true')
    
    return parser.parse_args()

if __name__ == '__main__':
    main()

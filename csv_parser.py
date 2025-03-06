import argparse
import pandas as pd
import sys
import unittest

def main():
    args = get_args()
    print_cols(args.csv_file, args.column) 
    

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

def print_cols(csv, cols):
    try:
        csv_file = pd.read_csv(csv, usecols=cols)
    except FileNotFoundError:
        print(f'File \'{args.csv_file}\' does not exist.', file=sys.stderr)
        return
    except ValueError:
        print(f'column could not be found')
        return

    print(csv_file.to_csv(index=False))

if __name__ == '__main__':
    main()

class TestCsv(unittest.TestCase):
    def test_good_csv(self):
        self.assertEqual(1,1)

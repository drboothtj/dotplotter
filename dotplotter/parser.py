'''
Parser for dotplotter.
    Functions:
        xxxxx
'''
import argparse
import sys
from argparse import RawTextHelpFormatter

def get_parser():
    '''
    gets argument parser
        arguments:
            None
        returns:
            argument_parser
    '''
    parser = argparse.ArgumentParser(
        prog='dotplotter',
        description=
            '''
            Creates a dotplot from blast results from a .tsv or stdin.
                EXAMPLE USAGE 1:'
                    dotplotter -i my_results.tsv'
                EXAMPLE USAGE 2:'
                    blastn -query seq1.fna -subject seq2.fna -outfmt 6 | dotplotter'
            ''',
        epilog='Written by Dr. T. J. Booth, 2023',
        formatter_class=RawTextHelpFormatter
    )
    parser.add_argument(
        '-i',
        '--input',
        type=argparse.FileType('r'),
        default=sys.stdin,
        help = (
            '.tsv containing blast results in outfmt 6'
        )
    )
    parser.add_argument(
        '-o',
        '--output',
        type=str,
        default='output.png',
        help = (
            'path to .png for the outputfile'
        )
    )
    parser.add_argument(
        '-e',
        '--e-value',
        type=float,
        default=0,
        help = (
            'cutoff for the e-value'
        )
    )
    parser.add_argument(
        '-s',
        '--size',
        type=int,
        default=1000,
        help = (
            'cuttoff value for the size'
        )
    )
    parser.add_argument(
        '-c',
        '--colour',
        type=str,
        default='black',
        help = (
            'string indiciating the default line colour'
        )
    )
    parser.add_argument(
        '-hs',
        '--highlight-start',
        type=int,
        default=-2,
        help = (
            'start location of region to highlight'
        )
    )
    parser.add_argument(
        '-he',
        '--highlight-end',
        type=int,
        default=-1,
        help = (
            'end location of region to highlight'
        )
    )
    parser.add_argument(
        '-hc',
        '--highlight-colour',
        type=str,
        default='red',
        help = (
            'string indiciating the highlight colour'
        )
    )
    parser.add_argument(
        '-hf',
        '--highlight-file',
        type=argparse.FileType('r'),
        default=None,
        help = (
            'path to .csv file for multiple highlights'
        )
    )
    return parser

def get_args():
    '''
    gets the arguments from the parser
        arguments:
            None
        returns:
            args: arguments object
    '''
    parser = get_parser()
    args = parser.parse_args()
    return args

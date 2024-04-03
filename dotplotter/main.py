'''
DOCSTRING
    FUCNTIONS:
'''
from sys import stdin
from typing import List
import matplotlib.pyplot as plt

from dotplotter import check_input, io, parser

def get_line_info(line: str) -> dict:
    '''
    takes a line of blast output (outfmt 6) and returns important values
        arguments:
            line: a single tab-seperated line of blast output
        returns:
            line_dict
    '''
    line_dict = {}
    split_line = line.split('\t')
    line_dict['qstart'] = int(split_line[6])
    line_dict['qend'] = int(split_line[7])
    line_dict['qsize'] = abs(line_dict['qstart'] - line_dict['qend'])
    line_dict['sstart'] = int(split_line[8])
    line_dict['send'] = int(split_line[9])
    line_dict['ssize'] = abs(line_dict['sstart'] - line_dict['send'])
    line_dict['min_size'] = min(line_dict['qsize'], line_dict['ssize'])
    line_dict['e_value'] = float(split_line[10])
    return line_dict

def is_between(list1, lower, upper):
    '''
    takes a list of values and works out if any of them are within specific boundaries
    '''
    is_between_flag = False
    for number in list1:
        if int(lower) < number < int(upper):
            is_between_flag = True
            print(lower, number, upper, '!')
    return is_between_flag

def plot_dotplot(query_values, subject_values, color):
    '''
    plots and writes a dotplot .png from provided x and y values
    '''
    for x_value, y_value in zip(query_values, subject_values):
        plt.plot(x_value, y_value, color = color)

def main():
    '''
    main routine for dotplotter
        arguments: None
        returns: None
    '''
    #get arguments
    args = parser.get_args()
    input_lines = [line.strip() for line in args.input.readlines()]
    eval_cutoff = args.e_value
    size_cutoff = args.size
    highlight_start = args.highlight_start
    highlight_end = args.highlight_end
    color = args.colour
    outfile = args.output
    highlight_color = args.highlight_colour
    bin_file = args.highlight_file
    
    #check input
    check_input.check_format(input_lines)
    
    #initialise lists
    query_values = []
    subject_values = []
    line_dicts = []

    if bin_file is None:
        bins = [[highlight_start, highlight_end, highlight_color]]
    else:
        bins = [line.strip().split(',') for line in bin_file.readlines()]
    
    ###temp 
    for line in input_lines:
        line_dict = get_line_info(line)
        if line_dict['e_value'] > eval_cutoff or line_dict['min_size'] < size_cutoff:
            continue
        query_values.append((line_dict['qstart'], line_dict['qend']))
        subject_values.append((line_dict['sstart'], line_dict['send']))
        line_dicts.append(line_dict)

    #plot
    plt.figure(figsize=(3.7,3.7))
    plot_dotplot(query_values, subject_values, color)
    for _bin in bins:
        bin_data = []
        query_values = []
        subject_values = []
        for line_dict in line_dicts:
            qstart = line_dict['qstart']
            qend = line_dict['qend']
            #if region runs over the bin use min values
            if is_between([qstart, qend], _bin[0], _bin[1]):
                query_values.append((qstart, qend))
                subject_values.append((line_dict['sstart'], line_dict['send'])) #add in half lines 
        plot_dotplot(query_values, subject_values, _bin[2].strip())

    # Add labels and title
    plt.xlabel('query') # get
    plt.ylabel('subject') # get
    
    # Display the plot
    plt.grid(True)
    plt.savefig(outfile)

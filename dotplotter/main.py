'''
DOCSTRING
    Functions: 
        get_line_info(line: str) -> dict
        plot_dotplot(x_values: List[Tuple], y_values: List[Tuple], colour: str) -> None
        main()

'''
from typing import List, Tuple
import matplotlib.pyplot as plt

from dotplotter import check_input, parser, chunks

def get_line_info(line: str) -> dict:
    '''
    takes a line of blast output (outfmt 6) and returns important values
        arguments:
            line: a single tab-seperated line of blast output
        returns:
            line_dict: dictionary containing the information about the line
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


def plot_dotplot(x_values: List[Tuple], y_values: List[Tuple], colour: str) -> None:
    '''
    adds plot to existing plot based on x and y values and a colour
        arguments:
            x_values:list of paired x-values 
            y_values: list of paired y-values
            colour: string or hexcode to colour plotted values
        returns:
            None
    '''
    for x_value, y_value in zip(x_values, y_values):
        plt.plot(x_value, y_value, color = colour)

def main():
    '''
    main routine for dotplotter
        arguments: None
        returns: None
    '''
    #get arguments
    print('Running dotplotter...')
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
        lower_boundary = min(int(_bin[0]), int(_bin[1]))
        upper_boundary = max(int(_bin[0]), int(_bin[1]))
        new_query_values, new_subject_values = chunks.get_chunks(
            query_values, subject_values, lower_boundary, upper_boundary
            )
        if len(new_query_values) == 0:
            print('WRARNING: Following highlight had no hits:', _bin)
        #print('plotting', new_query_values, new_subject_values, _bin[2].strip())
        plot_dotplot(new_query_values, new_subject_values, _bin[2].strip())

    # Add labels and title
    plt.xlabel('query') # get
    plt.ylabel('subject') # get

    # Display the plot
    plt.grid(True)
    plt.savefig(outfile)
    print('Done!')

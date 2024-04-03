'''
DOCSTRING
'''
from typing import List

def check_format(lines: List) -> None: ### make a seperate script with error classes
    '''
    raise and error if input is not as expected
        arguments:
            line: line to be checked
        returns:
            None
    '''
    #check 1: check the input is tab-seperated and of the expected size
    line = lines[0]
    line = line.split('\t')
    line_length = len(line)
    if line_length != 12:
        raise Exception(f'Line lenght is {line_length}. Check the file is tab seperated and in outfmt 6.')
    #check 2: check all the query and subjects have the same name 
    #to avoid people inputing multiple searches and getting nonesense
    
    ###MAKE FUCNTION"###
    qnames = [line.split('\t')[0] for line in lines]
    len_qnames = len(set(qnames))
    if  len_qnames != 1:
        raise Exception(f'There are {len_qnames} different query names. Query names should be identical.')
    snames = [line.split('\t')[1] for line in lines]
    len_snames = len(set(snames))
    if  len_snames != 1:
        raise Exception(f'There are {len_snames} different subject names. Query names should be identical.')
    ###MAKE FUCNTION"###
    #add any other checks here

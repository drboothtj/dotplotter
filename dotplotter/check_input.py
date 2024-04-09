'''
checks for dotplotter input
'''
from typing import List

class DotplotterError(Exception):
    '''
    custom error for dottplotter specific errors
    '''

class InputLengthError(DotplotterError):
    '''
    Error for incorrect number of input fields
    '''

class InputNameError(DotplotterError):
    '''
    Error called when there is a problem with input names
    '''

def check_query_and_subject_names(lines: List[str]) -> None:
    '''
    checks that the query and subject names are consistent
        arguments:
            lines: list of lines from the input file
        returns:
            None

    '''
    qnames = [line.split('\t')[0] for line in lines]
    len_qnames = len(set(qnames))
    if  len_qnames != 1:
        raise InputNameError(
            f'There are {len_qnames} different query names. Query names should be identical.'
            )
    snames = [line.split('\t')[1] for line in lines]
    len_snames = len(set(snames))
    if  len_snames != 1:
        raise InputNameError(
            f'There are {len_snames} different subject names. Query names should be identical.'
            )

def check_field_number(line: str) -> None:
    '''
    checks that there are 12 fields as expected from -outfmt 6
        arguments:
            line: a line from the input file
        returns:
            None
    '''
    line = line.split('\t')
    line_length = len(line)
    if line_length != 12:
        raise InputLengthError(
            f'Line lenght is {line_length}. Check the file is tab seperated and in outfmt 6.'
            )

def check_format(lines: List[str]) -> None: ### make a seperate script with error classes
    '''
    raise and error if input is not as expected
        arguments:
            line: line to be checked
        returns:
            None
    '''
    #check 1: check the input is tab-seperated and of the expected
    check_field_number(lines[0])
    #check 2: check all the query and subjects have the same name
    #to avoid people inputing multiple searches and getting nonesense
    check_query_and_subject_names(lines)
    #add any other checks here

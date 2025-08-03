import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your reverse_complement function here, along with any subroutines you need
def reverse_complement(pattern: str) -> str:
    """Calculate the reverse complement of a DNA pattern."""
    return_str = ""
    for nucleotide in pattern:
        complement = ''
        if nucleotide == 'A':
            complement = 'T'
        elif nucleotide == 'T':
            complement = 'A'
        elif nucleotide == 'G':
            complement = 'C'
        else:
            complement = 'G'
        return_str = complement + return_str
    return return_str
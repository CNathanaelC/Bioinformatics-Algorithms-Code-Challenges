import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your burrows_wheeler_transform function here, along with any subroutines you need
def burrows_wheeler_transform(text: str) -> str:
    """
    Generate the Burrows-Wheeler Transform of the given text.
    """
    pairs = []
    for i in range(len(text)):
        pairs.append(text[i:]+text[:i])
    pairs = sorted(pairs)
    return "".join([i[-1] for i in pairs])
"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    
    new = slide(line)
            
    for index in range(1, len(line)):
        if new[index] == new[index-1]:
            new[index-1] = new[index-1] + new[index]
            new[index] = 0
    
    merged = slide(new)
    
    return merged

def slide(line):
    """
    Helper function for merge:
    slide all non-zero numbers left
    """
    new = [0] * len(line)
    index = 0
    for num in line:
        if num != 0:
            new[index] = num
            index += 1
    return new

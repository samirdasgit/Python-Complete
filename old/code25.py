def abs_diff_between_sum_and_sum_of_squares(a:int, b:int) -> int:
    '''
    Given two integers, find the absolute difference between 
    their sum and the sum of their squares.
    Eg. 
    a, b = 2,3 
    sum is 5
    sum of squares is 13 
    absolute difference is 8

    Args:
        a - int : The first integer.
        b - int : The second integer.

    Returns:
        int: absolute difference between the sum and the sum of squares
    sum of numbers=(a+b)
    sum of squares=(a*2+b*2)
    return abs(sum of numbers-sum of squares)
    

def swap_except_middle_three(s: str) -> str:
    Given an odd-length string,
    swap the parts before and after the middle three characters,
    while keeping the middle three characters in place.

    Assume the string has at least 5 characters.

    Examples:
        "firstabclast1" -> "last1abcfirst"
        "abcdefghi" -> "ghidefabc"

    Args:
        s (str): The input string of odd length.

    Returns:
        str: The modified string with the parts swapped.
    n=len(s)
    middle_index=len(s)//2
    
    before=s[:middle_index-1]
    middle=s[middle_index-1:middle_index+2]
    after=s[middle_index+2:]
    return(after+middle+before)
    '''

def interleave_lists(list1, list2, list3):
    Given three lists of same length, 
    interleave them together and return the interleaved list.

    Example:
        list1 = [1, 2, 3]
        list2 = ['a', 'b', 'c']
        list3 = [(1,1),(2,2),(3,3)]
        output = [1, 'a', (1,1), 2, 'b', (2,2), 3, 'c', (3,3)]

    Args:
        list1 (list): The first list.
        list2 (list): The second list.
        list3 (list): The third list.

    Returns:
        list: A list containing interleaved elements from all three lists.
    interleaved=[item for trio in zip(list1,list2,list3)for item in trio]
    return(interleaved)
    ...

def has_more_than_5_unique_digits(num: int) -> bool:
    Determine if a given integer has more than 5 unique digits.

    Args:
        num (int): The input integer.

    Returns:
        bool: True if the integer has more than 5 unique digits, otherwise False.
    return len(set(str(abs(num))))>5
    ...

def final_position(pos: tuple, vel: tuple, time:int) -> tuple:
    Given an initial position of a point moving in a cartesian plane with a constant velocity, 
    find the the final position of the point after a given time. 

    Hint: final position = intial position + velocity * time

    Args:
        pos - tuple[int]: A tuple representing the position vector (x1, y1).
        vel - tuple[int]: A tuple representing the velocity vector (vx, vy).
        time - int: time of movement.

    Returns:
        tuple[int]: A tuple representing the displacement (dx, dy).
    '''
    return pos[0] + vel[0] * time, pos[1] + vel[1] * time

    ...

def remove_keys_not_in_list(d: dict, l: list) -> None:
    '''
    Remove keys from a dictionary that are not present in a given list.
    The function modifies the dictionary in place and does not return anything.

    Note: 
        Modifying a dict while iterating over it will give an error in python. 
        So, make a copy of the dict keys and then iterate over it.

    Args:
        d (dict): The dictionary to modify.
        l (list): The list of keys to keep in the dictionary.

    Returns:
        None
    '''
    keys_to_remove=[key for key in d.keys()if key_not_in_list]
    for key in keys_to_remove:
        del(keys_to_remove)
    '''
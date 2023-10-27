"""
Pycutroh

A cross plattform string cutting module for Python. Inspired by the linux cut command.

Usage:
    import pycutroh
    content = "This is a demonstration string."
    print(pycutroh.get_fields_new_separator(content, (0, 3), " ", "|"))

Returns:
    This|demonstration

Author: IT-Administrators
License: MIT

"""

# ---------- Helper functions ----------
# Helper function for position handling.
# Normally arrays start counting by 0. This function makes them start by 1.
def pos_handling(pos: int):
    """If used it starts counting by 1. Default is 0."""
    newpos = pos - 1
    if newpos < 0:
        newpos = 0
    return newpos

# Removes the leading separator if it exists.
def remove_leading_separator(content: str, sep: str):
    """Removes the leading separator, if it exists."""
    if content.startswith(sep):
        newstr = content[1:]
        return newstr
    else:
        return content

# Replaces the specified separator with a new one. 
def replace_separator(content: str, sep: str, newsep: str):
    """Replaces all separators with a new one.
    
    This is a helper function for the get_fields_new_separator function. 
    If handles some cases depending on the provided separators. 

    For example: 
    If only one separator exists in the provided string, it is replaced
    with the separator that is not in the string. 
    If both separators exist in the string, the first provided separator
    is replaced by the second.
    This can lead to some weird results if you have a string with the ";" delimiter, 
    that contains a date or time, which are usually delimited with "." or ":".
    """
    # Check if sep is in content and newsep not.
    if sep in content and newsep not in content:
        return str(content).replace(sep, newsep)
    # Check if newsep is in content and sep not.
    elif newsep in content and sep not in content:
        return str(content).replace(newsep, sep)
    # If content contains bot separators the sep is replaced with the newsep. 
    elif newsep and sep in content:
        return str(content).replace(sep, newsep)

def calc_separator_pos(content: str, sep:str):
    """Calculates the positions of the specified separator in the specified string."""
    # Initialising the separator list by adding 0 and contentlength.
    # This must be done to calculate the right amount of fields.
    seppos = [0, len(content)]

    # Iterating over content an adding the separator postions to the list.
    for chr in range(len(content)):
        if content[chr] == sep:
            seppos.append(chr)
    # Sorting the list for the field calculation.
    # If the list isn"t sorted the field calculation goes wrong because of wrong field limitations.
    sortedseppos = sorted(seppos)
    return sortedseppos

def calc_fields(fields: tuple, seppos: list):
    """Calculate the fields in the specified string."""
    fieldstart = 0
    fieldlist = []
    # Iterating over the specified fieldlist.
    # Setting new fieldstart, to start at the separator position +1.
    # Than adding the field parameters (fieldstart, fieldlength) to the fieldlist. 
    for field in fields:
        fieldstart = seppos[field]
        if field in range(len(seppos)):
            fieldlist.append((fieldstart, seppos[field + 1] - seppos[field]))
    return fieldlist

# ---------- Main functions ----------
# Get letter on position.
def get_letter_on_pos(content: str, pos: int):
    """Get the letter on the specified position."""
    if pos >= len(content):
        return content
    else:
        return content[pos]

# Get letters from pos to position.
def get_letters_from_pos_to_pos(content: str, pos: tuple):
    """Get letters between the specified positions."""
    # Gets only the letters from pos to position.
    # If there is no postion specified after the :
    # the string is returned from the starting position until the end. 
    newstr = content[pos[0]:pos[1]]
    return newstr

# Get content of the specified fields and join them to a new string, with the same separator.
def get_fields(content: str, fields: tuple, sep: int):
    """Get the specified fields.
    
    Retrieve the specified fields from the given string, using the specified
    separator as the field limitations. 
    Than join the retrieved fields using the specified separator.
    """
    newstringlst = []
    seppos = calc_separator_pos(content,sep)
    fieldlist = calc_fields(fields,seppos)
    # Creating the new string, by adding the content from the fieldstart position
    # to with the fieldlength.
    for f in fieldlist:
        newstringlst.append(content[f[0]:(f[0] + f[1])])
    # Returning the list as a string, by joining all elements together. 
    return remove_leading_separator(str().join(newstringlst), sep)

# Get content of the specified fields and join them to a new string, with a new separator.
def get_fields_new_separator(content: str, fields: tuple, sep: str, newsep: str):
    """Get the specified fields.
    
    Retrieve the specified fields from the given string, using the specified
    separator as the field limitations. 
    Than join the retrieved fields using the new separator.
    """
    newstr = get_fields(content, fields, sep)
    return replace_separator(newstr, sep, newsep)


# Functions that are imported by calling from <modulename> import *
__all__ = ["get_letter_on_pos", "get_letters_from_pos_to_pos", "get_fields", "get_fields_new_separator"]
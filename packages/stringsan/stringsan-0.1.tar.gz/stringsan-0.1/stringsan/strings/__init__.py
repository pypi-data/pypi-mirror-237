import re 

from itertools import groupby

def occurences(string: str, pattern) -> int:
    """
    Find all the occurences of the given pattern in the string

    :param: `pattern` can be a string or a regular expression
    """
    _occurences = re.findall(pattern, string)
    return len(_occurences)

def first_occurence(string: str) -> any:
    """
    Fetch the first occurence from the given string.
    """
    _match = re.search(r"\w+", string)
    return _match.group() if _match else None


def last_occurence(string: str) -> any:
    """
    Fetch the last occurence from the given string.
    """
    _match = re.findall(r"\b\w+\b", string)
    return _match[-1] if _match else None

def is_zalgo(string: str) -> bool:
    """
    Check whether the string contains zalgo characters
    """
    chars = [chr(i) for i in range(768, 879)]
    return any(char in chars for char in string)

def compress_string(string: str) -> str:
    """
    Compress a string by representing repeated characters with a numerical value.
    """
    compressed = ''.join(char + str(len(list(group))) for char, group in groupby(string))
    return compressed if len(compressed) < len(string) else string
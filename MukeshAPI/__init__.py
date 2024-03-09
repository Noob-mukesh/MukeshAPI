import random
import requests 
import string
import base64
from bs4 import BeautifulSoup


def pass_gen(num: int = 12):
    """
    This function generates a random password by combining uppercase letters, lowercase letters, punctuation marks, and digits.

    Parameters:
    - num (int): The length of the generated password. Default is 12 if not specified.

    Returns:
    - str: A randomly generated password consisting of characters from string.ascii_letters, string.punctuation, and string.digits.

    Example usage:
    >>> pass_gen()
    'r$6Ag~P{32F+'
    >>> pass_gen(10)
    'ZnK"9|?v3a'
    """
    characters = string.ascii_letters + string.punctuation + string.digits
    password = "".join(random.sample(characters, num))
    return password


def hastag_gen(arg: str):
    """
    Generate hashtags based on the given keyword using a specific website.
    
    Args:
    arg (str): The keyword for which hashtags need to be generated.
    
    Returns:
    str: A string of hashtags related to the given keyword.
    
    Example usage:
    >>> keyword = "python"
    >>> hashtags = hastag_gen(keyword)
    >>> print(hashtags)
    """
    m = base64.b64decode
    ux = m("aHR0cHM6Ly9hbGwtaGFzaHRhZy5jb20vbGlicmFyeS9jb250ZW50cy9hamF4X2dlbmVyYXRvci5waHA=").decode("utf-8")
    data = {"keyword": arg, "filter": "top"}
    res = requests.post(ux, data=data).text
    content = BeautifulSoup(res, "html.parser").find("div", {"class": "copy-hashtags"}).string
    return content



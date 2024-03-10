import random
import requests
import string
import base64
from bs4 import BeautifulSoup

__version__ = "0.5.8"

__all__ = ["hastag_gen","bhagwatgita","chatbot","pass_gen"]

def pass_gen( num: int = 12)->str:
    """
    This function generates a random password by combining uppercase letters, lowercase letters, punctuation marks, and digits.

    Parameters:
    - num (int): The length of the generated password. Default is 12 if not specified.

    Returns:
    - str: A randomly generated password consisting of characters from string.ascii_letters, string.punctuation, and string.digits.

    Example usage:
    >>> api = API()
    >>> api.pass_gen()
    'r$6Ag~P{32F+'
    >>> api.pass_gen(10)
    'ZnK"9|?v3a'
    """
    characters = string.ascii_letters + string.punctuation + string.digits
    password = "".join(random.sample(characters, num))
    return password

def hashtag_gen( arg: str)->list:
    """
    Generate hashtags based on the given keyword using a specific website.
    
    Args:
    arg (str): The keyword for which hashtags need to be generated.
    
    Returns:
    str: A string of hashtags related to the given keyword.
    
    Example usage:
    >>> api = API()
    >>> keyword = "python"
    >>> hashtags = api.hashtag_gen(keyword)
    >>> print(hashtags)
    """
    url = base64.b64decode("aHR0cHM6Ly9hbGwtaGFzaHRhZy5jb20vbGlicmFyeS9jb250ZW50cy9hamF4X2dlbmVyYXRvci5waHA=").decode("utf-8")
    data = {"keyword": arg, "filter": "top"}
    response = requests.post(url, data=data).text
    content = BeautifulSoup(response, "html.parser").find("div", {"class": "copy-hashtags"}).string
    output=content.split()
    return output
def chatbot(args:str)->str:
    """
    Interact with a chatbot to get a response based on the provided input text.

    Args:
    args (str): The text input to the chatbot for generating a response.

    Returns:
    str: The response from the chatbot based on the input text.

    Example usage:
    >>> api = API()
    >>> user_input = "Hello, how are you?"
    >>> response = api.chatbot(user_input)
    >>> print(response)
    """
    x = base64.b64decode("aHR0cHM6Ly9mYWxsZW54Ym90LnZlcmNlbC5hcHAvYXBpL2FwaWtleT01OTM1NjA4Mjk3LWZhbGxlbi11c2JrMzNrYnN1L2dyb3VwLWNvbnRyb2xsZXIvbXVrZXNoL21lc3NhZ2U9").decode("utf-8")
    full_url = f"{x}{args}"
    response = requests.get(full_url).json()["reply"]
    return response

def bhagwatgita(chapter: int, shalok: int = 1) -> dict:
    """
    Retrieve a verse from the Bhagavad Gita based on the provided chapter and shalok number.

    Args:
    chapter (int): The chapter number from which the verse will be retrieved.
    shalok (int, optional): The shalok number within the chapter. Default is 1.

    Returns:
    dict: A dictionary containing the chapter number, verse text, chapter introduction, and the specified shalok text.

    Example usage:
    >>> api = API()
    >>> verse_data = api.get_gita_verse(1, 5)
    >>> print(verse_data)
    """

    url = f"https://www.holy-bhagavad-gita.org/chapter/{chapter}/hi"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraph = soup.find("p")
    chapter_intro = soup.find("div", class_="chapterIntro")
    co = soup.find_all("section", class_="listItem")
    output = [i.text.strip().replace("View commentary »", "").replace("Bhagavad Gita ", "").strip()  for i in co]
    data = {
        "chapter_number": chapter,
        "verse": paragraph.text,
        "chapter_intro": chapter_intro.text,
        "shalok": output[shalok],
    }

    return data



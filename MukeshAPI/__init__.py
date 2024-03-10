import random
import requests
import string
import base64,json
from bs4 import BeautifulSoup
from requests_html import HTMLSession

__version__ = "0.1"

# __all__ = ["hastag_gen","bhagwatgita","chatbot","pass_gen","imdb"]
__all__ = ["api"]

class MukeshAPI:
    """Api for various purpose
    support group : https://t.me/the_support_chat
    owner : @mr_sukkun
    """
    def __init__(self)->None:
        """
        Purpose: value
        """
        
    

    def pass_gen(self, num: int = 12)-> str:
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

    def hashtag_gen(self, arg: str)-> list:
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
    def chatbot(self,args:str)->str:
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

    def bhagwatgita(self,chapter: int, shalok: int = 1) -> dict:
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


    def imdb(self,args: str) -> dict:
        """
        Retrieve information about a movie or TV show from IMDb based on the search query.

        Args:
        args (str): The movie or TV show to search for on IMDb.

        Returns:
        dict: A dictionary containing details about the movie or TV show, such as name, description, genre,
            actors, trailer link, and more.

        Example usage:
        >>> movie_data = imdb("The Godfather")
        >>> print(movie_data)
        """

        session = HTMLSession()

        url = f"https://www.imdb.com/find?q={args}"
        response = session.get(url)
        results = response.html.xpath("//section[@data-testid='find-results-section-title']/div/ul/li")
        urls = [result.find("a")[0].attrs["href"] for result in results][0]

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = requests.get(f"https://www.imdb.com/{urls}", headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")

        movie_name = soup.title.text.strip()

        meta_tags = soup.find_all("meta")
        description = ""
        keywords = ""

        for tag in meta_tags:
            if tag.get("name", "") == "description":
                description = tag.get("content", "")
            elif tag.get("name", "") == "keywords":
                keywords = tag.get("content", "")

        json_data = soup.find("script", type="application/ld+json").string
        parsed_json = json.loads(json_data)

        movie_url = parsed_json["url"]
        movie_image = parsed_json["image"]
        movie_description = parsed_json["description"]
        movie_review_body = parsed_json["review"]["reviewBody"]
        movie_review_rating = parsed_json["review"]["reviewRating"]["ratingValue"]
        movie_genre = parsed_json["genre"]
        movie_actors = [actor["name"] for actor in parsed_json["actor"]]
        movie_trailer = parsed_json["trailer"]
        
        output = []
        for result in results:
            name = result.text.replace("\n", " ")
            url = result.find("a")[0].attrs["href"]
            if ("Podcast" not in name) and ("Music Video" not in name):
                try:
                    image = result.xpath("//img")[0].attrs["src"]
                    file_id = url.split("/")[2]
                    output.append({
                        "movie_name": movie_name,
                        "id": file_id,
                        "poster": image,
                        "description": description,
                        "keywords": keywords,
                        "movie_url": movie_url,
                        "movie_image": movie_image,
                        "movie_description": movie_description,
                        "movie_review_body": movie_review_body,
                        "movie_review_rating": movie_review_rating,
                        "movie_genre": movie_genre,
                        "movie_actors": movie_actors,
                        "movie_trailer": movie_trailer,
                        "join": "@Mr_Sukkun",
                        "success": True,
                    })
                    return {"results": output}
                except:
                    return {"Success": False}
api=MukeshAPI()
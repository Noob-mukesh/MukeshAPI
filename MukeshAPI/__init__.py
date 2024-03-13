import random
import requests
import string,re
import base64,json
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import urllib
from .func import MORSE_CODE_DICT

__version__ = "0.6.2"

__all__ = ["api","AI"]


class MukeshAPI:
    
    def __init__(self)->None:
        """Api for various purpose
    support group : https://t.me/the_support_chat
    owner : @mr_sukkun
        """
        pass
    
               
    def password(self, num: int = 12)-> str:
        """
        This function generates a random password by combining uppercase letters, lowercase letters, punctuation marks, and digits.

        Parameters:
        - num (int): The length of the generated password. Default is 12 if not specified.

        Returns:
        - str: A randomly generated password consisting of characters from string.ascii_letters, string.punctuation, and string.digits.

        Example usage:
        >>> api = API()
        >>> api.password()
        'r$6Ag~P{32F+'
        >>> api.password(10)
        'ZnK"9|?v3a'
        """
        characters = string.ascii_letters + string.punctuation + string.digits
        password = "".join(random.sample(characters, num))
        return password

    def hashtag(self, arg: str)-> list:
        """
        Generate hashtags based on the given keyword using a specific website.
        
        Args:
        arg (str): The keyword for which hashtags need to be generated.
        
        Returns:
        str: A string of hashtags related to the given keyword.
        
        Example usage:
        >>> api = API()
        >>> keyword = "python"
        >>> hashtags = api.hashtag(keyword)
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

    def bhagwatgita(self,chapter: int, shalok: int = 1) -> requests.Response:
        """
        Retrieve a verse from the Bhagavad Gita based on the provided chapter and shalok number.

        Args:
        chapter (int): The chapter number from which the verse will be retrieved.
        shalok (int, optional): The shalok number within the chapter. Default is 1.

        Returns:
        dict: A dictionary containing the chapter number, verse text, chapter introduction, and the specified shalok text.

        Example usage:
        >>> api = API()
        >>> verse_data = api.bhagwatgita(1, 5)
        >>> print(verse_data)
        """
        xc=base64.b64decode("aHR0cHM6Ly93d3cuaG9seS1iaGFnYXZhZC1naXRhLm9yZy9jaGFwdGVyLw==").decode(encoding="utf-8")
        url = f"{xc}{chapter}/hi"
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
        >>> api = API()
        >>> movie_data = api.imdb("The Godfather")
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
    def morse_encode(self,args:str)->str:
        """
    Encode the input string into Morse code.

    Args:
        args (str): The input string to be encoded into Morse code. ✨

    Returns:
        str: The Morse code representation of the input string along with additional information. 🔠

    Example usage:
    >>> api = API()
    >>> encoded_result = api.morse_encode("Hello World")
    >>> print(encoded_result)
    """

        cipher = ""
        for letter in args.upper():
            if letter != " ":
                cipher += MORSE_CODE_DICT[letter] + " "
            else:
                cipher += " "
        output = {
            "input": args,
            "results": cipher,
            "join": "@Mr_Sukkun",
            "sucess": True
        }
        return (output)
    
    def morse_decode(self,args: str) -> str:
        """
    Decode the Morse code back into the original text. 🔄

    Args:
        args (str): The Morse code to be decoded back into text.

    Returns:
        str: The decoded text from the Morse code.

    Example usage:
    >>> api = API()
    >>> decoded_result =api.morse_decode(".... . .-.. .-.. --- / .-- --- .-. .-.. -..")
    >>> print(decoded_result)
    """

        args += " "
        decipher = ""
        citext = ""
        for letter in args:
            if letter != " ":
                i = 0
                citext += letter
            else:
                i += 1
                if i == 2:
                    decipher += " "
                else:
                    decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                    citext = ""
        output = {
            "input": args,
            "results": decipher,
            "join": "@Mr_Sukkun",
            "success": True
        }
        return output
       
    
    def unsplash(self,args)->requests.Response:
        """
    Get image URLs related to the query using the iStockphoto API.

    Args:
        args (str): The search query for images.

    Returns:
        list: List of image URLs related to the query.
        
    Example usage:
    >>> api = API()
    >>> response = api.unsplash("boy image")
    >>> print(response)
    

    """
        url = f'https://www.istockphoto.com/search/2/image?alloweduse=availableforalluses&phrase={args}&sort=best'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://unsplash.com/'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            
        
            soup = BeautifulSoup(response.content, 'html.parser')
            image_tags = soup.find_all('img')
            image_urls = [img['src'] for img in image_tags if img['src'].startswith('https://media.istockphoto.com')]
            
            return {"results": image_urls, "join": "@Mr_Sukkun", "success": True}
        else:
            return {f"status code: {response.status_code}"}
        
    def leetcode(self,username):
        """
    Retrieve user data including activity streak, profile information, and contest badges from LeetCode using GraphQL API.

    Args:
        username (str): The username of the LeetCode user.

    Returns:
        dict: A dictionary containing user data such as streak, total active days, badges, user profile information, and social media URLs.

    Example usage:
    >>> api = API()
    >>> user_data = api.leetcode("noob-mukesh")
    >>> print(user_data)"""
        url = base64.b64decode('aHR0cHM6Ly9sZWV0Y29kZS5jb20vZ3JhcGhxbC8=').decode("utf-8")

        payload = {
        'operationName': 'userProfileCalendar',
        'query': '''
        query userProfileCalendar($username: String!, $year: Int) {
        matchedUser(username: $username) {
            userCalendar(year: $year) {
            activeYears
            streak
            totalActiveDays
            dccBadges {
                timestamp
                badge {
                name
                icon
                }
            }
            submissionCalendar
            }
        }
        }
        ''',
        'variables': {'username': username, 'year': 2024}
    }

        payload_2 = {
        'operationName': 'userPublicProfile',
        'query': '''
        query userPublicProfile($username: String!) {
        matchedUser(username: $username) {
            contestBadge {
            name
            expired
            hoverText
            icon
            }
            username
            githubUrl
            twitterUrl
            linkedinUrl
            profile {
            ranking
            userAvatar
            realName
            aboutMe
            school
            websites
            countryName
            company
            jobTitle
            skillTags
            postViewCount
            postViewCountDiff
            reputation
            reputationDiff
            solutionCount
            solutionCountDiff
            categoryDiscussCount
            categoryDiscussCountDiff
            }
        }
        }
        ''',
        'variables': {'username': username}
    }

        try:
            response = requests.post(url, json=payload)
            data_1 = response.json()['data']['matchedUser']

            response = requests.post(url, json=payload_2)
            data_2 = response.json()['data']['matchedUser']

            output_dict2 = {} 
            output_dict2.update(data_1)
            output_dict2.update(data_2)
            output_dict = {}

            for key, value in output_dict2.items():
                if isinstance(value, dict):
                    output_dict[key] = {}
                    for k, v in value.items():
                        output_dict[key][k] = v
                else:
                    output_dict[key] = value
            return output_dict
        except Exception as e:
            return e
        
    
    def pypi(self,args):
        """
    Retrieve package information from the Python Package Index (PyPI) by providing the package name.

    Args:
        args (str): The name of the package to search for on PyPI.

    Returns:
        dict: A dictionary containing information about the specified package, such as name, version, description, author, license, and more.

    Example usage:
    >>> api = API()
    >>> package_info = api.pypi("requests")
    >>> print(package_info)
    """
   
        n = base64.b64decode("aHR0cHM6Ly9weXBpLm9yZy9weXBpLw==").decode("utf-8")
        result = requests.get(f"{n}{args}/json").json()["info"]
        return result
    
    
    def repo(self,args):
        """
    Search GitHub repositories based on the search query provided.

    Args:
        args (str): The search query to find repositories on GitHub.

    Returns:
        dict: A dictionary containing search results of GitHub repositories. Each entry includes an index and corresponding repository.

    Example usage:
    >>> api = API()
    >>> search_results = api.repo("MukeshRobot")
    >>> print(search_results)
    """
        
        n = base64.b64decode("aHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9zZWFyY2gvcmVwb3NpdG9yaWVzP3E9"
            ).decode("utf-8")
        search_results = requests.get(f"{n}{args}").json()
        items = search_results.get("items", [])
        result = []
        for index, item in enumerate(items, 1):
            result.append((index, item))

        return {"results": result, "join": "@Mr_Sukkun", "sucess": True}
    def github(self,args):
        """
    Search GitHub information based on the username query provided.

    Args:
        args (str): The search query to find information of  GitHub User.

    Returns:
        dict: A dictionary containing search results of GitHub username .

    Example usage:
    >>> api = API()
    >>> search_results = api.github("noob-mukesh")
    >>> print(search_results)
    """

        n = base64.b64decode("aHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS91c2Vycy8=").decode("utf-8")
        result = requests.get(f"{n}{args}").json()
        url = result["html_url"]
        name = result["name"]
        id = result["id"]
        company = result["company"]
        bio = result["bio"]
        pattern = "[a-zA-Z]+"
        created_at = result["created_at"]
        created = re.sub(pattern, " ", created_at)
        updated_at = result["updated_at"]
        updated = re.sub(pattern, " ", updated_at)
        avatar_url = f"https://avatars.githubusercontent.com/u/{id}"
        blog = result["blog"]
        location = result["location"]
        repositories = result["public_repos"]
        followers = result["followers"]
        following = result["following"]
        results = {
            "url": url,
            "name": name,
            "id": id,
            "company": company,
            "bio": bio,
            "created at": created,
            "updated at": updated,
            "Profile image": avatar_url,
            "blog": blog,
            "location": location,
            "repos": repositories,
            "followers": followers,
            "following": following,
        }
        return results
    def meme(self):
        """ Fetch  random memes from reddit
        
        Returns:
        
        dict: A dictionary containing search results of meme
        
        Example usage:
        >>> api = API()
        >>> search_results = api.meme()
        >>> print(search_results)
        """

        n = base64.b64decode("aHR0cHM6Ly9tZW1lLWFwaS5jb20vZ2ltbWU=").decode("utf-8")
        res = requests.get(f"{n}").json()
        title = res["title"]
        url = res["url"]
        results = {"title": title, "url": url}
        return results
    

api=MukeshAPI()

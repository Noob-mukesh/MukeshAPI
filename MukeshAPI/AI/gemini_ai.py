from .. import MukeshAPI
import requests
import json
import urllib
from base64 import b64decode as m

def gemini(self, args: str) -> dict:
    """
    Generate content using the Gemini API. ✨

    Args:
        args (str): The input text to generate content.

    Returns:
        dict: A dictionary containing the generated content with metadata.

    Example usage:
    >>> api = API()
    >>> generated_content = api.gemini("Hello, how are you?")
    >>> print(generated_content)
    """
    url = m('aHR0cHM6Ly9nZW5lcmF0aXZlbGFuZ3VhZ2UuZ29vZ2xlYXBpcy5jb20vdjFiZXRhL21vZGVscy9nZW1pbmktcHJvOmdlbmVyYXRlQ29udGVudD9rZXk9QUl6YVN5QlFhb1VGLUtXalBWXzRBQnRTTjBEUTBSUGtOZUNoNHRN').decode("utf-8")
    headers = {'Content-Type': 'application/json'}
    payload = {
        'contents': [
            {'parts': [{'text': args}]}
        ]
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            generated_text = response.json()["candidates"][0]["content"]["parts"][0]["text"]
            return {"results":generated_text,"join": "@Mr_Sukkun", "success": True}
    except Exception as e:
        return e
    
MukeshAPI.gemini=gemini
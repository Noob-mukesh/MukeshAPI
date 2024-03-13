from .. import MukeshAPI
import requests
import json
import re
from base64 import b64decode as m

def datagpt(self,args):
        """
        Sends a query to a specified datagpt API endpoint to retrieve a response based on the provided question.

        Args:
            args (str): The question or input for the datagpt.

        Returns:
            str: The response text from the datagpt API.

        Example usage:
        >>> api = API()
        >>> response = api.datagpt("What are the latest trends in AI?")
        >>> print(response)
        """
        url = m("aHR0cHM6Ly9hcHAuY3JlYXRvci5pby9hcGkvY2hhdA==").decode("utf-8")
        payload = {
            "question": args,
            "chatbotId": "712544d1-0c95-459e-ba22-45bae8905bed",
            "session_id": "8a790e7f-ec7a-4834-be4a-40a78dfb525f",
            "site": "datacareerjumpstart.mykajabi.com"
        }

        try:
            response = requests.post(url, json=payload)
            extracted_text = re.findall(r"\{(.*?)\}", response.text, re.DOTALL)
            extracted_json = "{" + extracted_text[0] + "}]}"
            json_text = extracted_json.replace('\n', ' ')

            data = json.loads(json_text)
            return {"results":data["text"],"join": "@Mr_Sukkun", "success": True
                    }
        except Exception as e:
            return e
MukeshAPI.datagpt=datagpt
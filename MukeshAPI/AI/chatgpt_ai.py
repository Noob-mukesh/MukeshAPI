from .. import MukeshAPI
import requests
import json
import urllib
from base64 import b64decode as m
from ..func import (payloads_response,gpt_4_mode,payload8)

def chatgpt(self,args,mode:str=False):
       
        """
        Sends a query to a specified chatgpt API endpoint to retrieve a response based on the provided question.
        

        Args:
            args (str): The question or input for the chatgpt.
            mode(str) : this  parameter is used to select different models of Chatgpt
                        available modes are "girlfriend","anime","animev2","flirt","santa","elonmusk"

        Returns:
            str: The response text from the chatgpt API.

        Example usage:
        >>> api = API()
        >>> response = api.chatgpt("hi babe?",mode="girlfriend")
        >>> print(response)
        """
        if not mode:
            try:
                session = requests.Session()
                response_data=payloads_response(payloads=payload8,args=args)
                url = "https://api.exh.ai/chatbot/v1/get_response"
                headers = {
                "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJ1c2VybmFtZSI6ImJvdGlmeS13ZWItdjMifQ.O-w89I5aX2OE_i4k6jdHZJEDWECSUfOb1lr9UdVH4oTPMkFGUNm9BNzoQjcXOu8NEiIXq64-481hnenHdUrXfg",
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
            }
                response = session.post(url, headers=headers, data=json.dumps(response_data))
                return {"results":response.json()["response"],"join": "@Mr_Sukkun", "success": True}
            except Exception as e:
                return e
        else:
            try:
                result = gpt_4_mode(args, mode)
                return {"results":result,"join": "@Mr_Sukkun", "success": True}
                
            except Exception as e:
                return e
        
MukeshAPI.chatgpt=chatgpt

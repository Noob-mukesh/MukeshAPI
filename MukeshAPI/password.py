import requests
def pass_gen(num):
    res=requests.get(url=f"https://mukesh-api.vercel.app/password/{num}").json()
    return res

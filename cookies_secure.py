import requests
import urllib3

def get_cookies(domain):
    cookies_secure = {}
    try:
        session = requests.Session()
        response = session.get("http://"+domain, verify=False)
        for cookie in session.cookies:
            cookies_secure[cookie.name] = {"value": cookie.value, "secure": cookie.secure}
        return cookies_secure
    except urllib3.exceptions.MaxRetryError:
        # print("urllib3.exceptions.MaxRetryError, cookies_secure")
        pass
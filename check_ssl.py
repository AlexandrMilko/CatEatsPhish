import sys
import requests

def has_ssl(domain):
    try:
        response = requests.get("http://"+domain)
        return True
    except requests.exceptions.SSLError:
        return False
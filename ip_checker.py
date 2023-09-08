import requests
from config import IP_CHECK_URL

def get_public_ip():

    try:
        response = requests.get(IP_CHECK_URL)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Exception occurred: {e}")
        return None

def has_ip_changed(old_ip):

    new_ip = get_public_ip()
    if new_ip is None:
        return False, old_ip
    elif new_ip != old_ip:
        return True, new_ip
    else:
        return False, old_ip

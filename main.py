import time
from config import CHECK_INTERVAL, CHECK_URL
from ip_checker import get_public_ip, has_ip_changed
from logger import logger, log_info, log_warning, log_error
import requests
import datetime


def check_internet_connection():
    try:
        response = requests.get(CHECK_URL)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        return False

def main():
    
    old_ip = get_public_ip()
    if old_ip is None:
        log_error("Unable to get the public IP")
        return

    log_info(f"Starting with IP: {old_ip}")
    start_time = datetime.datetime.now()

    while True:
        if not check_internet_connection():
            log_error("Internet connection lost")
        else:
            ip_changed, new_ip = has_ip_changed(old_ip)
            if ip_changed:
                end_time = datetime.datetime.now()
                duration = (end_time - start_time).total_seconds() / 60
                log_info(f"IP changed from {old_ip} to {new_ip}. The previous IP was used for {duration:.2f} minutes")
                old_ip = new_ip
                start_time = datetime.datetime.now()
            else:
                current_time = datetime.datetime.now()
                duration = (current_time - start_time).total_seconds() / 60
                log_info(f"Current IP {old_ip} is being used for {duration:.2f} minutes")

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
    
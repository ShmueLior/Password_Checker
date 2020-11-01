import requests
import hashlib
from configparser import ConfigParser


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching api data with status code of: {res.status_code}, and error message of: {res.content}')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return -1


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    sha1passwordFirstFive = sha1password[:5]
    sha1passwordTail = sha1password[5:]
    try:
        res = request_api_data(sha1passwordFirstFive)
        return get_password_leaks_count(res, sha1passwordTail)
    except Exception as exception:
        raise exception


def main():
    config_object = ConfigParser()
    config_object.read('./config/config.ini')
    passwords = list(config_object['PASSWORD']['password'].split(','))
    for password in passwords:
        count = pwned_api_check(password)
        if count == -1:
            print(f'The password \'{password}\' is all good!')
        else:
            print(f'The password \'{password}\' is bad, because it is been pwned for {count} times')



main()

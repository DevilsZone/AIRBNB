from stem import Signal
from stem.control import Controller
import requests

from fake_header import give_fake_headers

def renew_connection():
    with Controller.from_port(port=9051) as controller:
        try:
            controller.authenticate(password="AkasHKumar@1")
        except Exception as e:
            print("Error Here")
            print(e.args)
        try:
            controller.signal(Signal.NEWNYM)
        except Exception as e:
            print("Error There")
            print(e.args)
    print("Done")
    return give_fake_headers()

def get_tor_session():
    session = requests.session()
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    print(session.get("http://httpbin.org/ip").text)
    print(requests.get("http://httpbin.org/ip").text)
    return session


get_tor_session()

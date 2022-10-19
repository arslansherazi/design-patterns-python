"""
- Controls and manage access to the object protected by proxy pattern
- Following are some types of proxies
    1. Remote proxy (used to interact with the object located remotely)
    2. Virtual proxy (used to provide default response if response from actual object is delayed)
    3. Protection proxy (used as protection layer)
    4. Cache proxy (used to cache frequent results)
- It provides all the interfaces of actual object

Architecture:
Application/User (do_operation) --> Proxy (do_operation) --> Actual Object
                              <--                        <--

Example:
    A very simple real life scenario is our college internet, which restricts few site access. The proxy first checks
    the host you are connecting to, if it is not part of restricted site list, then it connects to the real internet.
    This example is based on Protection proxies.
"""
from abc import ABCMeta, abstractmethod


class Internet(metaclass=ABCMeta):
    @abstractmethod
    def connect_to(self, host: str):
        pass


class RealInternet(Internet):
    def connect_to(self, host: str):
        print('Connecting to: ', host)


# Protection Proxy
class InternetProxy(Internet):
    def __init__(self):
        self.internet = RealInternet()
        self.banned_sites = ['youtube.com', 'facebook.com', 'twitter.com', 'instagram.com']

    def connect_to(self, host: str):
        if host.lower() in self.banned_sites:
            raise Exception('This website is not allowed within the office premises')
        self.internet.connect_to(host)


if __name__ == '__main__':
    internet = InternetProxy()
    internet.connect_to(host='google.com')
    internet.connect_to(host='twitter.com')
    internet.connect_to(host='yahoo.com')


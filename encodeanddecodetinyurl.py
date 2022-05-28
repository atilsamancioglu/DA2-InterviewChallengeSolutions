'''
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Implement the Solution class:

Solution() Initializes the object of the system.
String encode(String longUrl) Returns a tiny URL for the given longUrl.
String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.
'''

class Codec:
    
    def __init__(self):
        self.encodingMap = {}
        self.decodingMap = {}
        self.baseUrl = "https://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encodingMap:
            shortUrl = self.baseUrl + str(len(self.encodingMap) + 1)
            self.encodingMap[longUrl] = shortUrl
            self.decodingMap[shortUrl] = longUrl
        return self.encodingMap[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        return self.decodingMap[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
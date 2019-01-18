from html.parser import HTMLParser

"""Parser for Amazon login page"""
class AmazonLoginParser(HTMLParser):
    def __init__(self):
        self.xmonkey=1
        super().__init__()
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
 
    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

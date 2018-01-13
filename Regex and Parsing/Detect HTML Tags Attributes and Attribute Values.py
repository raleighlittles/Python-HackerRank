from html.parser import HTMLParser

# Same approach as the HTML Parser 1 Challenge! Make a subclass and override methods
N = int(input())
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attributes):
        print(tag)
        [print('-> {} > {}'.format(*attribute)) for attribute in attributes]
    
html = '\n'.join([input() for x in range(0, N)])  
parser = MyHTMLParser()
parser.feed(html)
parser.close()
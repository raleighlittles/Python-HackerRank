def get_attr_number(node):
    # your code goes here
    # Use the iter(): https://docs.python.org/3/library/xml.etree.elementtree.html
    return sum([len(element.items()) for element in tree.iter()])

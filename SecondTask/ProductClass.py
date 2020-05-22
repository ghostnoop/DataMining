class Product(object):

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def __lt__(self, other):
        return self.count < other.count

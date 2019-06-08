import json

class Contact:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def full_name(self):
        return("{} {}".format(self.first, self.last))

class ContactEncoder(json.JSONEncoder):
    
    def default(self, obj):
        if isinstance(obj, Contact):
            return {'is_contact': True,
                    'first': obj.first,
                    'last': obj.last,
                    'full': obj.full_name}
        return super().default(obj)

if __name__ == '__main__':
    c = Contact("John", "Smith")
    print(json.dumps(c, cls=ContactEncoder))

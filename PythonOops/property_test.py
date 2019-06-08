class Color:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name
    
    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name
    
    def _get_name(self):
        return self._name
    
    name = property(_get_name, _set_name)

#Using Decorators
'''
class Silly:
    @property
    def silly(self):
        "This is a silly property"
        print("You are getting silly")
        return self._silly
    @silly.setter
    def silly(self, value):
        print("You are making silly {}".format(value))
        self._silly = value
    @silly.deleter
    def silly(self):
        print("Whoah, you killed silly!")
        del self._silly

'''
if __name__ == '__main__':
    c = Color(22, '')
    c.name ='ank' 
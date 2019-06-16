class User(object):
    ID = 1
    def __init__(self, name):
        self.id = User.ID
        self.name = name
        self.calendar = dict()
        self.invitations = list()
        User.ID += 1
    
    def get_calendar(self):
        for days in self.calendar:
            print(self.calendar[days])
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name


if __name__ == '__main__':
    u1 = User('A')
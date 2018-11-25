class Bunch(dict):
    def __init__(self, *args, **kwargs):
        super(Bunch, self).__init__(*args, **kwargs)
        self.__dict__ = self

if __name__ == '__main__':
    x = Bunch(name="Jayne Cobb", position="Public Relations")
    print(x.name)
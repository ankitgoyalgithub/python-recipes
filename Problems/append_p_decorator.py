def append_p(func):
    def wrapper(arg):
        arg = '<p>'+arg+'</p>'
        func(arg)
    return wrapper

def append_q(*args, **kwargs):
    def wrapper(func):
        def deco(inp):
            print(args)
            print(kwargs)
            func(inp)
        return deco 
    return wrapper

@append_p
def process_1(arg):
    print(arg)

@append_q(2,3)
def process_2(inp):
    print(inp)

if __name__ == '__main__':
    # process_1('ankit')
    process_2('ankit')
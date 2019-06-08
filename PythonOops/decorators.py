from time import time

def add_p(function):
    def func(inp):
        foo = function(inp)
        return '<p>' + foo + '</p>'
    return func

def timeit(function):
    def func(inp):
        start_time = time()
        result = function(inp)
        end_time = time()
        print(f"Time taken for execution is {end_time - start_time}")
        return result
    return func

@timeit
@add_p
def test(inp):
    return inp

if __name__ == '__main__':
    print(test('ankit'))
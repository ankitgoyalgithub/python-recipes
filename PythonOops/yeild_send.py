def psychologist():
    print("Tell You Problems")
    
    while True:
        answer = (yield)
        if answer is not None:
            if answer.endswith('?'):
                print("Don't ask yourself too many Questions")
            elif 'good' in answer:
                print("A that's good, go on")
            elif 'bad' in answer:
                print("Don't be so Negative")

def my_generator():
    try:
        yield 'something'
    except ValueError:
        yield 'dealing with the exception'
    finally:
        print("Ok, Lets Clean")

if __name__ == '__main__':
    free = psychologist()
    next(free)
    free.send("I feel Bad")
    free.send("Why I Shouldn't ?")
    free.send("ok then i should find what is good for me")

    g = my_generator()
    print(next(g))
    print(g.throw(ValueError("Mean")))
    print(g.close())
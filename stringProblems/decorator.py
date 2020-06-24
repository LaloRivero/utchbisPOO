def say_good_morning(func):
    def wrapper(name):
        return f'Good morning! My name is {name}'
    return wrapper


@say_good_morning
def say_hello(name):
    return f'Hello my name is {name}'


def run():
    name = 'Miguel Habacuc'
    print(say_hello(name))


if __name__ == "__main__":
    run()
def say_good_bye():
    print('Good bye!')

def super_function(func):
    func()

#######################################################

def say_good_mornign(func):
    def wraper(name):
        return f'Good morning! My name is {name}'
    return wraper


@say_good_mornign
def say_hello(name):
    return f'Hello my name is {name}'


def run ():
    name = 'Jimmy Johns'
    print(say_hello(name))

#######################################################

if __name__ == "__main__":
    super_function(say_good_bye)
    run()
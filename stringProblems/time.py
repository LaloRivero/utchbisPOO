from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Time elapsed {time_elapsed.total_seconds()}s')
    return wrapper


@execution_time
def random_func():
    print('start')
    for _ in range(1,100000000):
        pass
    print('end')


@execution_time
def random_func2():
    print('start')
    for _ in range(1,1000000):
        pass
    print('end')
    
    
random_func()
random_func2()
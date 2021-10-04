from datetime import datetime

def execution_time(func):
    """Calculate the execution time of an specific function"""    
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        delta = final_time-initial_time
        print(f'The execution time of the function is: ' + str(delta.total_seconds()) + ' segundos.')        
    return wrapper


@execution_time
def for_cicle():
    for _ in range(1000000):  # The "_"  symbol means that a will not use the variable.
        pass


@execution_time
def sum(x: int, y: int):
    sum_numbers=x+y
    print(f'The sum of {x} and {y} is: {sum_numbers}')


@execution_time
def greating(name: str):
    print(f'Hi {name}! hope you are enjoying this practice!')


def run():
    for_cicle()
    print('*'*30)
    sum(3,4)
    print('*'*30)
    greating('Manuel')


if __name__ == "__main__":
    run()
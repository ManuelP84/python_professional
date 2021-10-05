from time import sleep

def fibonacci_generator(max: int) -> int:
    counter =0
    num0=0
    num1=1 

    while True:
        if counter ==0:
            counter+=1
            yield num0
        elif counter==1:
            counter+=1
            yield num1
        else:
            sum=num0+num1
            num0, num1=num1, sum
            if counter<max:
                counter+=1
                yield sum
            else:
                break

if __name__ == "__main__":
    fibGen=fibonacci_generator(10)

    for element in fibGen:
        print(element)
        sleep(0.5)
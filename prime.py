    
def request_number() -> int:     
    try:
        number: int = int(input("Please enter the number: "))
        if number==0 or number ==1:
            raise TypeError
    except:
        print("Incorrect number! It must be different than '0' and '1'.") 
    else:
        return number
    finally:
        print("Process finished!")


def is_prime(number: int) -> bool:
    cont=0
    flag=False
    for i in range(2,number+1):
        if number%i!=0:
            continue
        else:
            cont +=1
    if cont==1:
        flag = True    
    return flag
    

def run():
    number: int = request_number()
    if is_prime(number):
        print(f'The number {number} is prime')
    else:
        print(f'The number {number} is NOT prime')


if __name__ == "__main__":
    run()

    

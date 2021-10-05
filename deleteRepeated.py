import random 

# Method 1. Delete repeated elements from a list. Using sets. 
def randomList(max: int):
    """Return a random list"""
    return [random.randint(0,10) for _ in range(max)]

def deleteRepeatedM1(some_list: list): #Cast from list to set and finally from set to list
    """Delete repeated elements from a list. Using sets. Returns an ordered list"""
    return list(set(some_list))

# Method 2. Delete repeated elements from a list.
def deleteRepeatedM2(some_list: list):
    """Delete repeated elements from a list. Returns an unordered list"""
    my_list = list()
    for element in some_list:
        if element not in my_list:
            my_list.append(element)
    return my_list

def run():
    """Main function"""
    my_list = randomList(20)
    my_new_list1 = deleteRepeatedM1(my_list)
    my_new_list2 = deleteRepeatedM2(my_list)
    print(f'A random list: {my_list}')
    print("**********Method 1**********")
    print(f'The list without repeated elements: {my_new_list1}')
    print("**********Method 2**********")
    print(f'The list without repeated elements: {my_new_list2}')
    

if __name__ == "__main__":
    run()



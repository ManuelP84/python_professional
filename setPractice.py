import random

def setsMaker():
    """Return a list with 2 elements. Each of them is a random set"""
    max_set_1= random.randint(6,10)
    max_set_2 = random.randint(6,10)
    set1 = {random.randint(0,max_set_1) for s in range(10)} # Implement set comprehension
    set2 = {random.randint(0,max_set_2) for s in range(10)} # Implement set comprehension
    return [set1,set2]

def randomSet():
    return {random.randint(0,10) for s in range(0,10)}

def randomList():
    return [random.randint(0,10) for l in range(0,5)]

def randomNumber():
    """Return a random number"""
    return random.randint(0,10)

def run():
    """Main function"""
    message="""
            ******************
            Set operations 
            ******************"""
    print(message)
    
    #Union between set's
    print("Union")
    set_list=setsMaker()
    set_result = set_list[0] | set_list[1]
    print(f"Set 'union' between Set 1: {set_list[0]} and Set 2: {set_list[1]}")
    print(f'Set result: {set_result}')
    print("************************************************************************************")

    #Intersection between set's
    print("Intersection")
    set_list=setsMaker()
    set_result = set_list[0] & set_list[1]
    print(f"Set 'intersection' between Set 1: {set_list[0]} and Set 2: {set_list[1]}")
    print(f'Set result: {set_result}')
    print("************************************************************************************")

    #Difference between set's
    print("Difference: Set1 - Set2")
    set_list=setsMaker()
    set_result = set_list[0] - set_list[1]
    print(f"Set 'difference' between Set 1: {set_list[0]} and Set 2: {set_list[1]}")
    print(f'Set result: {set_result}')
    print("************************************************************************************")

    #Difference between set's
    print("Difference: Set2 - Set1")
    set_list=setsMaker()
    set_result = set_list[1] - set_list[0]
    print(f"Set 'difference' between Set 2: {set_list[1]} and Set 1: {set_list[0]}")
    print(f'Set result: {set_result}')
    print("************************************************************************************")

    #Simetric Difference between set's
    print("Simetric Difference")
    set_list=setsMaker()
    set_result = set_list[0] ^ set_list[1]
    print(f"Set 'difference' between Set 1: {set_list[0]} and Set 2: {set_list[1]}")
    print(f'Set result: {set_result}')
    print("************************************************************************************")

    #Clean set_result
    set_result.clear()

    #Implementing pop() function
    print("Implementing pop() function")
    my_set = randomSet()
    print(my_set)
    for _ in range(len(my_set)):
        my_set.pop()
        print(my_set)
    my_set.clear()
    print("************************************************************************************")

    #Casting lists
    my_list = randomList()
    my_set = set(my_list)
    print(f'Casting of a list into a set') 
    print(f'List: {my_list}')
    print(f'Set(List): {my_set}')
    print("************************************************************************************")

    #Remove elements "Discard"
    random_number= randomNumber()
    my_set = randomSet()
    print(f'Discard element: {random_number} of the set: {my_set}') 
    print("Implementing Discard. If the element is not in the set the discard() method won't do anything to the set.")
    my_set.discard(random_number)
    print(my_set)
    print("************************************************************************************")

    #Remove elements "Remove"
    random_number= randomNumber()
    my_set = randomSet()
    print(f'Remove element: {random_number} of the set: {my_set}') 
    print("Implementing Remove. If the element is not present it will raise an exception.")
    my_set.remove(random_number)
    print(my_set)
    print("************************************************************************************")

    # Add elements "Add"
    random_number= randomNumber()
    my_set = randomSet()
    print(f'Add element: {random_number} to the set: {my_set}') 
    print("Implementing Add. If the element is already in the set the add() method won't duplicate the element.")
    my_set.add(random_number)
    print(my_set)
    print("************************************************************************************")

    # Add elements "update"
    random_list= randomList()
    my_set = randomSet()
    print(f'The list: {random_list}') 
    print(f'The set: {my_set}') 
    print("Implementing update. The method update() will include the elements that are not in the set")
    my_set.update(random_list)
    print(f'The set updated with the list: {my_set}')
    print("************************************************************************************")

if __name__ == "__main__":
    run()
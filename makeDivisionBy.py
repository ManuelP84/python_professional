def makeDivisionBy(divisor: int):
    """This closure returns a function that returns the division of an x number by n
    """
    def divide(dividend: int)->int:
        return dividend/divisor
    return divide

def run():

    divisionBy3 = makeDivisionBy(3)
    divisionBy5 = makeDivisionBy(5)
    divisionBy18 = makeDivisionBy(18)

    print(divisionBy3(18))
    print(divisionBy5(100))
    print(divisionBy18(54))

if __name__ == "__main__":
    run()







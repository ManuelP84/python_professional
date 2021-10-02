#Closure exercise

def multiplier(number: int):
    
    def stringMultiplier(string: str) -> str:

        newString = string*number
        return newString
    return stringMultiplier


def run():
    stringMult1 = multiplier(24)
    stringMult2 = multiplier(24)
    stringMult3 = multiplier(24)
    stringMult4 = multiplier(24)

    print(stringMult1("*"))
    print(stringMult2("/"))
    print("******HOLA MUNDO********")
    print(stringMult3("/"))
    print(stringMult4("*"))

if __name__ == "__main__":
    run()

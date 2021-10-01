
def is_palindrome(string: str) ->bool:
    string = string.replace(" ", "").lower()
    if string == string[::-1]:
        return True
    return False

def run():
    string = input("Please entre ther word: ")
    is_pal=is_palindrome(string)
    if is_pal:
        print(f'The word "{string}" is a palindrome.')
    else: print(f'The word "{string}" is NOT a palindrome.')

if __name__=="__main__":
    run()
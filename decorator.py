
def with_custom_message(string: str):
    def with_message(function):
        print(f'******{string}*******')
        def wrapper(*args,**kwargs):
            print('*'*53)
            function(*args,**kwargs)
            print('*'*53)
        return wrapper
    return with_message


message = "Welcome to your data adquisition system."
@with_custom_message(message)
def request_information():
    name = input("Please enter your name: ")   
    email = input("Please enter your email: ")   
    company = input("Please enter your company name: ")

def run():
    request_information()
    

if __name__ == "__main__":
    run()

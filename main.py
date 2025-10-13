def main():
    print (greet())
    print (bye())

def upper(func):
    def wrapper():
        return func().upper()
    return wrapper

@upper
def greet():
    return 'Hello!'

@upper
def bye():
    return 'bye!'

if __name__ == "__main__":
    main()
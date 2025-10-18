class Flask:
    def __init__(self):
        self.routes = {}
    
    def route(self, m, r):
        def wrapper(func):
            self.routes[m] = {r :  func} 
        return wrapper 
    
app = Flask()

@app.route("GET", "/products")
def get_products():
    print("Hello")

@app.route("POST", "/categories")
def post_categories():
    print("Bye")

def main():
    get_products = app.routes["GET"]['/products']
    get_products()

    post_categories = app.routes["POST"]['/categories']
    post_categories()

if __name__=="__main__":
    main()
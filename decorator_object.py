class Flask:
    def __init__(self):
        self.routes = {}
    
    def route(self, r, m):
        def wrapper(func):
            self.routes[r] = {m :  func} 
        return wrapper 
    
app = Flask()

@app.route("/products", "GET")
def get_products():
    print("Hello")

@app.route("/categories", "POST")
def post_categories():
    print("Bye")

def main():
    get_products = app.routes['/products']["GET"]
    get_products()

    post_categories = app.routes ['/categories']["POST"]
    post_categories()

if __name__=="__main__":
    main()
class Flask:
    def __init__(self):
        self.routes = {}
    
    def route(self, r):
        def wrapper(func):
            self.routes[r] = func 
        return wrapper 
    
app = Flask()

@app.route("/products")
def get_products():
    print("Hello")

def main():
    print(app.routes)
    get_products = app.routes['/products']
    get_products()

if __name__=="__main__":
    main()
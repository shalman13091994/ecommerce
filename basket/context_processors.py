from .basket import Basket

# add context_processor under template so these will reflect in all pages
# A context processor is a Python function that takes the request object as an argument and returns a dictionary that gets added to the request context. 
# They come in handy when you need to make something available globally to all templates.
# from basket class

def basket(request):
    return {
        'basket':Basket(request)
        }

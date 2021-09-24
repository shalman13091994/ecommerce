from .basket import Basket

def basket(request):

    # we passing the request data into the class basket from basket.py and we can utilise n we need the information from it
    return {'basket' : Basket(request)} #from the basket class
    # we hve to create contentprocessor this in settings
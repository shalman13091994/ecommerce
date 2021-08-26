from decimal import Decimal

from store.models import Product


class Basket():
    """
    A base Basket class, providing some default behaviors that
    can be inherited or overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, qty):
        """
        Adding and updating the users basket session data
        """
        # product= product_id, qty=product_qty from views
        product_id = str(product.id)
        # fetching the product id and add the qty = qty(product_qty from views)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        else:
            self.basket[product_id] = {'price': str(product.price), 'qty': qty}
            
        # self.session.modified = True
        self.save()


    # TypeError: 'Basket' object is not iterable
    def __iter__(self):
        """
        collect the product_id in the session data to query the datbase and return the products
        """
        product_ids = self.basket.keys()
        # products is product manager from model
        products = Product.products.filter(id__in = product_ids)
        # copy of the last session data - sum of the totalproduct in the basket0
        basket = self.basket.copy()

        for product in products:
# select the product the id in the basket and add the additional data to product (['product']) 
# and include the data to the product
            basket[str(product.id)]['product'] = product
        
        # calculating the price
        for item in basket.values():
            item['price'] = Decimal(item["price"])
            item['total_price'] = item['price'] * item['qty']
            yield item        

# find no.of items in the partcular ex: 4 quantities of python book 
    def __len__(self):
        """
        Get the basket data and count the qty of items
        """
        return sum(item['qty'] for item in self.basket.values())

# find no.of items in the partcular and calculate the price for each as total ex: 4 quantities of python book * price for each 

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())
    

    def update(self, product, qty):
        """
        update values in session data
        """
      # product= product_id, qty=product_qty from views
        product_id = str(product)
        qty = qty 
    # fetching the product id and add the qty = qty(product_qty from views)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        self.save()


    def delete(self, product):
        """
        Delete item from session data
        """
        product_id = str(product)

        if product_id in self.basket:
            del self.basket[product_id]
            print(product_id)
        self.save()

    def save(self):
        self.session.modified = True



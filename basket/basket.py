from decimal import Decimal

from store.models import Product


class Basket:
    """
    A base Basket class, providing some default behaviors that
    can be inherited or overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get("skey")
        if "skey" not in request.session:
            basket = self.session["skey"] = {}
        self.basket = basket

    def add(self, product, qty):
        """
        Adding and updating the users basket session data
        """
        # product= product_id, qty=product_qty from views
        product_id = str(product.id)
        if product_id in self.basket:
            self.basket[product_id]["qty"] = qty
        else:
            self.basket[product_id] = {"price": str(product.regular_price), "qty": qty}

        self.save()

    def __iter__(self):
        """
        Collect the product_id in the session data to query the database
        and return products
        """
        product_ids = self.basket.keys()
        # products is product manager from model
        # products = Product.products.filter(id__in=product_ids)
        products = Product.objects.filter(id__in=product_ids)
        # copy of the last session data - sum of the totalproduct in the basket
        basket = self.basket.copy()

        # select the product the id in the basket and add the additional data to product (['product'])
        # and include the data to the product
        for product in products:
            basket[str(product.id)]["product"] = product

        for item in basket.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["qty"]
            yield item

    # find no.of items in the partcular ex: 4 quantities of python book
    def __len__(self):
        """
        Get the basket data and count the qty of items
        """
        return sum(item["qty"] for item in self.basket.values())

    # find no.of items in the partcular and calculate the price for each as total ex: 4 quantities of python book * price for each
    def get_total_price(self):
        subtotal = sum(Decimal(item["price"]) * item["qty"] for item in self.basket.values())

        if subtotal == 0:
            shipping = Decimal(0.00)
        else:
            shipping = Decimal(11.50)
        total = subtotal + Decimal(shipping)
        return total

    def update(self, product, qty):
        """
        Update values in session data
        """
        # product= product_id, qty=product_qty from views
        product_id = str(product)

        if product_id in self.basket:
            # fetching the product id and add the qty = qty(product_qty from views)
            self.basket[product_id]["qty"] = qty
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

    def clear(self):
        # remove basket from session

        del self.session["skey"]
        # del self.session[setttings.BASKET_SESSION_ID]
        self.save

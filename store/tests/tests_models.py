from django.test import TestCase
from store.models import Category, Product
from django.contrib.auth.models import User

#copy the db.sqlite and create and make it as .coverage database where our testing case will run 

class TestCategoriesModel(TestCase):

#providing the data here rather than checking in the localhost 
    def setUp(self):
        self.data1 = Category.objects.create(name = 'django', slug='django')

    def test_category_model_entry(self):
        """
         Test Category model data insertion/types/field attributes    
          
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))


    def test_category_model_entry(self):
        """ 
        test category model default name def __str__ testing this
        """
        #it should return name = 'django'
        data = self.data1
        self.assertTrue(str(data), 'django')


class TestProductModel(TestCase):

    def setUp(self):
        Category.objects.create(name = 'django', slug='django')
        User.objects.create(username ='admin')
        self.data1 = Product.objects.create(category_id =1, title ='django beginners', slug='django-beginners',
                     price='12.05', created_by_id =1, image ='django')

    def test_product_model_entry(self):
        """
         Test product model data insertion/types/field attributes    
         Test product model default name def __str__ testing this
          
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        #it should return title ='django beginners' 
        self.assertEqual(str(data), 'django beginners')
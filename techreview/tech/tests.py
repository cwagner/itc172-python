from django.test import TestCase
from .models import Product, ProductType
from .forms import ProductForm
from django.urls import reverse

# Create your tests here.
class ProductTest(TestCase):
    def test_stringOutput(self):
        product = Product(productname='Lenovo laptop')
        self.assertEqual(str(product), product.productname)

    def test_tableName(self):
        self.assertEqual(str(Product._meta.db_table), 'product')

#testing a view
class TestIndex(TestCase):
    def test_viewUrlAccessibleByName(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_viewUsesCorrectTemplate(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'tech/index.html')

class NewProductFormTest(TestCase):
    # valid form data
    def test_product_form_is_valid(self):
        form = ProductForm(data={'productname': 'Lenovo laptop', 'producttype': 'laptop', 'user': 'carissawagner', 'productentrydate': '2019-02-22', 'productdescription': 'Laptop, fairly decent, has a good keyboard'})
        self.assertTrue(form.is_valid)

    def test_product_form_is_invalid(self):
        form = ProductForm(data={})
        self.assertTrue(form.is_valid)

from django.test import TestCase
from .models import Product, ProductType
from .forms import ProductForm
from django.urls import reverse
from django.contrib.auth.models import User

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
        tech_type = ProductType.objects.create(typename='laptop')
        user = User.objects.create(username='carissawagner')
        form = ProductForm(data={'productname': 'Lenovo laptop', 'producttype': tech_type.pk, 'user': user.pk, 'productentrydate': '2019-02-22', 'producturl': 'http://www.microsoft.com', 'productdescription': 'Laptop, fairly decent, has a good keyboard'})
        self.assertTrue(form.is_valid())

    def test_product_form_is_invalid(self):
        form = ProductForm(data={'producttype': 'laptop', 'user': 'carissawagner', 'productentrydate': 'invalid date', 'productdescription': 'Laptop, fairly decent, has a good keyboard'})
        self.assertFalse(form.is_valid())

class GetProductTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/tech/products')
        self.assertTrue(200 <= response.status_code)
        self.assertTrue(response.status_code < 400)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('getproducts'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('getproducts'))
        self.assertTemplateUsed(response, 'tech/products.html')

        

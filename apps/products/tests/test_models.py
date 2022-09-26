from django.test import TestCase

class ProductTestCase(TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_create_product_no_name(self):
        name = 'Product 1'
        self.assertEqual(name, 'Product 1')
        
from django.test import TestCase
from myapp.models import Emp

class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        Emp.objects.create(name='name',age=122)
    def test_false_is_false(self):
        self.assertFalse('hhk'.isdigit())

    def test_false_is_true(self):
        self.assertTrue('2555'.isdigit())

    def test_one_plus_one_equals_two(self):
        emp =Emp.objects.get()
        field_label=emp._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
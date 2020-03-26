from django.test import TestCase
from waitlist.models import Waitlist


# Create your tests here.
class WaitlistModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all tests methods
        Waitlist.objects.create(id=1, guests =5, lastname = 'ece', catagory = 'customer')

    def test_id_label(self):
        waitlist = Waitlist.objects.get(id=1)
        field_label = waitlist._meta.get_field('id').verbose_name
        self.assertEquals(field_label, 'id')

    def test_guests_label(self):
        waitlist = Waitlist.objects.get(id=1)
        field_label = waitlist._meta.get_field('guests').verbose_name
        self.assertEquals(field_label, 'guests')

    def test_lastname_label(self):
        waitlist = Waitlist.objects.get(id=1)
        field_label = waitlist._meta.get_field('lastname').verbose_name
        self.assertEquals(field_label, 'lastname')


    def test_name_max_length(self):
        waitlist = Waitlist.objects.get(id=1)
        max_length = waitlist._meta.get_field("lastname").max_length
        self.assertEquals(max_length, 128)

    def test_catagory_label(self):
        waitlist = Waitlist.objects.get(id=1)
        field_label = waitlist._meta.get_field('catagory').verbose_name
        self.assertEquals(field_label, 'catagory')

    def test_catagory_max_length(self):
        waitlist = Waitlist.objects.get(id=1)
        max_length = waitlist._meta.get_field("catagory").max_length
        self.assertEquals(max_length, 64)

    def test_object_name_is_name(self):
        waitlist = Waitlist.objects.get(id=1)
        expected_object_name = f"{waitlist.id}"
        self.assertEquals(expected_object_name, str(waitlist))

from django.test import TestCase
from reservation.models import Table
from reservation.models import Reservation


# Create your tests here.
class TableModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Table.objects.create(table_id=2, cap=5, occupied=False)

    def test_table_id_label(self):
        table = Table.objects.get(id=1)
        field_label = table._meta.get_field('table_id').verbose_name
        self.assertEquals(field_label, 'table_id')

    def test_cap_label(self):
        table = Table.objects.get(id=1)
        field_label = table._meta.get_field('cap').verbose_name
        self.assertEquals(field_label, 'cap')

    def test_occupied_label(self):
        table = Table.objects.get(id=1)
        field_label = table._meta.get_field('occupied').verbose_name
        self.assertEquals(field_label, 'occupied')

    def test_object_name_is_name(self):
        table = Table.objects.get(id=1)
        expected_object_name = f"{table.table_id}"
        self.assertEquals(expected_object_name, str(table))


class ReservationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Reservation.objects.create(rsv_number = 1, table_id = 1, no_of_guests = 3, user='ece651', date='2020-5-2')

    def test_rsv_number_label(self):
        rsv = Reservation.objects.get(id=1)
        field_label = rsv._meta.get_field('rsv_number').verbose_name
        self.assertEquals(field_label, 'rsv_number')

    def test_table_id_label(self):
        rsv = Reservation.objects.get(id=1)
        field_label = rsv._meta.get_field('table_id').verbose_name
        self.assertEquals(field_label, 'table_id')

    def test_no_of_guests_label(self):
        rsv = Reservation.objects.get(id=1)
        field_label = rsv._meta.get_field('no_of_guests').verbose_name
        self.assertEquals(field_label, 'no_of_guests')

    def test_user_label(self):
        rsv = Reservation.objects.get(id=1)
        field_label = rsv._meta.get_field('user').verbose_name
        self.assertEquals(field_label, 'user')

    def test_date_label(self):
        rsv = Reservation.objects.get(id=1)
        field_label = rsv._meta.get_field('date').verbose_name
        self.assertEquals(field_label, 'date')

    def test_object_name_is_name(self):
        rsv = Reservation.objects.get(id=1)
        expected_object_name = f"{rsv.rsv_number}"
        self.assertEquals(expected_object_name, str(rsv))
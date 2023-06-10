from odoo.tests.common import HttpCase, tagged, TransactionCase

# This test should only be executed after all modules have been installed.
@tagged('-at_install', 'post_install')
class TestMaterialSupplier(TransactionCase):
    def test_create_supplier(self):
        supplier = self.env['material.supplier'].create({
            'name': 'A new supplier',
            'address': 'Near My Home',
            'phone': '123123'
        })
        self.assertEqual(supplier.name, "A new supplier")
        self.assertEqual(supplier.address, "Near My Home")
        self.assertEqual(supplier.phone, "123123")
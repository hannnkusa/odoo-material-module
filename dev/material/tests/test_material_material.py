from odoo.tests.common import HttpCase, tagged, TransactionCase


# This test should only be executed after all modules have been installed.
@tagged('-at_install', 'post_install')
class TestMaterialMaterial(TransactionCase):
    def test_create_material_without_supplier(self):
        """
        Test creating a material without supplier
        """
        material = self.env['material.material'].create({
            'code': 'M00100',
            'name': 'A new material',
            'type': 'fabric',
            'buy_price': 10000
        })
        self.assertEqual(material.code, "M00100")
        self.assertEqual(material.name, "A new material")
        self.assertEqual(material.type, "fabric")
        self.assertEqual(material.buy_price, "10000")

    def test_create_material_with_supplier(self):
        """
            Test creating a material with supplier
        """
        # Create Supplier
        supplier = self.env['material.supplier'].create({
            'name': 'A new supplier',
            'address': 'Near My Home',
            'phone': '123123'
        })
        # Create Material with relation onto supplier
        material = self.env['material.material'].create({
            'code': 'M00100',
            'name': 'A new material',
            'type': 'fabric',
            'buy_price': 10000,
            'supplier_id': supplier.id
        })
        self.assertEqual(material.code, "M00100")
        self.assertEqual(material.name, "A new material")
        self.assertEqual(material.type, "fabric")
        self.assertEqual(material.buy_price, "10000")
        self.assertEqual(material.supplier_id, supplier.id)

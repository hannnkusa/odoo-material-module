from odoo import api, fields, models, _
class MaterialSupplier(models.Model):
    _name = "material.supplier"
    _inherit = "mail.thread"
    _description = "Supplier Records"

    ref = fields.Char(string="Reference", default=lambda self: _('New'))
    name = fields.Char(string="Name", required=True, tracking=True)
    address = fields.Char(string="Address", required=True, tracking=True)
    phone = fields.Char(string="Phone Number", required=True, tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('material.supplier')
        return super(MaterialSupplier, self).create(vals_list)
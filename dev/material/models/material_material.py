from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class MaterialMaterial(models.Model):
    _name = "material.material"
    _inherit = "mail.thread"
    _description = "Material Records"

    code = fields.Char(string='Code', default=lambda self: _('New'))
    name = fields.Char(string='Name', required=True, tracking=True)
    type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton'),
    ], string='Type', required=True, tracking=True)
    buy_price = fields.Integer(string='Buy Price', required=True, tracking=True)
    supplier_id = fields.Many2one('material.supplier', string='Supplier', required=True, tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['code'] = self.env['ir.sequence'].next_by_code('material.material')
        return super(MaterialMaterial, self).create(vals_list)
    @api.constrains('buy_price')
    def _check_buy_price(self):
        for rec in self:
            if rec.buy_price < 100:
                raise ValidationError(_("The Material Buy Price Should Not Be Below 100!"))

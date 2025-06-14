from odoo import models, fields

class DefectLog(models.Model):
    _name = 'manufacturing.defect.log'
    _description = 'Manufacturing Defect Log'

    date = fields.Datetime(string='Date', default=fields.Datetime.now)
    production_id = fields.Many2one('mrp.production', string='Production Order')
    lot_id = fields.Many2one('stock.lot', string='Lot')
    custom_lot = fields.Char(string='Custom Lot')
    qty = fields.Float(string='Quantity')
    weight = fields.Float(string='Weight')
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    ], default='new', string='Status')
    reason = fields.Text(string='Reason')
    operator_id = fields.Many2one('res.users', string='Operator', default=lambda self: self.env.user)

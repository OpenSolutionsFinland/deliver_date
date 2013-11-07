from osv import osv, fields

class delivery_date_order(osv.osv):
    _name='sale.order.line'
    _inherit='sale.order.line'
    
    _columns = {
        'delivery_date': fields.char('Deliver', size=64, required=False, translate=True),
    }
    
delivery_date_order()
from osv import osv, fields

class delivery_date(osv.osv):
    _name='sale.order.line'
    _inherit='sale.order.line'
    
    columns = {
        'delivery_date': fields.date('Delivery date'),
    }
    
delivery_date()
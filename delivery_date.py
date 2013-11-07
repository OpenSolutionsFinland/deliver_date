from osv import osv, fields

class delivery_date_order(osv.osv):
    _name='sale.order'
    _inherit='sale.order'
    
    columns = {
        'delivery_date': fields.date('Delivery date'),
    }
    
delivery_date_order()
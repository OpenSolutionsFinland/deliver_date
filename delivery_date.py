from osv import osv, fields

class delivery_date(osv.osv_memory):
    _name='sale.order.line'
    _inherit='sale.order.line'
    
    columns = {
        'delivery_date': fields.date('Delivery date'),
    }
    
delivery_date()

class delivery_date_order(osv.osv_memory):
    _name='sale.order'
    _inherit='sale.order'
    
    columns = {
        'delivery_date': fields.date('Delivery date'),
    }
    
delivery_date_order()
from osv import osv, fields
from datetime import datetime, date, time, timedelta

class delivery_date_order(osv.osv):
    _name='sale.order.line'
    _inherit='sale.order.line'
    
    def _get_delivery_date(self, cr, uid, name, context=None):
        deliveryDate = date.today()
        line = self.browse(cr, uid, [], context)
        if line:
            deliveryDate = date.today() - timedelta(line.delay, 0, 0)
        return deliveryDate.isoformat()
        
    _columns = {
        'delivery_date': fields.date('Delivery date')
    }
    
    _defaults = {
        'delivery_date':  lambda self, cr, uid, ctx: self._get_delivery_date(cr,uid,'sale.order.line', ctx),
    }
    
delivery_date_order()
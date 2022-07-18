from odoo import models


class StockMove(models.Model):
    _inherit = "stock.move"

    def _get_new_picking_values(self):
        vals = super()._get_new_picking_values()
        group_carrier = self.mapped("group_id.carrier_id")
        if group_carrier:
            vals["carrier_id"] = group_carrier.id
        return vals

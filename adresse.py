# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class DeliveryAdresse(models.AbstractModel):
    _inherit = 'account.move'
    descreption = 

    delivery_adress = fields.One2many('res.partner', string="Delivery Address", compute='_compute_address_type')
    name = fields.Char(string="name", required= True)

    @api.depends('partner_id.child_ids')
    def _compute_address_type(self):
        for res in self:
            self.delivery_adress = res.partner_id.child_ids.filtered(lambda x: x.type == 'delivery')

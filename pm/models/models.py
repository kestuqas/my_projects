# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pm(models.Model):
    _name = 'pm.pm'

    @api.depends('price', 'qty')
    def _calculate_value(self):
        self.value = self.price * self.qty
        return self.value

    @api.one
    def _my_currency(self):
        self.my_currency = 'EUR'
        return self.my_currency

    @api.one
    def _check_exchange(self):
        # TODO: do real check of exchange rate
        self.exchange_rate = float(0.8)
        return self.exchange_rate

    @api.one
    def _recalculate_value(self):
        if self.currency != self.my_currency:
            self.calculated = self.value * self.exchange_rate
        return self.calculated

    name = fields.Char(string='ID', required=True)
    customer = fields.Char()
    qty = fields.Integer(string='QTY')
    uom = fields.Char(string='UOM')
    price = fields.Float()
    value = fields.Float(compute='_calculate_value', store=True)
    currency = fields.Char()
    my_currency = fields.Char(compute='_my_currency', string='My Curr.')
    exchange_rate = fields.Float(compute='_check_exchange', store=True)
    calculated = fields.Float(compute='_recalculate_value', store=True)
    description = fields.Text()
    date = fields.Char()
    deadline = fields.Char()





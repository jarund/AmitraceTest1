# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.depends('order_line', 'order_line.bid_amount')
    def _compute_bid_diff(self):
        for rec in self:
            if any([line.bid_amount for line in rec.order_line]):
                rec.bid_diff = sum([line.bid_amount for line in rec.order_line]) - \
                               sum([line.price_subtotal for line in rec.order_line])
                rec.is_bid_diff = True
            else:
                rec.is_bid_diff = False
                rec.bid_diff = 0.0

    is_bid_diff = fields.Boolean(compute='_compute_bid_diff', string='Bid Diff?')
    bid_diff = fields.Monetary(compute='_compute_bid_diff', string='Bid Diff')


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    bid_amount = fields.Monetary(string="Bid", default=0)

    def _prepare_invoice_line(self, **optional_values):
        res = super(SaleOrderLine, self)._prepare_invoice_line()
        res.update({
            'bid_amount': self.bid_amount
        })
        return res

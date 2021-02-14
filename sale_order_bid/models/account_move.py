# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class AccountMove(models.Model):
    _inherit = "account.move"

    @api.depends('invoice_line_ids', 'invoice_line_ids.bid_amount')
    def _compute_bid_diff(self):
        for rec in self:
            if any([line.bid_amount for line in rec.invoice_line_ids]):
                rec.bid_diff = sum([(line.bid_amount * line.quantity) for line in rec.invoice_line_ids]) - \
                               sum([line.price_subtotal for line in rec.invoice_line_ids])
                rec.is_bid_diff = True
            else:
                rec.is_bid_diff = False
                rec.bid_diff = 0.0

    is_bid_diff = fields.Boolean(compute='_compute_bid_diff', string='Bid Diff?')
    bid_diff = fields.Monetary(compute='_compute_bid_diff', string='Bid Diff')


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    bid_amount = fields.Monetary(string="Bid")

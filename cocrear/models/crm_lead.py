# -*- coding: utf-8 -*-
from odoo import models, fields, api

class WhatsAppMessage(models.Model):
    _inherit = 'whatsapp.message'
    lead_id = fields.Many2one('crm.lead', string='Lead', compute='_compute_lead_id')

    def _compute_lead_id(self):
        for record in self:
            lead = False
            if record.mail_message_id.model == 'crm.lead':
                lead = self.env['crm.lead'].browse(record.mail_message_id.res_id)
            elif record.mail_message_id.model == 'sale.order':
                sale_order = self.env['sale.order'].browse(record.mail_message_id.res_id)
                if sale_order and sale_order.opportunity_id:
                    lead = sale_order.opportunity_id

            record.lead_id = lead

class CrmLead(models.Model):
    _inherit = "crm.lead"
    whatsapp_history = fields.One2many('whatsapp.message', 'lead_id', string='Historial de WhatsApp')

# -*- coding: utf-8 -*-

from odoo import models, fields, api

AVAILABLE_CHANNELS = [
    ('sosafe', 'SOSAFE'),
    ('telefono', 'Teléfono'),
    ('radial', 'Radial'),
    ('camaras', 'Cámaras')
]

class SecurityProcedureTypeCategory(models.Model):
    _name = 'nunoasegura.security.procedure.type.category'

    name = fields.Char(string="Nombre")

class SecurityProcedureType(models.Model):
    _name = 'nunoasegura.security.procedure.type'

    name = fields.Char(string="Nombre")
    category = fields.Many2one('nunoasegura.security.procedure.type.category', string="Categoría")
    
    
class SecurityProcedure(models.Model):
    _name = 'nunoasegura.security.procedure'
    _inherit = ['tickets.ticket', 'tickets.geoplace']

    channel = fields.Selection(AVAILABLE_CHANNELS, string="Canal")
    type = fields.Many2one('nunoasegura.security.procedure.type', string='Tipo')






# class nunoasegura(models.Model):
#     _name = 'nunoasegura.nunoasegura'
#     _description = 'nunoasegura.nunoasegura'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

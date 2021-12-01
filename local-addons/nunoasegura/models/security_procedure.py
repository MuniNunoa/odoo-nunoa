# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

logging.basicConfig(format='[%(asctime)s] - %(name)s - %(funcName)s - %(levelname)s : %(message)s', level=logging.INFO)
log = logging.getLogger(__name__)

AVAILABLE_CHANNELS = [
    ('sosafe', 'SOSAFE'),
    ('telefono', 'Teléfono'),
    ('radial', 'Radial'),
    ('camaras', 'Cámaras'),
    ('plan-barrial', 'Plan Barrial')
]

class SecurityProcedureTypeCategory(models.Model):
    _name = 'nunoasegura.security.procedure.type.category'

    name = fields.Char(string="Nombre")
    types = fields.One2many('nunoasegura.security.procedure.type', 'category', string="Tipos")
    # types = fields.One2many('nunoasegura.security.procedure.type', string="Tipos")


class SecurityProcedureType(models.Model):
    _name = 'nunoasegura.security.procedure.type'

    name = fields.Char(string="Nombre")
    category = fields.Many2one('nunoasegura.security.procedure.type.category', string="Categoría")

class Patrol(models.Model):
    _name = 'nunoasegura.patrol'

    name = fields.Char(string="Nombre")
    
class SecurityProcedure(models.Model):
    _name = 'nunoasegura.security.procedure'
    _inherit = ['tickets.ticket', 'tickets.geoplace', 'mail.thread']

    channel = fields.Selection(AVAILABLE_CHANNELS, string="Canal")
    type = fields.Many2one('nunoasegura.security.procedure.type', string='Tipo')
    operator = fields.Many2one('res.users', string="Operador", default=lambda self: self.env.user, readonly=True)
    neighborhood_plan = fields.Many2one('nunoasegura.neighborhood.plan', string="Plan Barrial")
    # inspectors = fields.Many2many('res.users', string='Inspectores')
    inspectors = fields.Many2many('res.users', string='Inspectores', 
        domain=lambda self: [("groups_id", "=", self.env.ref("nunoasegura.inspector_group").id)])
    patrols = fields.Many2many('nunoasegura.patrol', string="Patrullas")
    outcome = fields.Text("Resultado")

    inspector_assigned_at = fields.Datetime("Asignación de inspector", readonly=True)
    inspector_arrival_at = fields.Datetime("Llegada al lugar", readonly=True)
    
    @api.model
    def create(self, data):
        return super(SecurityProcedure, self.with_context(tracking_disable=True)).create(data)

    @api.onchange('inspectors', 'patrols')
    def set_inspector_assigned_at(self):
        if (not self.inspector_assigned_at) and (self.inspectors or self.patrols):
            for record in self:
                record.inspector_assigned_at = fields.Datetime.now()
            
    
    # def reset_geolocation(self):
    #     return super().reset_geolocation()


    def mark_inspector_arrival(self):
        self.inspector_arrival_at = fields.Datetime.now()

        # hora de creación
        # hora de asignacion
        # hora de llegada
        # hora de cierre

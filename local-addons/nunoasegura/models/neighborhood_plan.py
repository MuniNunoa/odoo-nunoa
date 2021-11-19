# -*- coding: utf-8 -*-

from odoo import models, fields, api

AVAILABLE_SOURCES = [
    ('comunit-norte', 'Comunit. Norte'),
    ('comunit-oriente', 'Comunit. Oriente'),
    ('comunit-poniente', 'Comunit. Poniente'),
    ('coord-comunit', 'Coord. Comunitario'),
    ('dpto-innovacion', 'Dpto. Innovación'),
    ('jefe-operativo', 'Jefe Operativo'),
    ('director', 'Director')
]

AVAILABLE_TEAMS = [
    ('comunitario', 'Comunitario'),
    ('emergencias', 'Emergencias'),
    ('innovacion', 'Innovación'),
    ('obras', 'Obras'),
    ('operativo', 'Operativo'),
]

WEEKDAYS = [
    ('1', 'Lunes'),
    ('2', 'Martes'),
    ('3', 'Miércoles'),
    ('4', 'Jueves'),
    ('5', 'Viernes'),
    ('6', 'Sábado'),
    ('7', 'Domingo')
]

INTERVENTION_TYPES = [
    "Vigilancia especial",
    "Fiscalización",
    "Mediación",
    "Asesoría/Charlas",
    "Patrullaje general",
    "Visita domiciliaria",
    "Poda",
    "Otros"
]
class NeighborhoodPlan(models.Model):
    _name = 'nunoasegura.neighborhood.plan'
    _inherit = ['tickets.ticket']

    request_source = fields.Selection(AVAILABLE_SOURCES, string="Fuente de requerimiento")
    responsible_team = fields.Selection(AVAILABLE_TEAMS, string="Equipo responsable")
    cuadrante = fields.Integer("Cuadrante")
    unidad_vecinal = fields.Integer("Unidad Vecinal")
    intervention_type = fields.Selection(list(zip(INTERVENTION_TYPES, INTERVENTION_TYPES)), string="Intervención requerida")

    weekday_start = fields.Selection(WEEKDAYS, string="Desde")
    weekday_end = fields.Selection(WEEKDAYS, string="Hasta")
    
    intervention_start = fields.Date("Inicio de intervención")
    intervention_end = fields.Date("Término de intervención")
    # intervention_duration = fields.Integer("Días de duración", compute="_compute_intervention_duration")

    # @api.depends('intervention_start', 'intervention_end')
    # def _compute_intervention_duration(self):
    #     pass


    

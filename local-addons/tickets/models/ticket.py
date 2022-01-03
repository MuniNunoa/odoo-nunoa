# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import utils

AVAILABLE_PRIORITIES = [
    ('0', 'No tiene'),
    ('1', 'Baja'),
    ('2', 'Normal'),
    ('3', 'Alta'),
]

AVAILABLE_STATES = [
    ('nuevo', 'Nuevo'),
    ('en-proceso', 'En proceso'),
    ('cerrado', 'Cerrado')
]

STREET_TYPES = [
    ("CALLE", "CALLE"),
    ("AVENIDA", "AVENIDA"),
    ("PASAJE", "PASAJE")
]

STREET_NAMES = utils.get_street_names()


class Ticket(models.Model):
    _name = 'tickets.ticket'
    _description = "Un ticket representa una solicitud que debe ser resuelta"

    description = fields.Text("Descripción")
    priority = fields.Selection(AVAILABLE_PRIORITIES, 'Prioridad', default='0')
    state = fields.Selection(AVAILABLE_STATES, 'Estado', default='nuevo', required=True)
    created_at = fields.Datetime("Fecha de creación", default=lambda s: fields.Datetime.now())
    closed_at = fields.Datetime("Fecha de cierre", readonly=True)
    deadline = fields.Date("Vencimiento")
    
    requester = fields.Many2one('res.partner', string="Solicitante")
    assigned_to = fields.Many2one('res.users', string='Asignado a')

    requester_name = fields.Char(related='requester.name', string="Nombre")
    requester_email = fields.Char(related='requester.email', string="Teléfono")
    requester_phone = fields.Char(related='requester.phone', string="Correo")


    def close(self):
        self.state = 'cerrado'
        self.closed_at = fields.Datetime.now()

class Street(models.Model):
    _name = 'tickets.street'
    _description = "Calles de Ñuñoa"

    type = fields.Char('Tipo')
    short_name = fields.Char("Calle")
    name = fields.Char(string='Nombre', compute="_compute_name", store=True)

    @api.depends('type', 'short_name')
    def _compute_name(self):
        for record in self:
            record.name = f"{record.type} {record.short_name}"


class GeoPlace(models.Model):
    _name = 'tickets.geoplace'
    _description = "Lugar georreferenciado"
    
    street = fields.Many2one('tickets.street', string="Calle")
    address_number = fields.Integer("Número")
    address_obs = fields.Char("Dpto/Block/Villa")
    latitude = fields.Float("Latitud", digits=(12, 6), readonly=True)
    longitude = fields.Float("Longitud",  digits=(12, 6), readonly=True)
    unidad_vecinal = fields.Char("Unidad Vecinal")
    cuadrante = fields.Char("Cuadrante")
    latlon = fields.Char("LatLon",  compute="_compute_latlon", readonly=True)

    @api.depends('latitude', 'longitude')
    def _compute_latlon(self):
        for record in self:
            record.latlon = f"{record.latitude},{record.longitude}" 

    def get_full_addresses(self):
        addresses = []
        full_address = f"{self.street.short_name} {self.address_number}, Ñuñoa, Chile"
        addresses.append(full_address)
        if self.street.type and (self.street.type != 'CALLE'):
            alternative_address = f"{self.street.type} {full_address}"
            addresses.append(alternative_address)
        # reversed_list = list(reversed(addresses))
        return list(reversed(addresses))
    
    def reset_geolocation(self):
        self.latitude = None
        self.longitude = None
        self.unidad_vecinal = None
        self.cuadrante = None

    @api.onchange('street', 'address_number')
    def onchange_address(self):
        if self.street and self.address_number:
            for address in self.get_full_addresses():
                lat_lon = utils.get_coordinates(address)
                if lat_lon:
                    self.latitude, self.longitude = lat_lon
                    self.unidad_vecinal = utils.get_uv(*lat_lon)
                    self.cuadrante = utils.get_cuadrante(*lat_lon)
                    return
        self.reset_geolocation()
    
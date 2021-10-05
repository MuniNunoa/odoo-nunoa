from re import I
from odoo import models, fields, api



class Sector(models.Model):
    _name = 'nunoatubarrio.sector'
    _description = 'Sector'
    
    nombre = fields.Char('Nombre')


class UnidadVecinal(models.Model):
    _name = 'nunoatubarrio.unidadvecinal'
    _description = 'Unidad Vecinal'

    numero = fields.Integer("N°")
    jjvv = fields.Char("JJVV")

class TipoProblema(models.Model):
    _name = 'nunoatubarrio.tipoproblema'
    _description = 'Clasificación de problema vecinal'

    nombre = fields.Char("Nombre")


class Problema(models.Model):
    _name = 'nunoatubarrio.problema'
    _description = 'Problema vecinal'

    unidad_vecinal = fields.Many2one("nunoatubarrio.unidadvecinal", string="Unidad Vecinal")
    
    fecha = fields.Date("Fecha", default=lambda s: fields.Date.today())
    descripcion = fields.Text("Descripción")
    direccion = fields.Char("Dirección")

    # lat = fields.Float("Latitud geográfica")
    # lon = fields.Float("Longitud geográfica")

    vecino_id = fields.Many2one("res.partner", string="Vecino", required=True)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'), 
        ('enproceso', 'En proceso'), 
        ('solucionado', 'Solucionado')], default='pendiente')

    solucion_id = fields.Many2one("nunoatubarrio.solucion", string="Solución")

    

class Solucion(models.Model):
    _name = 'nunoatubarrio.solucion'
    _description = 'Solución a un problema vecinal'

    direccion_responsable = fields.Char("Dirección Responsable")
    unidad_ejecutora = fields.Char("Unidad Ejecutora")
    descripcion = fields.Text()
    plazo = fields.Date("Plazo")
    gasto_estimado = fields.Integer("Gasto estimado")



# class nunoatubarrio(models.Model):
#     _name = 'nunoatubarrio.nunoatubarrio'
#     _description = 'nunoatubarrio.nunoatubarrio'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

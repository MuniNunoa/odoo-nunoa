# -*- coding: utf-8 -*-
# from odoo import http


# class Nunoasegura(http.Controller):
#     @http.route('/nunoasegura/nunoasegura/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nunoasegura/nunoasegura/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nunoasegura.listing', {
#             'root': '/nunoasegura/nunoasegura',
#             'objects': http.request.env['nunoasegura.nunoasegura'].search([]),
#         })

#     @http.route('/nunoasegura/nunoasegura/objects/<model("nunoasegura.nunoasegura"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nunoasegura.object', {
#             'object': obj
#         })

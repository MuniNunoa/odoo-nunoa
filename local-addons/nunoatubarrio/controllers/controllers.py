# -*- coding: utf-8 -*-
# from odoo import http


# class Nunoatubarrio(http.Controller):
#     @http.route('/nunoatubarrio/nunoatubarrio/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nunoatubarrio/nunoatubarrio/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nunoatubarrio.listing', {
#             'root': '/nunoatubarrio/nunoatubarrio',
#             'objects': http.request.env['nunoatubarrio.nunoatubarrio'].search([]),
#         })

#     @http.route('/nunoatubarrio/nunoatubarrio/objects/<model("nunoatubarrio.nunoatubarrio"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nunoatubarrio.object', {
#             'object': obj
#         })

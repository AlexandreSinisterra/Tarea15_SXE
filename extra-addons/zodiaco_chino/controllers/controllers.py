# -*- coding: utf-8 -*-
from odoo import http

# class MyModule(http.Controller):
#     @http.route('/zodiaco_chino/zodiaco_chino/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zodiaco_chino/zodiaco_chino/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('zodiaco_chino.listing', {
#             'root': '/zodiaco_chino/zodiaco_chino',
#             'objects': http.request.env['zodiaco_chino.zodiaco_chino'].search([]),
#         })

#     @http.route('/zodiaco_chino/zodiaco_chino/objects/<model("zodiaco_chino.zodiaco_chino"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zodiaco_chino.object', {
#             'object': obj
#         })
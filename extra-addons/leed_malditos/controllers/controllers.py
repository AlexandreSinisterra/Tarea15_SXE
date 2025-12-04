# -*- coding: utf-8 -*-
from odoo import http

# class MyModule(http.Controller):
#     @http.route('/leed_malditos/leed_malditos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/leed_malditos/leed_malditos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('leed_malditos.listing', {
#             'root': '/leed_malditos/leed_malditos',
#             'objects': http.request.env['leed_malditos.leed_malditos'].search([]),
#         })

#     @http.route('/leed_malditos/leed_malditos/objects/<model("leed_malditos.leed_malditos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('leed_malditos.object', {
#             'object': obj
#         })
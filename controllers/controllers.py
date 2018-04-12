# -*- coding: utf-8 -*-
from odoo import http

# class Citasfpg(http.Controller):
#     @http.route('/citasfpg/citasfpg/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/citasfpg/citasfpg/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('citasfpg.listing', {
#             'root': '/citasfpg/citasfpg',
#             'objects': http.request.env['citasfpg.citasfpg'].search([]),
#         })

#     @http.route('/citasfpg/citasfpg/objects/<model("citasfpg.citasfpg"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('citasfpg.object', {
#             'object': obj
#         })
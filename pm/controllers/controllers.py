# -*- coding: utf-8 -*-
from odoo import http

# class Pm(http.Controller):
#     @http.route('/pm/pm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pm/pm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pm.listing', {
#             'root': '/pm/pm',
#             'objects': http.request.env['pm.pm'].search([]),
#         })

#     @http.route('/pm/pm/objects/<model("pm.pm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pm.object', {
#             'object': obj
#         })
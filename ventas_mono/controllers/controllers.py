# -*- coding: utf-8 -*-
from odoo import http

# class VentasMono(http.Controller):
#     @http.route('/ventas_mono/ventas_mono/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ventas_mono/ventas_mono/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ventas_mono.listing', {
#             'root': '/ventas_mono/ventas_mono',
#             'objects': http.request.env['ventas_mono.ventas_mono'].search([]),
#         })

#     @http.route('/ventas_mono/ventas_mono/objects/<model("ventas_mono.ventas_mono"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ventas_mono.object', {
#             'object': obj
#         })
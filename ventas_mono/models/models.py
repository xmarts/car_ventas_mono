# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TiempoEntrega(models.Model):
	_name = "tiempo.entrega"

	name = fields.Char(string="Nombre")
	description = fields.Char(string="Descripción")
	cedis_selection = fields.Selection([('occidente','Cedis Occidente'),('centro','Cedis Centro'),('sur','Cedis Sur')],string='Cedis')

class Observaciones(models.Model):
	_name = "obser.sale"

	name = fields.Char(string="Nombre")
	description = fields.Text(string="Descripción de la observación")

	@api.multi
	def name_get(self):
		result = []
		for record in self:
			record_name = str(record.name) + ': ' + str(record.description)
			result.append((record.id, record_name))
		return result

class StockMoveInherit(models.Model):
	_inherit = "stock.move"

	tiempo_entrega_tabla = fields.Many2many('tiempo.entrega', string="Tiempo de entrega", related="sale_line_id.tiempo_entrega_tabla")
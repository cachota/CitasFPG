# -*- coding: utf-8 -*-

from odoo import models, fields, api

class citasfpg(models.Model):
	_name = 'citasfpg.citasfpg'
	_order = 'fechaVisual,orden desc'

     	autor = fields.Char(string="Autor", required=True)
     	cita = fields.Html(string="Cita")
	fechaVisual = fields.Date(string="Fecha de Visualizacion")
	orden = fields.Integer(string="Orden")

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

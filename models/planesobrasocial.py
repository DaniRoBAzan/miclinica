# -*- coding: utf-8 -*-

from odoo import models, fields, api,  _

class PlanesObraSocial(models.Model):
    _inherit="res.partner"
    _name = 'res.partner'
    name_plan = fields.Char(string="Nombre del Plan")
    description_plan = fields.Text(string="Detalle del Plan", help="Detalle de lo que cubre este plan.")
    plan_ids = fields.One2many('res.partner', 'parent_id', string='Child Tags')


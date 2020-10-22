# -*- coding: utf-8 -*-

from odoo import models, fields, api,  _

class ObraSociales(models.Model):
    _inherit = 'res.partner'
    _name = 'res.partner'
    _description ='modelo de Obras sociales '
    obra_social_id = fields.Many2one('res.partner', string='Parent Category', index=True, ondelete='cascade')
    plan_id = fields.One2many('res.partner', 'obra_social_id')
    name_plan = fields.Char(string="Nombre del Plan")
    description_plan = fields.Text(string="Detalle del Plan", help="Detalle de lo que cubre este plan.")
    # plans_ids = fields.One2many('miclinica.planesobrasocial', 'parent_id', string='Child Tags')
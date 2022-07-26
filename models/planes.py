# -*- coding: utf-8 -*-

from odoo import models, fields, api,  _

class Planes(models.Model):
    _name = 'miclinica.planes'
    _description ='modelo de Planes'
    _rec_name = 'nombre_plan'


    #-#CAMPOS
    nombre_plan = fields.Char(
        string="Nombre"
    )
    codigo_plan = fields.Char(
        string="Codigo"
    )
    descripcion_plan = fields.Text(
        string="Detalle", 
        help="Detalle del plan."
    )
    logo_plan = fields.Binary(
        string="Logo", 
        attachment=True
    )
    
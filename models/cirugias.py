# -*- coding: utf-8 -*-

from odoo import models, fields, api,  _

class Cirugias(models.Model):
    _name = 'miclinica.cirugias'
    _description ='modelo de Cirugias.'
    _rec_name = 'nombre'


    #-#CAMPOS
    nombre = fields.Char(
        string="Nombre"
    )
    codigo = fields.Char(
        string="Codigo"
    )
    
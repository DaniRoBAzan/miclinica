# -*- coding: utf-8 -*-

from odoo import models, fields, api,  _

class Enfermedades(models.Model):
    _name = 'miclinica.enfermedades'
    _description ='modelo de Enfermedades'
    _rec_name = 'nombre'


    #-#CAMPOS
    nombre = fields.Char(
        string="Nombre"
    )
    codigo = fields.Char(
        string="Codigo"
    )
    familia = fields.Char( #este debe ser m2o /ej: [2333]Ocular
        string="Familia"
    )
    origen = fields.Char(
        string="Origen"
    )
    notas = fields.Text(
        string="Notas"
    )

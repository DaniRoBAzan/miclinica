# -*- coding: utf-8 -*-

from odoo import models, fields, api,  _

class ObraSocial(models.Model):
    _name = 'miclinica.obrassociales'
    _description ='modelo de Obras sociales'
    _rec_name = 'nombre_obra_social'


    #-#CAMPOS
    nombre_obra_social = fields.Char(
        string="Nombre"
    )
    codigo_obra_social = fields.Char(
        string="Codigo"
    )
    descripcion_obra_social = fields.Text(
        string="Detalle", 
        help="Detalle de la obra social."
    )
    logo_obra_social = fields.Binary(
        string="Logo", 
        attachment=True
    )
    obrasocial_line_ids = fields.One2many('miclinica.obrassociales.line', 'obrasocial_ids', string='Linea Obra Social')


class ObraSocialLine(models.Model):
    _name = 'miclinica.obrassociales.line'
    _description ='Linea de Obras sociales'
    _rec_name = 'name'
            
    obrasocial_ids = fields.Many2one(
        'miclinica.obrassociales', 
        string='Obra Social'
    )
    planes_ids = fields.Many2one(
        'miclinica.planes',
        string='Planes'
    )
    name = fields.Char(
        string='Nombre',
        compute='_compute_name'
    )

    def _compute_name(self):
        for rec in self:
            rec.name = rec.obrasocial_ids.nombre_obra_social + " / " + rec.planes_ids.nombre_plan or False

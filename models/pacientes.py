# -*- coding: utf-8 -*-

from odoo import models, fields, api,  _
from datetime import datetime
from datetime import date

class Pacientes(models.Model):
    _inherit = 'res.partner'
    _name = 'res.partner'
    _description ='modelo de Pacientes'
    
    #-> FUNCIONES
    @api.depends('paciente_birthday')
    def _calcular_edad(self):
        for rec in self:
            if self.paciente_birthday:
                hoy = date.today()
                fechanacimiento = rec.paciente_birthday
                #primero restamos los años y luego  la comparación entre mes y día actual y mes y día de nacimiento. 
                edad = hoy.year - fechanacimiento.year - ((hoy.month, hoy.day) < (fechanacimiento.month, fechanacimiento.day))
                print("==> edad: ",edad)
                self.paciente_age = int(edad)
            else:
                self.paciente_age = 0

    @api.depends('paciente_age')
    def _setear_categoria_covid(self):
        for rec in self:
            if rec.paciente_age:
                if int(rec.paciente_age) > 60:
                    rec.paciente_category_covid = 'en riesgo'
                else:
                    rec.paciente_category_covid = 'sin riesgo'
            else:
                rec.paciente_category_covid = 'Edad sin informar'

    #-> CAMPOS
    #paciente_name = fields.Char(string="Nombre del Paciente")
    paciente_dni = fields.Char(string="DNI")
    paciente_birthday = fields.Date(string="Fecha Nacimiento")
    paciente_age = fields.Integer(string="Edad",compute="_calcular_edad", default=0, required=False)
    #paciente_number_phone = fields.Char(string="Numero Telefono")
    paciente_category_covid = fields.Char(string="Categoria Covid", compute="_setear_categoria_covid", default="-")

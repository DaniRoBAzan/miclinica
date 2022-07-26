# -*- coding: utf-8 -*-

from odoo import models, fields, api,  _
from datetime import datetime
from datetime import date

class Pacientes(models.Model):
    _inherit = 'res.partner'
    _name = 'res.partner'
    _description ='modelo de Pacientes'

    #-# CAMPOS
    paciente_dni = fields.Char(
        string="DNI"
    )
    paciente_birthday = fields.Date(
        string="Fecha Nacimiento"
    )
    paciente_age = fields.Integer(
        string="Edad",
        compute="_calcular_edad", 
        default=0, 
        required=False
    )
    paciente_category_covid = fields.Char(
        string="Categoria Covid", 
        compute="_setear_categoria_covid", 
        default="-", 
        help="La categoria se calcula automaticamente, teniendo en cuenta que la edad de 60 es riesgoso."
    )
    paciente_obrasocial_ids = fields.One2many('res.partner.obrassociales', 'paciente_ids', string='Obras Sociales')
    es_paciente = fields.Boolean(
        string="Es paciente",
        default=False, 
        help="Seleccionar en caso de que este contacto sera utilizado como paciente."
    )
    habitos_horas_semanas = fields.Integer(string='Horas / Semanas', default=0)
    habitos_cigarrillos_diarios = fields.Integer(string='Cant. Cigarrillos Diarios', default=0)
    habitos_bebe_alcohol = fields.Boolean(string='Bebe Alcohol', default=True)
    habitos_observaciones = fields.Text(string='Observaciones')
    examen_fisico = fields.Text(string='Examen Fisico')

    antecedentes_personales_ids = fields.One2many('miclinica.antecedentes.personales', 'paciente_ids', string='Antecedentes Personales')
    antecedentes_familiares_ids = fields.One2many('miclinica.antecedentes.familiares', 'paciente_ids', string='Antecedentes Familiares')
    cirugias_previas_ids = fields.One2many('miclinica.cirugias.personales', 'paciente_ids', string='Cirugias Previas')
    farmacos_ids = fields.One2many('miclinica.farmacos.personales', 'paciente_ids', string='Farmacos')



    #-# FUNCIONES
    @api.depends('paciente_birthday')
    def _calcular_edad(self):
        for rec in self:
            if self.paciente_birthday:
                hoy = date.today()
                fechanacimiento = rec.paciente_birthday
                #-#PRIMERO RESTAMOS LOS ANIOS Y LUEGO HACEMOS LA COMPARACION ENTRE MES-> DIA ACTUAL Y MES-> DIA DE NACIMIENTO 
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

class ObraSocialLine(models.Model):
    _name = 'res.partner.obrassociales'
    _description ='Obras Sociales de pacientes'

    paciente_ids = fields.Many2one(
        'res.partner', 
        string='Paciente'
    )
    obrasocial_line_ids = fields.Many2one(
        'miclinica.obrassociales.line', 
        string='Plan - Obra Social'
    )

class AntecedentesPersonales(models.Model):
    _name = 'miclinica.antecedentes.personales'
    _description ='Antecedentes Personales de pacientes'

    paciente_ids = fields.Many2one(
        'res.partner', 
        string='Paciente'
    )
    enfermedades_ids = fields.Many2one(
        'miclinica.enfermedades', 
        string='Enfermedades'
    )
    observaciones = fields.Text(string='Observaciones')

class AntecedentesFamiliares(models.Model):
    _name = 'miclinica.antecedentes.familiares'
    _description ='Antecedentes Familiares de pacientes'

    paciente_ids = fields.Many2one(
        'res.partner', 
        string='Paciente'
    )
    familiar = fields.Char(string='Familiar')
    enfermedades_ids = fields.Many2one(
        'miclinica.enfermedades', 
        string='Enfermedades'
    )
    observaciones = fields.Text(string='Observaciones')

class CirugiasPersonales(models.Model):
    _name = 'miclinica.cirugias.personales'
    _description ='Cirugias Personales de pacientes'

    paciente_ids = fields.Many2one(
        'res.partner', 
        string='Paciente'
    )
    cirugias_ids = fields.Many2one(
        'miclinica.cirugias', 
        string='Cirugias'
    )
    observaciones = fields.Text(string='Observaciones')

class FarmacosPersonales(models.Model):
    _name = 'miclinica.farmacos.personales'
    _description ='Farmacos Personales de pacientes'

    paciente_ids = fields.Many2one(
        'res.partner', 
        string='Paciente'
    )
    farmacos_ids = fields.Many2one(
        'product.template', 
        string='Farmacos'
    )
    observaciones = fields.Text(string='Observaciones')


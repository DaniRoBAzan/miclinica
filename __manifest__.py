# -*- coding: utf-8 -*-
{
    'name': 'Mi clinica',
    'version': '14.0.0.0.0',
    'category': 'Extra Tools',
    'summary': 'Modulo para sanatorios/clinicas/hospitales.',
    'author': 'Romina Bazan',
    'website':'https://www.linkedin.com/in/danielarominabazan/',
    'maintainer': 'Romina Bazan',
    'depends': [
        'base',
        'contacts', 
        'sale', 
        'account', 
        'calendar', 
    ],
    'data': [
        'views/planes_view.xml',
        'views/obrasociales_view.xml',
        'views/enfermedades_view.xml',
        'views/cirugias_view.xml',
        'views/pacientes_view.xml',
        'views/menu_view.xml',
        'report/report_partner_template.xml',
        'report/report_partner_view.xml',
        'security/ir.model.access.csv',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}

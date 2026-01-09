# -*- coding: utf-8 -*-
{
    'name': "hospital",

    'summary': """
        gestion de pacientes/medicos""",

    'description': """
        modulo que permitye la gestion de pacientes y medicos de un hospital y los diagnosticos.
    """,

    'author': "homer, dou",
    'website': "http://www.sivesestoinvitameauncafe.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/paciente_view.xml',
        'views/medico_view.xml',
        'views/diagnostico_view.xml',
        'views/menu_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
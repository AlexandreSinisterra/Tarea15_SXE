# -*- coding: utf-8 -*-
{
    'name': "zodiaco_chino",

    'summary': """
        app para calcular tu zodiaco chino""",

    'description': """
        extension de la app contantos donde a traves de la fecha muestra el animal del zodiaco chino correspondiente ademas de un apartado vip y bla bla bla
    """,

    'author': "Michael jackson",
    'website': "http://www.sivesestoponmeunpuntitomasenlaevaluacion.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
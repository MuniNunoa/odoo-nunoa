# -*- coding: utf-8 -*-
{
    'name': "Ñuñoa tu barrio",

    'summary': """
        Sistema de gestión vecinal de Ñuñoa""",

    'description': """
        Long description of module's purpose
    """,

    'author': "José Miguel Cordero, Municipalidad de Ñuñoa",
    'website': "https://www.nunoa.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/problema_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

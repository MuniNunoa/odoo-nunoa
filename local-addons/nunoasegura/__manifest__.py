# -*- coding: utf-8 -*-
{
    'name': "Ñuñoa Segura",

    'summary': """
        Central de seguridad pública de Ñuñoa""",

    'description': """
        Long description of module's purpose
    """,

    'author': "José Miguel Cordero, Municipalidad de Ñuñoa",
    'website': "https://github.com/josemcorderoc/odoo-nunoa",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'tickets', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/procedures.xml',
        'views/procedures_categories.xml',
        'views/neighborhood_plan.xml',
        'static/src/xml/groups.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    "qweb": ['static/src/xml/procedures_template.xml'],
}

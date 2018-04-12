# -*- coding: utf-8 -*-
{
    'name': "citasfpg",

    'summary': """
        Crea, modifica y muestra las citas""",

    'description': """
        Crea, modifica y muestra las citas
    """,

    'author': "Fernando Priego Galvez",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/citas.xml',
	'data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}

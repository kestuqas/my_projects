# -*- coding: utf-8 -*-
{
    'name': "pm",

    'summary': """
        This is a trial odoo project management module""",

    'description': """
        This is a trial odoo project management module mainly dedicated for freelancers, which contains or will contain project, time, invoicing and payment management functions.
    """,

    'author': "Kęstutis Reimeris",
    'website': "N/A",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

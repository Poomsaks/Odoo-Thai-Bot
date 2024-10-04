# -*- coding: utf-8 -*-
{
    'name': "Odoo-thai-Bot",
    'author': "Poomsak",
    'description': '',
    'version': '0.1',
    'depends': ['base', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/main_bot.xml',
        'views/my_template.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'images': ['static/description/icon.png'],
}

# -*- coding: utf-8 -*-
# Copyright 2016 SYLEAM Info Services
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Website Custom Robots',
    'version': '1.0',
    'category': 'Custom',
    'description': """Allows to customize the robots.txt file per website""",
    'author': 'SYLEAM',
    'website': 'http://www.syleam.fr/',
    'depends': ['website'],
    'data': [
        'views/website.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'active': False,
    'license': 'AGPL-3',
}


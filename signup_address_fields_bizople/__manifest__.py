# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Bizople Solutions Pvt. Ltd.
# See LICENSE file for full copyright and licensing details.

{
    'name': 'Signup Address Fields',
    'description': """ Signup Address Fields """,
    'summary': """ Signup Address Fields """,
    'category': 'Website',
    'version': '14.0.0.0',
    'author': 'Bizople Solutions Pvt. Ltd.',
    'website': 'https://www.bizople.com/',
    'depends': [
        'portal'    
    ],
    'data': [
        'views/assets.xml',
        'views/auth_signup_template.xml',
    ],
    'images': [
        'static/description/banner.png'
    ],
    'installable': True,
    'application': True,
    'license': 'OPL-1',
}

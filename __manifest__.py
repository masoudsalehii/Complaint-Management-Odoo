# -*- coding: utf-8 -*-
{
    'name': 'RealState Complaint',
    'version': '1.0.0',
    'author': 'Masoud Salehi',
    'category': 'Realstate/Complaints',
    'sequence': -105,
    'summary': 'Complaints Management',
    'description': """""",
    'depends': ['mail', 'base', 'board', 'hr', 'sale', 'project','website_profile'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/menu.xml',
        'views/complaints_views.xml',
        'views/complaint-form-template.xml',
        'views/submit-form-template.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'assets': {
        'web.assets_frontend': [
            'realstate_complaint/static/src/css/complaints_form.css',
        ],
    },
}

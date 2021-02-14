# Copyright 2014-2018 Tecnativa - Pedro M. Baeza
{
    'name': 'Sales Order bid',
    'version': '14.0',
    'author': 'Ketan Kachhela',
    'category': 'Sales Management',
    'depends': [
        'account',
        'sale',
        'sale_management',
    ],
    'website': '',
    'maintainers': ['Ketan Kachhela'],
    'data': [
        'data/data.xml',
        'views/account_move_view.xml',
        'views/sale_order_views.xml',
        'views/report_invoice.xml',
        'views/account_report.xml',
        'report/sale_report_templates.xml',
        'report/sale_report.xml'
    ],
    'demo': [
    ],
    'installable': True,
}

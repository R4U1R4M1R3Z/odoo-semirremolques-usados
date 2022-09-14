# -*- coding:utf-8 -*-

{
    'name': 'Modulo de semirremolques usados',
    'version': '1.0',
    'depends': [
        'contacts',
        'mail',
    ],
    'author': 'Raúl Ramírez',
    'category': 'Sale',
    'website': 'http://www.indetruck.com',
    'summary': 'Modulo de control de semirremolques usados',
    'description': '''
    Modulo de control de semirremolques usados
    ''',
    'data': [
        'views/usados.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'report/reporte_usados.xml',
    ],
}
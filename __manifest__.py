{
    'name': 'pharmacy management system',
    'version': '1.2',
    'author': 'SLP',
    'keywords': ['pharmacy', 'management', 'system'],
    'license': 'AGPL-3',
    'key': 'pharmacy management system',
    'category': 'Sales/CRM',
    'sequence': 15,
    'summary': 'Track leads and close opportunities',
    'description': "This is the pharmacy management system",
    'website': 'https://slppharmacy.com',
     'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/pharmacy_views.xml',
        'views/pharmacy_menu_views.xml',
    ],
    'images': ['static/description/icon.png'],
    'assets': {
        'web.assets_backend': [
            'static/src/css/style.css',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False
}
# -*- coding: utf-8 -*-
{
    'name': "Catalog",
    'summary': 'Odoo module untuk menyediakan catalog busana yang ada di Sanggar Liza',
    'description': 'Modul ini dapat menampilkan seluruh busana yang tersedia, menambahkan busana ',
    'sequence': -100,
    'author': "G11 #IndonesiaTanpaPacaran",
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/catalog_menus.xml',
        'views/catalog_forms.xml',
        'views/catalog_trees.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
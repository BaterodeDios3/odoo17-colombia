# -*- coding: utf-8 -*-
{
    'name': "Chats de WhatsApp en CRM",

    'summary': """ CRM """,

    'description': """
        Historial de chats de WhatsApp en crm_lead
    """,

    'author': "Alex Martínez",
    'website': "https://www.plataformacocrear.com/",

    'version': '0.1',
    'category': 'Sales/Sales',
    'sequence': 95,

    'depends': [
        'sale',
        'crm',
    ],

    'data': [
        'views/crm_lead_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'cocrear/static/src/css/custom_styles.css',
        ],
    },
    'application': False,
}
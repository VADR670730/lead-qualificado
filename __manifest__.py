# -*- coding: utf-8 -*-
{
    'name': "lead-qualificado",

    'summary': """
        Adiciona campos para qualificar o lead.
        """,

    'description': """
        Módulo destinado a extender o módulo CRM, adicionando a possibilidade de criar e editar características do condomínio.
    """,

    'author': "André Guilhon",
    'website': "https://guilhon.dev.br",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['crm'],

    'data': [
        'views/views.xml',
        'reports/lead_report.xml',
        'reports/reports.xml',
    ]
}
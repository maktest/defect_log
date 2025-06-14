{
    'name': 'Manufacturing Defect Log',
    'license': 'LGPL-3',
    'version': '18.0.1.0.0',
    'category': 'Manufacturing',
    'summary': "Журнал фіксації браку на виробництві",
    'description': "Облік і аналіз дефектів виробництва. Всі ключові поля, фільтри, експорт.",
    'depends': ['mrp', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/defect_log_views.xml',
    ],
    'installable': True,
    'application': True,
}

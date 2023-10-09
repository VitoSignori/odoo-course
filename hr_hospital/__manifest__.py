{
    'name': "Hospital",
    'summary': " Odoo-school, practice 2",

    'author': "Vito Signori",
    'website': "http://www.vitosignori.com",

    'category': 'Customizatin',
    'license': 'OPL-1',
    'version': '15.0.1.0.0',

    'depends': ['base'],
    'external_dependencies': {'python': [], },

    'data': [
        'security/ir.model.access.csv',
        'views/hospital_menu.xml',
        'views/hospital_doctor_views.xml',
        'views/hospital_patient_views.xml',
        'views/hospital_disease_views.xml',
        'views/hospital_patient_visit_views.xml',
        'data/disease_data.xml',
    ],

    'demo': [
        'demo/doctor_demo.xml',
        'demo/patient_demo.xml'
    ],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/icon.png',
    ],

}

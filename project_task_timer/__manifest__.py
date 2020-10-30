# -*- coding: utf-8 -*-

{
    'name': 'TEC Project Task Timer',
    'version': '13.0.1.0.0',
    'summary': """Task Timer With Start & Stop""",
    'description': """"This module helps you to track time sheet in project automatically.""",
    'category': 'Project',
    'author': "Tripoli entrepreneurs Club",
    'maintainer': 'Tripoli entrepreneurs Club',
    'website': 'https://www.tripolientrepreneurs.org/',
    'depends': ['base', 'project', 'hr_timesheet'],
    'data': [
        'wizards/stop_reason.xml',
        'views/project_task_timer_view.xml',
        'views/project_timer_static.xml',
        
    ],
    'images': ['static/description/banner.png'],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
    'development_status': 'Beta',
}

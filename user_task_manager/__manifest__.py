{
    "name": "User Task Manager",
    "summary": "Gestion de tareas de usuarios",
    "description": "Modulo para gestionar tareas asignadas a usuarios.",
    "version": "15.0.1.0.0",
    "category": "Productivity",
    "author": "Julio Gomez",
    "website": "",
    "depends": ["base"],
    "data": [
        "security/task_security.xml",
        "security/ir.model.access.csv",
        "views/task_views.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
# -*- coding: utf-8 -*-
{
    "name": "Sentbox",
    "summary": """Quick way to find sent messages""",
    "category": "Discuss",
    "images": [],
    "version": "1.0.0",

    "author": "IT-Projects LLC, Pavel Romanchenko",
    "website": "https://it-projects.info",
    "license": "LGPL-3",

    "depends": [
        "base",
        "mail",
        "mail_base"
    ],

    "data": [
        "views/templates.xml",
    ],
    "qweb": [
        "static/src/xml/menu.xml",
    ],
    'installable': True,
}

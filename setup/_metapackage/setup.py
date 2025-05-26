import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-hr-recruitment",
    description="Meta package for open-synergy-ssi-hr-recruitment Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_hr_recruitment',
        'odoo14-addon-ssi_hr_recruitment_career_transition',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)

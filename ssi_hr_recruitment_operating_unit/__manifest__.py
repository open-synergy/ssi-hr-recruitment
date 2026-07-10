# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "HR - Recruitment + Operating Unit",
    "version": "14.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_hr_recruitment",
        "ssi_operating_unit_mixin",
    ],
    "data": [
        "security/res_group/recruitment_applicant.xml",
        "security/res_group/recruitment_vacancy.xml",
        "security/ir_rule/recruitment_applicant.xml",
        "security/ir_rule/recruitment_vacancy.xml",
        "view/recruitment_applicant.xml",
        "view/recruitment_vacancy.xml",
    ],
}

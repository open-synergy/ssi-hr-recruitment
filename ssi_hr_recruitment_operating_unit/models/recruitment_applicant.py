# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class RecruitmentApplicant(models.Model):
    """
    Represents a job applicant going through the recruitment workflow.
    Adds a single Operating Unit to segregate applicant data by
    organizational unit, on top of the company already carried by the
    transaction mixin.
    """

    _name = "recruitment_applicant"
    _inherit = [
        "recruitment_applicant",
        "mixin.single_operating_unit",
    ]

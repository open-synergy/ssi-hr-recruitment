# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class RecruitmentVacancy(models.Model):
    """
    Represents a job vacancy opened for recruitment.
    Adds a single Operating Unit to segregate vacancy data by
    organizational unit, on top of the company already carried by the
    transaction mixin.
    """

    _name = "recruitment_vacancy"
    _inherit = [
        "recruitment_vacancy",
        "mixin.single_operating_unit",
    ]

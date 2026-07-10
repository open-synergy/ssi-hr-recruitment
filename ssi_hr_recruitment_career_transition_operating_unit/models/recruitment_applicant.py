# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class RecruitmentApplicant(models.Model):
    """
    Propagates the applicant's Operating Unit to the join
    ``employee_career_transition`` record created by ``action_recruit()``,
    so the two records share the same Operating Unit instead of the
    career transition falling back to the acting user's default.
    """

    _inherit = "recruitment_applicant"

    def _prepare_career_transition_data(self, employee_id):
        _super = super(RecruitmentApplicant, self)
        res = _super._prepare_career_transition_data(employee_id)
        if self.operating_unit_id:
            res["operating_unit_id"] = self.operating_unit_id.id
        return res

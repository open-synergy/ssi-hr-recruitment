# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestRecruitmentCareerTransitionOperatingUnit(YamlTransactionCase):
    def test_recruitment_career_transition_operating_unit(self):
        self.run_yaml_scenario(
            "test_data_recruitment_career_transition_operating_unit.yaml"
        )

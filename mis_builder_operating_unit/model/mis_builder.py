# -*- coding: utf-8 -*-
# © 2015 Eficent Business and IT Consulting Services S.L. -
# Jordi Ballester Alomar
# © 2015 Serpent Consulting Services Pvt. Ltd. - Sudhir Arya
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from openerp import api, fields, models


class MisReportInstance(models.Model):

    _inherit = 'mis.report.instance'

    operating_unit_ids = fields.Many2many('operating.unit',
                                          string='Operating Unit',
                                          required=False)


class MisReportInstancePeriod(models.Model):

    _inherit = 'mis.report.instance.period'

    @api.multi
    def _get_additional_move_line_filter(self):
        aml_domain = super(
            MisReportInstancePeriod, self)._get_additional_move_line_filter()
        if self.report_instance_id.operating_unit_ids:
            operating_unit_ids = [op.id for op in
                                  self.report_instance_id.operating_unit_ids]
            aml_domain.append(('operating_unit_id', 'in',
                               tuple(operating_unit_ids)))
        return aml_domain

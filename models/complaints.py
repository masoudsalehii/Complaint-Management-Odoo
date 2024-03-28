from odoo import models, fields, api


class Complaints(models.Model):
    _name = 'realstate_complaint.complaints'
    _description = 'complaints'
    _rec_name = 'complaint_id'

    complaint_id = fields.Char(string='Complaint ID', readonly=True, compute='_compute_complaint_id')
    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    flat_address = fields.Char(string='Flat Address', required=True)
    complaint_type = fields.Selection([
        ('question', 'Question'),
        ('electrical', 'Electrical Issue'),
        ('heating', 'Heating Issue'),
        # Add more complaint types as needed
    ], string='Complaint Type', required=True)
    description = fields.Text(string='Description', required=True)

    service_reply = fields.Html(string='Reply', widget='html',
                                    attrs={'style': 'height: 300px; overflow-y: auto;'} )

    status = fields.Selection([('NEW', 'New'),
                               ('REVIEW', 'In Review'),
                               ('PROGRESS', 'In Progress'),
                               ('SOLVED', 'Solved'),
                               ('CLOSED', 'Closed'), ], default='NEW', string='Status', required='True')

    # Method
    @api.onchange('complaint_id')
    def _compute_complaint_id(self):
        for record in self:
            record.complaint_id = str(record.id).zfill(7)

    def action_classify(self):
        # I have to add a feature here to send an email so that he knows he needs to review this task
        for rec in self:
            rec.status = 'REVIEW'

    def action_drop(self):
        for rec in self:
            # Update state to 'CLOSED'
            rec.status = 'CLOSED'

    def action_review(self):
        for rec in self:
            # Update state to 'CLOSED'
            rec.status = 'PROGRESS'

    def action_plan(self):
        for rec in self:
            report_action = self.env.ref('realstate_complaint.report_complaint').report_action(self)  # Pass `self` here
            rec.status = 'PROGRESS'
            # Generate report
        return report_action


    def action_close(self):
        # Update status
        for rec in self:
            rec.status = 'CLOSED'
            # send an email
            # I kept getting the following error: ValueError: A string literal cannot contain NUL (0x00) characters.
            # Due to the time limit I did not invest more time to solve the issue
            # template = self.env.ref('realstate_complaint.email_template_complaint_closed')
            # template.send_mail(rec.id, force_send=True)

    def action_solve(self):
        for rec in self:
            rec.status = 'SOLVED'







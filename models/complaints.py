from odoo import models, fields, api
from odoo.exceptions import UserError


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
        # print action plan based on DIN5008 standard.
        for rec in self:
            rec.status = 'PROGRESS'

    def action_close(self):
        # send an email
        # for rec in self:
        #     # Check if description field is empty
        #     if rec.service_reply:
        #         # Send email to tenant
        #         mail_values = {
        #             'subject': 'Your Complaint Update - %s' % rec.complaint_id,
        #             'body_html': '<p>Hello,</p><p>Your complaint has been resolved. Here is the reply provided:'
        #                          '</p><p>%s</p><p>Thank you.</p>' % rec.service_reply,
        #             'email_to': rec.email,
        #         }
        #         self.env['mail.mail'].create(mail_values).send()
        #     else:
        #         mail_values = {
        #             'subject': 'Your Complaint Update - %s' % rec.complaint_id,
        #             'body_html': 'Your Issue is Closed' ,
        #             'email_to': rec.email,
        #         }
        #         self.env['mail.mail'].create(mail_values).send()

        # Update status
        for rec in self:
            rec.status = 'CLOSED'

    def action_solve(self):
        for rec in self:
            rec.status = 'SOLVED'







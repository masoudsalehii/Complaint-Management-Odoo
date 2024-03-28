from odoo import http
from odoo.http import request


class ComplaintsForm(http.Controller):

  @http.route('/complaints/form', csrf=False, auth='public', website=True)
  def complaints_form(self, **kw):
    # Provide necessary context here, if any
    return http.request.render('realstate_complaint.complaints_form')

  @http.route('/complaints/submit', csrf=False, auth='public', methods=['GET', 'POST'], website=True)
  def complaints_submit(self, **post):
    # Filter out the csrf_token field if present
    post.pop('csrf_token', None)
    Complaints = request.env['realstate_complaint.complaints']
    Complaints.create(post)
    return request.render('realstate_complaint.complaints_submit_confirmation')


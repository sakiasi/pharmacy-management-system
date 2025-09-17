from odoo import models, fields

class PharmacyPatient(models.Model):
    _name = 'pharmacy.patient'
    _description = 'Patient'

    name = fields.Char(string='Full Name', required=True)
    first_name = fields.Char()
    last_name = fields.Char()
    date_of_birth = fields.Date()
    gender = fields.Selection([('male','Male'), ('female','Female'), ('other','Other')])
    phone = fields.Char()
    email = fields.Char()
    address = fields.Text()
    insurance_info = fields.Char()
    medical_history = fields.Text()
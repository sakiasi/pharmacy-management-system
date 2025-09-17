from odoo import fields, models

class PharmacyEmployee(models.Model):
    _name = 'pharmacy.employee'
    _description = 'pharmacy employee'

    name = fields.Char(string='Name', required=True)
    dob = fields.Date(string='Date of Birth', required=True)
    phone = fields.Char(string='Phone Number', required=True)
    email = fields.Char(string='Email', required=True)
    address = fields.Text(string='Address')
    position = fields.Selection([
        ('pharmacist', 'Pharmacist'),
        ('assistant', 'Assistant'),
        ('manager', 'Manager')
    ], string='Position', required=True)
    
    #test

from odoo import models, fields


class HospitalPatientVisit(models.Model):
    _name = 'hr.hospital.patient.visit'
    _description = 'Hospital Patient Visit'

    date = fields.Datetime()
    patient = fields.Many2one(comodel_name='hr.hospital.patient')
    doctor = fields.Many2one(comodel_name='hr.hospital.doctor')
    conclusion = fields.Char()

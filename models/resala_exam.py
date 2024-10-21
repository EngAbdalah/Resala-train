from odoo import models, fields

class ResalaExam(models.Model):
    _name = 'resala_exam'
    _description = 'Exam Management'

    name = fields.Char(string='Exam Name', required=True)
    notes = fields.Text(string='Notes')
    course = fields.Many2one('resala_courses', string='Course')
    state = fields.Selection([('pass', 'Pass'), ('fail', 'Fail')], string='Result')
    trainer_id = fields.Many2one('resala_trainer', string='Trainer', related='course.trainer_id')

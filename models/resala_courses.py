from odoo import models, fields

class ResalaCourses(models.Model):
    _name = 'resala_courses'
    _description = 'Course Management'

    name = fields.Char(string='Course Name', required=True)
    hours = fields.Float(string='Course Hours')
    trainer_id = fields.Many2one('resala_trainer', string='Trainer')
    pass_count = fields.Integer(string='Passed Exams', default=0)
    total_count = fields.Integer(string='Total Exams', default=0)

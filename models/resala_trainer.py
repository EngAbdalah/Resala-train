from odoo import models, fields, api

class ResalaTrainer(models.Model):
    _name = 'resala_trainer'
    _description = 'Trainer Management'

    name = fields.Char(string='Trainer Name', required=True)
    sequence = fields.Integer(string='Sequence', default=10)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    courses = fields.One2many('resala_courses', 'trainer_id', string='Courses')
    state = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused')
    ], string='Status', compute='_compute_state', store=True)

    @api.depends('courses')
    def _compute_state(self):
        for trainer in self:
            if trainer.courses:
                total_passed = sum(course.pass_count for course in trainer.courses)
                total_exams = sum(course.total_count for course in trainer.courses)
                trainer.state = 'accepted' if total_exams > 0 and (total_passed / total_exams) * 100 > 70 else 'refused'

    def action_open_exams(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Exams',
            'res_model': 'resala_exam',
            'domain': [('course', 'in', self.courses.ids)],
            'view_mode': 'tree,form',
            'context': {'default_trainer_id': self.id},
        }

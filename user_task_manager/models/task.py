from odoo import api, fields, models
from odoo.exceptions import ValidationError


class UserTask(models.Model):
    _name = 'user.task'
    _description = 'User Task'
    _order = 'deadline asc'

    name = fields.Char(string='Titulo', required=True)
    description = fields.Text(string='Descripcion')
    priority = fields.Selection(
        [('0', 'Baja'), ('1', 'Media'), ('2', 'Alta')],
        string='Prioridad',
        default='1',
    )
    state = fields.Selection(
        [
            ('draft', 'Borrador'),
            ('in_progress', 'En Progreso'),
            ('done', 'Completada'),
        ],
        string='Estado',
        default='draft',
    )
    deadline = fields.Date(string='Fecha Limite')
    is_done = fields.Boolean(
        string='Completada',
        compute='_compute_is_done',
        store=True,
    )
    user_id = fields.Many2one(
        'res.users',
        string='Usuario Asignado',
        default=lambda self: self.env.user,
        required=True,
    )

    @api.depends('state')
    def _compute_is_done(self):
        for task in self:
            task.is_done = task.state == 'done'

    @api.constrains('deadline')
    def _check_deadline(self):
        for task in self:
            if task.deadline and task.deadline < fields.Date.today():
                raise ValidationError(
                    'La fecha limite no puede ser menor a la fecha actual.'
                )




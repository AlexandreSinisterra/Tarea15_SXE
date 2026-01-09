from odoo import models, fields

class Diagnostico(models.Model):
    _name = 'hospital.diagnostico'
    _description = 'Gestión de Diagnósticos'

    medico_id = fields.Many2one('hospital.medico', string="medico", required=True)
    paciente_id = fields.Many2one('hospital.paciente', string="paciente", required=True)
    sintoma = fields.Text(string="sintomas")
    consulta = fields.Char(related='medico_id.consulta', string="Consulta", readonly=True)
    resultado = fields.Text(string="resultado")
    cura = fields.Text(string="cura")
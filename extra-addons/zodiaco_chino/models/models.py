# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class zodiaco_chino(models.Model):
    _inherit = 'res.partner'

    f_nac = fields.Date("Fecha de nacimiento")
    edad = fields.Integer(string="Edad", readonly = True, compute="_calcular_edad", store=True)
    signo_chino = fields.Char(string="Signo Chino", readonly = True, compute="_calcular_chinada", store=True)

    @api.depends('f_nac')
    def _calcular_edad(self):
        for record in self:
            if record.f_nac:
                if (record.f_nac.month,record.f_nac.day) < (datetime.now().month,datetime.now().day):
                    record.edad = (datetime.now().year - record.f_nac.year) -1
                else:
                    record.edad = datetime.now().year - record.f_nac.year

    @api.depends('f_nac')
    def _calcular_chinada(self):
        signos = [
            "Rata", "Buey", "Tigre", "Conejo", "Dragón", "Serpiente",
            "Caballo", "Cabra", "Mono", "Gallo", "Perro", "Cerdo"
        ]
        for record in self:
            if record.f_nac:
                record.signo_chino = signos[(record.f_nac.year - 4) % 12]
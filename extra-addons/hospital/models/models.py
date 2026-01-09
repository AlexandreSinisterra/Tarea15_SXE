# -*- coding: utf-8 -*-
#from contextlib import nullcontext

#from odoo import models, fields, api
#from datetime import datetime

#class zodiaco_chino(models.Model):
#    _inherit = 'res.partner'
#
#    f_nac = fields.Date("Fecha de nacimiento")
#    edad = fields.Integer(string="Edad", readonly = True, compute="_calcular_edad", store=True)
#    signo_chino = fields.Char(string="Signo Chino", readonly = True, compute="_calcular_chinada", store=True)
#    codigo_socio = fields.Char(string="Código de Socio")
#    lvl_f = fields.Char(string="Nivel de Fidelidad", readonly = True, compute="_calcular_tonteriA", store=True)
#
#    @api.depends('codigo_socio')
#    def _calcular_tonteriA(self):
#        for record in self:
#            codigo = record.codigo_socio or ""
#            if codigo.startswith("G"):
#                record.lvl_f = "Gold"
#            elif codigo:
#                record.lvl_f = "Prémium"
#            else:
#                record.lvl_f = "Estándar"
#
#    @api.depends('f_nac')
#    def _calcular_edad(self):
#        for record in self:
#            if record.f_nac:
#                if (record.f_nac.month,record.f_nac.day) < (datetime.now().month,datetime.now().day):
#                    record.edad = (datetime.now().year - record.f_nac.year) -1
#                else:
#                    record.edad = datetime.now().year - record.f_nac.year
#
#    @api.depends('f_nac')
#    def _calcular_chinada(self):
#        signos = [
#           "Rata", "Buey", "Tigre", "Conejo", "Dragón", "Serpiente",
#            "Caballo", "Cabra", "Mono", "Gallo", "Perro", "Cerdo"
#        ]
#        for record in self:
#            if record.f_nac:
#                record.signo_chino = signos[(record.f_nac.year - 4) % 12]
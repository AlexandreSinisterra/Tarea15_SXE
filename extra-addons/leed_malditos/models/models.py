# -*- coding: utf-8 -*-

from odoo import models, fields, api

class my_module(models.Model):
     _name = 'leed_malditos.leed_malditos'
     _des = 'ni idea'

     Alumno = fields.Char(string="Alumno")
     nivel_sueno = fields.Integer(string="nivel_sueno")
     bebida_recomendado = fields.Char(string="bebida_recomendado",compute='_una_funcion')

     @api.depends('nivel_sueno')
     def _una_funcion(self):
          for record in self:
               if record.nivel_sueno <4 and record.nivel_sueno>0:
                    record.bebida_recomendado = "Café con leche"
               elif record.nivel_sueno <7 and record.nivel_sueno>3:
                    record.bebida_recomendado = "Café solo largo"
               elif record.nivel_sueno <10 and record.nivel_sueno>6:
                    record.bebida_recomendado = "Café solo larguísimo"
               elif record.nivel_sueno==10:
                    record.bebida_recomendado = "Inyección de adrenalina"
               else:
                    record.bebida_recomendado = "fuera de rango"
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
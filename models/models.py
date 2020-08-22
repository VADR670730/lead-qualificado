# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LeadQualificado(models.Model):
    _inherit = 'crm.lead'

    quantidade_unidades = fields.Integer(string='Quantidade de unidades')
    quantidade_blocos = fields.Integer(string='Quantidade de blocos')
    quantidade_moradores = fields.Integer(string='Quantidade de moradores')
    tipo_portaria = fields.Selection([('1', 'Própria'), ('2', 'Terceirizada')], string='Tipo de portaria')
    horario_portaria = fields.Selection([('12', '12 horas'), ('24', '24 horas')], string='Horario da portaria')
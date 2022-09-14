# -*- coding:utf-8 -*-
from odoo import api, fields, models

class ubicacion(models.Model):
    _name = 'ubicaciones'
    _description = 'Modulo para el control de ubicaciones'

    name = fields.Char(string='Nombre descriptivo de la ubicación')
    contacto = fields.Many2one(comodel_name='res.partner', string='Contacto')
    telf_contacto = fields.Char(related="contacto.phone", string="Teléfono de contacto")
    ubicacion = fields.Char(string="Ubicación")
    
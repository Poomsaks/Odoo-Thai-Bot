from odoo import models, fields


class MianBot(models.Model):
    _name = 'main.bot'
    _description = 'name'

    name = fields.Char(string="ชื่อ", required=False)


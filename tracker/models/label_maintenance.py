from odoo import models, fields


class LabelMaintenance(models.Model):
    _name = 'label.maintenance'
    _description = "Maintenance for Label Selection"

    name = fields.Char(string="Label")
    active = fields.Boolean(string="Active")
    color = fields.Integer(string="Color")
    handles = fields.Char(string="Drag and Drop")
    label_id = fields.Many2one(string="Label", comodel_name='main.view')


class LabelPrinter(models.Model):
    _name = 'label.printer'
    _description = "Printer for Label Selection"

    name = fields.Char(string="Label")
    active = fields.Boolean(string="Active")
    color = fields.Integer(string="Color")
    printer_id = fields.Many2one(string="Checklist", comodel_name='main.view')


class LabelSorter(models.Model):
    _name = 'label.sorter'
    _description = "Sorter for Label Selection"

    name = fields.Char(string="Label")
    active = fields.Boolean(string="Active")
    color = fields.Integer(string="Color")
    sorter_id = fields.Many2one(string="Checklist", comodel_name='main.view')


class LabelQcc(models.Model):
    _name = 'label.qcc'
    _description = "QCC for Label Selection"

    name = fields.Char(string="Label")
    active = fields.Boolean(string="Active")
    color = fields.Integer(string="Color")
    qcc_id = fields.Many2one(string="Checklist", comodel_name='main.view')
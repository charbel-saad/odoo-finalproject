from odoo import api, fields, models


class StopReason(models.TransientModel):
    _name = 'stop.reason'
    _description = 'Get Lost Reason'

    stop_reason = fields.Selection([ ('Electricity', 'Electricity problem '),('Personal', ' personal problems '),], default="Personal", string="not finished due to" 

    
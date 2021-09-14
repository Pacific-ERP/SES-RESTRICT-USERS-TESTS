from odoo import api, fields, models, tools, SUPERUSER_ID, _
import logging
_logger = logging.getLogger(__name__)

class resGroups(models.Model):
	_inherit = "res.groups"

	group_id = fields.Many2one('restrict.settings', string='All Groups')



class restrict_settings(models.Model):

    _name = 'restrict.settings'
    name = fields.Char(string='name')
    allowed_ip = fields.Char(string='Allowed Ip')
    allowed_group_ids = fields.One2many('res.groups', 'group_id', string='Allowed Groups')
    max_try = fields.Char(string='Maximum attempts')
    cooldown_time = fields.Char(string='cooldown time')


    def write(self, values):
        resConfigObj =  self.env['ir.config_parameter'].sudo()
        if values.get("max_try"):
            resConfigObj.set_param('base.login_cooldown_after',values["max_try"])
        if values.get("cooldown_time"):
            resConfigObj.set_param('base.login_cooldown_duration',values["cooldown_time"])
        
        return super(restrict_settings, self).write(values)


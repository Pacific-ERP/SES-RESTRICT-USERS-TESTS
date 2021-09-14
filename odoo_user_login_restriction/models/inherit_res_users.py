# -*- coding: utf-8 -*-

# from odoo import models, fields, api
from odoo.addons.base.models.res_users   import  Users
from odoo.http import request
from odoo.exceptions import AccessDenied, AccessError, UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)
from odoo import api, fields, models, tools, SUPERUSER_ID, _


class Users(models.Model):

    _inherit = 'res.users'

    @classmethod
    def _login(cls, db, login, password,user_agent_env):
        allowed_user = [1,2]
        user_id = super(Users,cls)._login(db, login, password,{'interactive':True})
        with cls.pool.cursor() as cr:
            self = api.Environment(cr, SUPERUSER_ID, {})[cls._name]
            user = self.env['res.users'].sudo().browse([user_id])
            if  request._context.get("web"):
                if user_id in allowed_user or not user.has_group('base.group_user'):
                    pass
                else:
                    raise AccessDenied(_("Only main admin can login through this url"))
            else:
                restrictObj = self.env["restrict.settings"].sudo().search([])[0]
                user_in_groups = [i.id for i  in restrictObj.allowed_group_ids.users]

                ips = restrictObj.allowed_ip
                if ips is False:
                    ips = ""
                ip = request.httprequest.remote_addr
                if user.has_group('base.group_user'):
                    if user.id in user_in_groups or  ip in ips.replace(" ","").split(","):
                        pass
                    else:
                        raise AccessDenied(_("Either your IP is not configured or you does not have necessary permisson to login "))
        return user_id

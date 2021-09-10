# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################
{
  "name"                 :  "Odoo User Login Restriction",
  "summary"              :  """Restrict Users to Access their Accounts in Odoo""",
  "category"             :  "website",
  "version"              :  "1.0.1",
  "author"               :  "Webkul Software Pvt. Ltd.",
  "license"              :  "Other proprietary",
  "website"              :  "https://store.webkul.com/Odoo.html",
  "description"          :  """Restrict Users to Access their Accounts in Odoo""",
  "live_test_url"        :  "http://odoodemo.webkul.com/?module=odoo_user_login_restriction&lifetime=90&lout=1&custom_url=/admin/login",
  "depends"              :  [
                             'web',
                            #  'website_sale',
                            ],
  "data"                 :  [
                             'security/ir.model.access.csv',
                             'data/demo.xml',
                             'views/admin_login_view.xml',
                             'views/restrict_settings_view.xml',
                            ],
  "images"               :  ['static/description/Banner.png'],
  "application"          :  True,
  "installable"          :  True,
  "price"                :  69,
  "currency"             :  "USD",
}

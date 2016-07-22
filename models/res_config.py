# -*- coding: utf-8 -*-
##############################################################################
#
#    website_custom_robots module for OpenERP, Allows to customize the robots.txt file per website
#    Copyright (C) 2016 SYLEAM Info Services (<http://www.Syleam.fr/>)
#              Sylvain Garancher <sylvain.garancher@syleam.fr>
#
#    This file is a part of website_custom_robots
#
#    website_custom_robots is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    website_custom_robots is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields


class ResConfig(models.Model):
    _inherit = 'website.config.settings'

    robots = fields.Text(string='Robots.txt', related='website_id.robots', help='Contents to put in the /robots.txt URL.')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

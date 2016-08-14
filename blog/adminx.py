#!/usr/vin/env python
# -*- coding:utf-8 -*-
"""
  @date = ''
__author__ = 'magic'
"""
import xadmin
import xadmin.views as xviews

from .models import Post
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(xviews.BaseAdminView, BaseSetting)

class AdminSettings(object):
    # 设置base_site.html的Title
    site_title = '博客管理后台'
    # 设置base_site.html的Footer
    site_footer = 'Winhong Inc.'
    menu_style = 'default'

    # 菜单设置
#     def get_site_menu(self):
#         return (
#             {'title': '博客管理', 'perm': self.get_model_perm(Page, 'change'), 'menus': (
#                 {'title': '所有页面', 'icon': 'fa fa-vimeo-square'
#                     , 'url': self.get_model_url(Page, 'changelist')},
#                 {'title': '分类目录', 'icon': 'fa fa-vimeo-square'
#                     , 'url': self.get_model_url(Category, 'changelist')},
#             )},
#         )
# xadmin.site.register(xviews.CommAdminView, AdminSettings)
#
# xadmin.site.register(Page)
# xadmin.site.register(Category)
xadmin.site.register(Post)
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from wxpy import ensure_one


class ZaoBaoService(object):
    @staticmethod
    def forward_zaobao(bot):
        """
        转发王小二早报
        """
        groups = bot.groups(update=True)

        junwei_group = ensure_one(groups.search('新君威车友交流群'))
        morning_group = ensure_one(groups.search("Hello , morning!"))

        wangerxiao = ensure_one(junwei_group.search('赣州 王二小'))

        @bot.register(junwei_group)
        def forward_msg(msg):
            if msg.member == wangerxiao:
                if ZaoBaoService.__is_zaobao__(msg.text):
                    msg.forward(morning_group, prefix='Kinga')

    @staticmethod
    def __is_zaobao__(text):
        return text.find('早报') != -1 and text.find('微语') != -1

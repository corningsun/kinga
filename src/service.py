#!/usr/bin/env python
# -*- coding:utf-8 -*-
from wxpy import TEXT
from wxpy import Tuling
from wxpy import ensure_one

from config import TuLingConfig, GroupNames


class ZaoBaoService(object):
    @staticmethod
    def forward_zaobao(bot):
        """
        转发王小二早报
        """
        groups = bot.groups(update=True)

        junwei_group = ensure_one(groups.search(GroupNames.JUNWEI))
        morning_group = ensure_one(groups.search(GroupNames.MORNING))

        wangerxiao = ensure_one(junwei_group.search('赣州 王二小'))

        @bot.register(junwei_group)
        def forward_msg(msg):
            if msg.member == wangerxiao:
                if ZaoBaoService.__is_zaobao__(msg.text):
                    msg.forward(morning_group, prefix='Kinga')

    @staticmethod
    def __is_zaobao__(text):
        return text.find('早报') != -1 and text.find('微语') != -1


class TulingService(object):
    @staticmethod
    def start_tuling(bot):
        groups = bot.groups(update=True)
        junwei_group = ensure_one(groups.search(GroupNames.JUNWEI))
        morning_group = ensure_one(groups.search(GroupNames.MORNING))

        tianya_group = ensure_one(groups.search('天涯'))
        sunjiaxiao_group = ensure_one(groups.search('孙家小群'))
        sunjiada_group = ensure_one(groups.search('孙家大群'))

        tuling = Tuling(api_key=TuLingConfig.API_KEY)

        @bot.register([junwei_group, morning_group, tianya_group, sunjiaxiao_group, sunjiada_group], TEXT)
        def forward_msg(msg):
            if msg.is_at:
                tuling.do_reply(msg, at_member=True)




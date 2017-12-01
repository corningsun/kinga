#!/usr/bin/env python
# -*- coding:utf-8 -*-
from wxpy import Bot
from wxpy import embed

from service import ZaoBaoService


def start_bot():
    bot = Bot(cache_path=False)

    # 启用 puid 属性，并指定 puid 所需的映射数据保存/载入路径
    bot.enable_puid('wxpy_puid.pkl')

    # 自动消除手机端的新消息小红点提醒
    # Bot.auto_mark_as_read = True

    ZaoBaoService.forward_zaobao(bot)

    # 堵塞线程
    embed()


if __name__ == '__main__':
    print("main start")

    start_bot()

    print("main end")

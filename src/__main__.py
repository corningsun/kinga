#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time

from wxpy import Bot
from wxpy import embed

from service import ZaoBaoService, TulingService


def init_bot():
    bot = Bot(cache_path=False, console_qr=True)

    # 启用 puid 属性，并指定 puid 所需的映射数据保存/载入路径
    bot.enable_puid('wxpy_puid.pkl')

    # 自动消除手机端的新消息小红点提醒
    # Bot.auto_mark_as_read = True

    return bot


if __name__ == '__main__':
    print("main start")

    bot = init_bot()

    ZaoBaoService.forward_zaobao(bot)

    TulingService.start_tuling(bot)

    @bot.register()
    def forward_msg(msg):
        print("%s: %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), msg))

    embed()

    print("main end")

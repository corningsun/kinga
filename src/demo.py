#!/usr/bin/env python
# -*- coding:utf-8 -*-
from wxpy import ensure_one


def hello_file_helper(bot):
    bot.file_helper.send("Hello, I'm file_helper!")


def self_add(bot):
    # 在 Web 微信中把自己加为好友
    bot.self.add()
    bot.self.accept()


def hello_self(bot):
    # 发送消息给自己
    bot.self.send('能收到吗？')


def show_group_members(bot, group_name):
    group = ensure_one(bot.groups(update=True).search(group_name))
    for member in group.members:
        print("name:%s, nick_name:%s, puid:%s" % (member.name, member.nick_name, member.puid))


def show_groups(bot):
    groups = bot.groups()
    for group in groups:
        print("name:%s, nick_name:%s, puid:%s" % (group.name, group.nick_name, group.puid))

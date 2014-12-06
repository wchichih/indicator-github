#!/usr/bin/env python3
# -*-utf8-*-

import os
from gi.repository import AppIndicator3
from gi.repository import Gtk, GObject
import requests
import time, threading


def add_separator(menu):
    separator = Gtk.SeparatorMenuItem()
    separator.show()
    menu.append(separator)

def item_about(menu):
    dialog = Gtk.AboutDialog.new()
    dialog.set_program_name('Indicator Github')
    dialog.set_version('v0.01')
    dialog.set_comments('Simple notifier for Github')
    dialog.set_authors(['alim0x'])
    dialog.set_website('https://github.com/alim0x/indicator-github')
    dialog.set_website_label('View in Github')
    with open('LICENSE.txt','r') as f:
        dialog.set_license(f.read())
    dialog.show_all()
    dialog.run()
    dialog.destroy()

def item_quit(menu):
    add_separator(menu)
    exit_item = Gtk.MenuItem('Quit')
    exit_item.connect('activate', quit_indicator)
    menu.append(exit_item)
    exit_item.show()


def notify():
    with open(os.path.abspath('.') + '/token', 'r') as f:
        token = f.read()
        token = token[:40]
        if len(token) != 40:
            indicator.set_label('Token Error', '100% thrust')
        else:
            msg = requests.get('https://api.github.com/notifications?access_token=' + token)
            msg = msg.json()
            indicator.set_label(' [ '+str(len(msg))+' ]', '100% thrust')


def loop():
    while(True):
        notify()
        time.sleep(120)


if __name__ == '__main__':
    indicator = AppIndicator3.Indicator.new('Github Notifier', 'github', 0)
    indicator.set_icon_theme_path(os.path.abspath('.'))
    indicator.set_icon('github')
    indicator.set_label('Test', '100% thrust')
    indicator.set_status(1)

    menu = Gtk.Menu()
    menu_item = Gtk.MenuItem.new_with_label('About...')
    menu_item.connect('activate', item_about)
    menu.append(menu_item)
    menu.append(Gtk.SeparatorMenuItem.new())
    menu_item = Gtk.MenuItem.new_with_label('Quit')
    menu_item.connect('activate', Gtk.main_quit)
    menu.append(menu_item)
    menu.show_all()

    indicator.set_menu(menu)
    th = threading.Thread(target = loop, name = 'LoopNotify')
    th.start()
    th.join()
    Gtk.main()

#!/usr/bin/env python3
# -*-utf8-*-

import os
from gi.repository import AppIndicator3
from gi.repository import Gtk, GObject
import requests
import webbrowser


def goto_github():
    webbrowser.open_new('https://github.com/')


# menu items ###############
def add_separator(menu):
    separator = Gtk.SeparatorMenuItem()
    separator.show()
    menu.append(separator)


def add_link(menu):
    link = Gtk.MenuItem(label='View in Github')
    # link.connect('activate', )
    menu.append(link)
    link.show()


def item_about(menu):
    dialog = Gtk.AboutDialog.new()
    dialog.set_program_name('Indicator Github')
    dialog.set_version('v0.01')
    dialog.set_comments('Simple notifier for Github')
    dialog.set_authors(['alim0x'])
    dialog.set_website('https://github.com/alim0x/indicator-github')
    dialog.set_website_label('View in Github')
    with open('LICENSE.txt', 'r') as f:
        dialog.set_license(f.read())
    dialog.show_all()
    dialog.run()
    dialog.destroy()


def item_quit(menu):
    exit_item = Gtk.MenuItem('Quit')
    exit_item.connect('activate', Gtk.main_quit)
    menu.append(exit_item)
    exit_item.show()


# check notifications ###############
def notify():
    with open(os.path.abspath('.') + '/token', 'r') as f:
        token = f.read()
        token = token[:40]
        if len(token) != 40:
            indicator.set_label('Token Error', '100% thrust')
        else:
            msg = requests.get('https://api.github.com/notifications?\
            access_token=' + token)
            msg = msg.json()
            indicator.set_label(' '+str(len(msg))+' ', '100% thrust')
        return True


if __name__ == '__main__':
    # set indicator
    indicator = AppIndicator3.Indicator.new('Github Notifier', 'github', 0)
    indicator.set_icon_theme_path(os.path.abspath('.'))
    indicator.set_icon('github')
    indicator.set_label('Test', '100% thrust')
    indicator.set_status(1)

    # set menu
    menu = Gtk.Menu()
    add_link(menu)
    menu.append(Gtk.SeparatorMenuItem.new())
    menu_item = Gtk.MenuItem.new_with_label('About...')
    menu_item.connect('activate', item_about)
    menu.append(menu_item)
    menu.append(Gtk.SeparatorMenuItem.new())
    item_quit(menu)
    menu.show_all()

    indicator.set_menu(menu)
    notify()
    GObject.timeout_add(120*1000, notify)  # check notification every 2 mins
    Gtk.main()

#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
This is a plugin for the Sublime Text Editor
https://www.sublimetext.com/

Replace all occurences of the currently selected text in the document with an incrementing number.
Some options are provided:
 * Start with an offset
 * Use fixed number of digits (fill up with leading 0s)
 * Define a preceding text in front of the iterator
'''

import sublime, sublime_plugin
import re

SETTINGS_FILE = "SimpleIncrementor.sublime-settings"
EXPHELP = '''Use key:value pairs separated by a blank character to pass options.

Valid Keys:
digits, offset, prectext, step

Example:
digits:5 offset:10

To re-show this dialogue, enable show_help in the Plugin Settings.
'''

def settings():
    return sublime.load_settings(SETTINGS_FILE)


class SimpleIncrementExpertParseCommand(sublime_plugin.TextCommand):
    ''' Take the arguments from expert mode and create a dictionary from it to
        call the main function
    '''

    def run(self, edit, cmd):
        cmds = dict(re.findall(r'(\S+):(\S+)', cmd))
        sublime.active_window().run_command('simple_increment', cmds)
        #print(cmds)


class SimpleIncrementExpertCommand(sublime_plugin.TextCommand):
    ''' Get the user input for expert-mode execution '''

    def run(self, edit):
        shelp = False
        if settings().has("show_help"):
            shelp = settings().get("show_help")
        
        if shelp:
            sublime.message_dialog(EXPHELP)

        settings().set("show_help", False)
        sublime.save_settings(SETTINGS_FILE)

        self.view.window().show_input_panel(
            'Simple Incrementor - Expert Mode:',
            '',
            lambda x: sublime.active_window().run_command('simple_increment_expert_parse', {
                'cmd': x
                }),
            None,
            None)


class SimpleIncrementCommand(sublime_plugin.TextCommand):
    ''' The main component for doing the replacement '''

    def run(self, edit, **kwargs):
        offset = int(kwargs.get('offset', 0))
        digits = int(kwargs.get('digits', 0))
        step = int(kwargs.get('step', 1))
        prectext = kwargs.get('prectext', '')
        
        # Select all occurances of the selected text
        sublime.active_window().run_command('find_all_under')

        i = offset
        cntr = 0
        for occurance in self.view.sel():
            self.view.replace(edit, occurance, prectext + str(i).zfill(digits))
            i += step
            cntr += 1
        self.view.window().status_message('Replaced {} occurances'.format(cntr))


class SimpleIncrementDigitsCommand(sublime_plugin.TextCommand):
    ''' Fill up the left part with leading zeros to match the given number of digits '''

    prectext = ''
    def run(self, edit, prectext = ''):
        self.prectext = prectext 
        self.view.window().show_input_panel(
            'Simple Incrementor: How many total digits?',
            '',
            lambda x: sublime.active_window().run_command('simple_increment', {
                'digits': x,
                'prectext': self.prectext
                }),
            None,
            None)


class SimpleIncrementPrectextCommand(sublime_plugin.TextCommand):
    ''' Get the preceding text from the user '''

    def run(self, edit):
        self.view.window().show_input_panel(
            'Simple Incrementor: Preceding Text?',
            '',
            lambda x: sublime.active_window().run_command('simple_increment', {
                'prectext': x
                }),
            None,
            None)


class SimpleIncrementPrectextDigitsCommand(sublime_plugin.TextCommand):
    ''' Combination of preceding text and fill-up with leading zeros '''

    def run(self, edit):
        self.view.window().show_input_panel(
            'Simple Incrementor: Preceding Text?',
            '',
            lambda x: sublime.active_window().run_command('simple_increment_digits', {
                'prectext': x
                }),
            None,
            None)


class SimpleIncrementOffsetCommand(sublime_plugin.TextCommand):
    ''' Start incrementation with an offset '''

    def run(self, edit):
        self.view.window().show_input_panel(
            'Simple Incrementor: Offset?',
            '',
            lambda x: sublime.active_window().run_command('simple_increment', {
                'offset': x
                }),
            None,
            None)



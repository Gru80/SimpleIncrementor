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

import sublime
import sublime_plugin


class SimpleIncrementCommand(sublime_plugin.TextCommand):
    ''' The main component for doing the replacement '''

    def run(self, edit, offset=0, digits=0, prectext=''):
        sublime.active_window().run_command('find_all_under')
        i = offset
        cntr = 0
        for occurance in self.view.sel():
            self.view.replace(edit, occurance, prectext + str(i).zfill(digits))
            i+=1
            cntr+=1
        self.view.window().status_message ('Replaced {} occurances'.format(cntr))


class SimpleIncrementDigitsCommand(sublime_plugin.TextCommand):
    prectext = ''
    def run(self, edit, prectext = ''):
        self.prectext = prectext 
        self.view.window().show_input_panel(
            'Simple Incrementor: How many total digits?',
            '',
            lambda x: sublime.active_window().run_command('simple_increment', {
                'digits': int(x),
                'prectext': self.prectext
                }),
            None,
            None)


class SimpleIncrementPrectextCommand(sublime_plugin.TextCommand):

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
    def run(self, edit):
        self.view.window().show_input_panel(
            'Simple Incrementor: Offset?',
            '',
            lambda x: sublime.active_window().run_command('simple_increment', {
                'offset': int(x)
                }),
            None,
            None)



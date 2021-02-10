#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Replace all occurences of the current selection in the document with an incrementing number
'''

import sublime
import sublime_plugin


class SimpleIncrementCommand(sublime_plugin.TextCommand):
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
	def on_done(self, user_input):
			sublime.active_window().run_command('simple_increment', {
				'digits': int(user_input),
				'prectext': self.prectext
				})

	def run(self, edit, prectext = ''):
		self.prectext = prectext 
		self.view.window().show_input_panel('Simple Incrementor: How many total digits?', '', self.on_done, None, None)


class SimpleIncrementPrectextCommand(sublime_plugin.TextCommand):
	def on_done(self, user_input):
			sublime.active_window().run_command('simple_increment', {
				'prectext': user_input
				})

	def run(self, edit):
		self.view.window().show_input_panel('Simple Incrementor: Preceding Text?', '', self.on_done, None, None)


class SimpleIncrementPrectextDigitsCommand(sublime_plugin.TextCommand):
	def on_done(self, user_input):
			sublime.active_window().run_command('simple_increment_digits', {
				'prectext': user_input
				})

	def run(self, edit):
		self.view.window().show_input_panel('Simple Incrementor: Preceding Text?', '', self.on_done, None, None)


class SimpleIncrementOffsetCommand(sublime_plugin.TextCommand):
	def on_done(self, user_input):
			sublime.active_window().run_command('simple_increment', {
				'offset': int(user_input)
				})

	def run(self, edit):
		self.view.window().show_input_panel('Simple Incrementor: Offset?', '', self.on_done, None, None)


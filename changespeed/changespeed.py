#!/usr/bin/env python

from plumbum import cli
import time


class Changespeed(cli.Application):
	PROGNAME = "changespeed.py"
	VERSION = "0.1"

	total_seconds = 0


	@cli.switch(["-s", "--seconds"], cli.Range(0, 60), group = "Timesetters")
	def seconds(self, seconds):
		"""Set seconds"""
		self.total_seconds += seconds


	@cli.switch(["-m", "--minutes"], cli.Range(0, 60), group = "Timesetters")
	def minutes(self, minutes):
		"""Set minutes"""
		self.total_seconds += (minutes * 60)


	@cli.switch(["-h", "--hours"], int, group = "Timesetters")
	def hours(self, hours):
		"""Set hours"""
		self.total_seconds += (hours * 60 * 60)


	def speeded_time(self, time, rate):
		"""Recount time for selected rate"""
		coeff = 1.0 / rate
		return time * coeff


	def main(self, rate):
		time_pattern = '%H hours %M minutes %S seconds'
		orig_str = time.strftime(time_pattern, time.gmtime(self.total_seconds))
		rated = self.speeded_time(self.total_seconds, float(rate))
		rated_str = time.strftime(time_pattern, time.gmtime(rated))

		print(orig_str)
		print("x " + rate)
		print("-" * 30)
		print(rated_str)



if __name__ == "__main__":
	Changespeed.run()


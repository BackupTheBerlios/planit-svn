# -*- coding: iso-8859-1 -*-

import sys
import logging.config
from optparse import OptionParser
from planit.input import loader
from planit.system.core import Project
from planit.system.core import Task
from planit.system.core import Resource
from planit.system.core import Timetable

#logging.basicConfig()
logging.config.fileConfig( "log.conf" )

def start():
	(options, args) = parse_command_line()

	project = loader.load( args[0], options.inputFormat )

def parse_command_line():
	usage = "usage: %prog [options] inputFilename outputFilename"
	version = "%prog 0.1"
	parser = OptionParser( usage=usage, version=version )
	parser.add_option( "-i", "--input", dest="inputFormat", type="string", default="planit",  
			help="format of input: one of 'planit' [default]", metavar="FORMAT" )
	parser.add_option( "-o", "--output", dest="outputFormat", type="string", default="png", 
			help="format of output: one of 'png' [default], 'eps'", metavar="FORMAT" )
	parser.add_option( "-v", "--verbose", dest="verbose", action="store_true", default=True, 
			help="make lots of noise [default]" )
	parser.add_option( "-q", "--quiet", dest="verbose", action="store_false",
			help="be very quiet" )
	(options, args) = parser.parse_args()

	if len( args ) < 1:
		parser.error( "incorrect number of arguments" );

	return (options, args)

start()

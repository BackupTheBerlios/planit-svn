import logging
from planit.system.core import Project
from planit.input import planitLoader

def load( filename, format ):
	log = logging.getLogger( "Loader" )

	log.debug( "filename: %s" % filename )
	log.debug( "format: %s" % format )

	project = {
		'planit': planitLoader.load( filename )
	}[ format ]

	return project

import logging
from planit.output import epsExport

def write( project, filename, format ):
	log = logging.getLogger( __name__ )

	log.debug( "filename: %s" % filename )
	log.debug( "format: %s" % format )

	{
		'eps': epsExport.output( project, filename )
	}[ format ]

import logging
import time

class Object:
	def __init__( self ):
		self.log = logging.getLogger( self.__class__.__module__ + "." + self.__class__.__name__ )

class Project( Object ):
	def __init__( self, name ):
		Object.__init__( self )
		self.name = name
		self.refTasks = {}
		self.refResources = {}
		self.refTimetables = {}
		self.tasks = []
		self.resources = []
		self.timetables = []
		self.log.debug( "new Project '%s'" % self.name )
	
	def referenceTask( self, task ):
		self.refTasks[ task.id ] = task
		for childTask in task.childTasks[:]:
			self.referenceTask( childTask )

	def referenceResource( self, resource ):
		self.refResources[ resource.id ] = resource
		for childResource in resource.childResources[:]:
			self.referenceResource( childResource )

	def referenceTimetable( self, timetable ):
		self.refTimetables[ timetable.id ] = timetable
		for childTimetable in timetable.childTimetables[:]:
			self.referenceTimetable( childTimetable )

	def addTask( self, task ):
		self.tasks.append( task )
		self.referenceTask( task )
	
	def addTasks( self, tasks ):
		for task in tasks[:]:
			self.addTask( task )
	
	def addResource( self, resource ):
		self.resources.append( resource )
		self.referenceResource( resource )
	
	def addResources( self, resources ):
		for resource in resources[:]:
			self.addResource( resource )

	def addTimetable( self, timetable ):
		self.timetables.append( timetable )
		self.referenceTimetable( timetable )
	
	def addTimetables( self, timetables ):
		for timetable in timetables[:]:
			self.addTimetable( timetable )

class Task( Object ):
	def __init__( self, id, name, start, end ):
		Object.__init__( self )
		self.id = id
		self.name = name
		self.start = start
		self.end = end
		self.childTasks = []
		self.resourcesUsed = []
		self.log.debug( "new Task '%s' (%s) [%s, %s]" % (self.name, self.id, time.strftime("%Y/%m/%d", start), time.strftime("%Y/%m/%d", end)) )

	def addTask( self, task ):
		self.childTasks.append( task )
	
	def addTasks( self, tasks ):
		for task in tasks[:]:
			self.addTask( task )
	
	def addResourceUsed( self, id, load ):
		self.resourcesUsed.append( [id, load] )
	
class Resource( Object ):
	def __init__( self, id, name ):
		Object.__init__( self )
		self.id = id
		self.name = name
		self.childResources = []
		self.timetablesUsed = []
		self.resourcesUsed = []
		self.log.debug( "new Resource '%s' (%s)" % (self.name, self.id) )
	
	def addResource( self, resource ):
		self.childResources.append( resource )
	
	def addResources( self, resources ):
		for resource in resources[:]:
			self.addResource( resource )
	
	def addTimetableUsed( self, id ):
		self.timetablesUsed.append( id )

	def addResourceUsed( self, id, load ):
		self.resourcesUsed.append( [id, load] )

class Timetable( Object ):
	def __init__( self, id, name ):
		Object.__init__( self )
		self.id = id
		self.name = name
		self.childTimetables = []
		self.log.debug( "new Timetable '%s' (%s)" % (self.name, self.id) )

	def addTimetable( self, timetable ):
		self.childTimetables.append( timetable )
	
	def addTimetables( self, timetables ):
		for timetable in timetables[:]:
			self.addTimetable( timetable )

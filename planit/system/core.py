import logging
from time import strftime

class Project:
	def __init__( self, name ):
		self.log = logging.getLogger( "Project" )
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

class Task:
	def __init__( self, id, name, start, end ):
		self.log = logging.getLogger( "Task" )
		self.id = id
		self.name = name
		self.start = start
		self.end = end
		self.childTasks = []
		self.resourcesUsed = []
		self.log.debug( "new Task '%s' (%s) [%s, %s]" % (self.name, self.id, strftime("%Y/%m/%d", start), strftime("%Y/%m/%d", end)) )

	def addTask( self, task ):
		self.childTasks.append( task )
	
	def addTasks( self, tasks ):
		for task in tasks[:]:
			self.addTask( task )
	
	def addResourceUsed( self, id, load ):
		self.resourcesUsed.append( [id, load] )
	
class Resource:
	def __init__( self, id, name ):
		self.log = logging.getLogger( "Resource" )
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

class Timetable:
	def __init__( self, id, name ):
		self.log = logging.getLogger( "Timetable" )
		self.id = id
		self.name = name
		self.childTimetables = []
		self.log.debug( "new Timetable '%s' (%s)" % (self.name, self.id) )

	def addTimetable( self, timetable ):
		self.childTimetables.append( timetable )
	
	def addTimetables( self, timetables ):
		for timetable in timetables[:]:
			self.addTimetable( timetable )

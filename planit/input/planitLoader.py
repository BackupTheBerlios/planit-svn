import logging
import time
from xml.dom import Node
from xml.dom.ext.reader.Sax import FromXmlFile
from planit.system.core import Project
from planit.system.core import Task
from planit.system.core import Resource
from planit.system.core import Timetable

def load( filename ):
	log = logging.getLogger( "input.planitLoader.load" )

	doc = FromXmlFile( filename )

	rootEL = doc.getElementsByTagName( "project" )[0]

	return loadProject( rootEL )

def loadProject( rootEL ):
	projectName = rootEL.getAttribute( "name" )

	project = Project( projectName )

	tasksEL = getElementsByTagName( rootEL, "tasks" )
	if len( tasksEL ) > 0:
		tasksEL = tasksEL[0]
		tasks = loadTasks( tasksEL )
		project.addTasks( tasks )

	resourcesEL = getElementsByTagName( rootEL, "resources" )
	if len( resourcesEL ) > 0:
		resourcesEL = resourcesEL[0]
		resources = loadResources( resourcesEL )
		project.addResources( resources )

	timetablesEL = getElementsByTagName( rootEL, "timetables" )
	if len( timetablesEL ) > 0:
		timetablesEL = timetablesEL[0]
		timetables = loadTimetables( timetablesEL )
		project.addTimetables( timetables )

	return project

def loadTasks( tasksEL ):
	tasks = []

	for taskEL in getElementsByTagName( tasksEL, "task" ):
		task = loadTask( taskEL )
		if task is not None:
			tasks.append( task )

	return tasks

def loadTask( taskEL ):
	id = taskEL.getAttribute( "id" )
	name = taskEL.getAttribute( "name" )
	start = taskEL.getAttribute( "start" )
	end = taskEL.getAttribute( "end" )

	start = time.strptime( start, "%Y/%m/%d" )
	end = time.strptime( end, "%Y/%m/%d" )

	task = Task( id, name, start, end )

	for childTaskEL in getElementsByTagName( taskEL, "task" ):
		childTask = loadTask( childTaskEL )
		if childTask is not None:
			task.addTask( childTask )

	for resourceEL in getElementsByTagName( taskEL, "use-resource" ):
		id = resourceEL.getAttribute( "id" )
		if resourceEL.hasAttribute( "load" ):
			load = resourceEL.getAttribute( "load" )
			load =  int( load[:-1] )
		else:
			load = 100
		task.addResourceUsed( id, load )

	return task

def loadResources( resourcesEL ):
	resources = []

	for resourceEL in getElementsByTagName( resourcesEL, "resource" ):
		resource = loadResource( resourceEL )
		if resource is not None:
			resources.append( resource )

	return resources

def loadResource( resourceEL ):
	id = resourceEL.getAttribute( "id" )
	name = resourceEL.getAttribute( "name" )

	resource = Resource( id, name )

	for childResourceEL in getElementsByTagName( resourceEL, "resource" ):
		childResource = loadResource( childResourceEL )
		if childResource is not None:
			resource.addResource( childResource )

	for timetableEL in getElementsByTagName( resourceEL, "use-timetable" ):
		id = timetableEL.getAttribute( "id" )
		resource.addTimetableUsed( id )

	for resourceEL in getElementsByTagName( resourceEL, "use-resource" ):
		id = resourceEL.getAttribute( "id" )
		if resourceEL.hasAttribute( "load" ):
			load = resourceEL.getAttribute( "load" )
			load =  int( load[:-1] )
		else:
			load = 100
		resource.addResourceUsed( id, load )

	return resource

def loadTimetables( timetablesEL ):
	timetables = []

	for timetableEL in getElementsByTagName( timetablesEL, "timetable" ):
		timetable = loadTimetable( timetableEL )
		if timetable is not None:
			timetables.append( timetable )

	return timetables

def loadTimetable( timetableEL ):
	id = timetableEL.getAttribute( "id" )
	name = timetableEL.getAttribute( "name" )

	timetable = Timetable( id, name )

	for childTimetableEL in getElementsByTagName( timetableEL, "timetable" ):
		childTimetable = loadTimetable( childTimetableEL )
		if childTimetable is not None:
			timetable.addTimetable( childTimetable )

	return timetable

def getElementsByTagName( element, tagName ):
	list = []
	if element.hasChildNodes():
		for node in element.childNodes[:]:
			if Node.ELEMENT_NODE == node.nodeType:
				if tagName == node.tagName:
					list.append( node )
	return list

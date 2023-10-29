
'''
	import pathlib
	from os.path import dirname, join, normpath
	
	this_folder = pathlib.Path (__file__).parent.resolve ()
	search = normpath (join (this_folder, "../.."))

	import body_scan
	body_scan.start (
		glob_string = search + '/**/*status.py'
	)
'''

import glob
import json

import body_scan.aggregate as aggregate
import body_scan.processes.scan as scan

import body_scan.functions.alarm_printer as alarm_printer
import body_scan.functions.start.sequentially as start_sequentially
import body_scan.functions.start.simultaneously as start_simultaneously

'''
	
'''
def start (
	glob_string = "",
	relative_path = False,
	module_paths = [],
	simultaneous = False,
	print_alarms = True,
	records = 0	
):
	finds = glob.glob (glob_string, recursive = True)
		
	if (records >= 1):
		print ()
		print ("searching for glob_string:")
		print ("	", glob_string)
		print ()
	
	if (records >= 1):
		print ()
		print ("	finds:", finds)
		print ("	finds count:", len (finds))
		print ();

	if (simultaneous == True):
		path_statuses = start_simultaneously.now (
			finds,
			module_paths,
			relative_path,
			records
		)
	else:
		path_statuses = start_sequentially.now (
			finds,
			module_paths,
			relative_path,
			records
		)

	status = aggregate.start (
		path_statuses
	)

	'''
		status
		alarms
		stats
	'''
	print ("status:", json.dumps (status, indent = 4))
	if (print_alarms):
		alarm_printer.start (status ["paths"])
		
	print ("stats:", json.dumps (status ["stats"], indent = 4))	
		
	return {
		"status": status
	}
	

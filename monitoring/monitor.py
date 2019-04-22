# Main driver for the water basin monitoring
# 

##### imports #####
import io
import os
import time
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import logging
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import sys
sys.path.append('../visualization')
from Visualizer import initVisualizer
from Visualizer import updatePlots
from Visualizer import updateData

# monitors
import pHMonitor
import ecMonitor
import tempMonitor

CS = ",";
dirpath = os.getcwd();
resultsPath = dirpath[:dirpath.rfind('/')] + "/results/";

interval_sec = 10;
interval_ms = interval_sec * 1000;

def execute():
	print("Executing monitor process at: " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "\n");
	
	# perform the monitoring
	runMonitors();

	# write the results to file
	phReading_test = random.uniform(0., 14.);
	ecReading_test = random.uniform(0., 3.);
	tempReading_test = random.uniform(10., 25.);
	writeResultsToFile(phReading_test, ecReading_test, tempReading_test);

	# update visualization data
	updateData(phReading_test, ecReading_test, tempReading_test);
	updatePlots();

def runMonitors():
	print("Running monitors\n")
	pHMonitor.readPH();
	ecMonitor.readEC();
	tempMonitor.readTemp();
	print("runMonitors() complete\n\n")


def writeResultsToFile(pHReading, ecReading, tempReading):
	print("Writing results to file...\n")
	timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S');
	filename = resultsPath + timestamp + "_results.txt"
	f = open(filename, "w");

	results = str(pHReading) + CS + str(ecReading) + CS + str(tempReading);

	f.write(results);

	f.close();

	print("writeResultsToFile complete\n\n")


# called by main
def start():
	# get time stamp
	st = datetime.datetime.fromtimestamp(time.time()).strftime('%m-%d-%Y %H:%M:%S');
	print("Starting monitoring system: " + st + "\n")

	# initialize the visualizer
	initVisualizer();

	log = logging.getLogger('apscheduler.executors.default')
	log.setLevel(logging.INFO)  # DEBUG

	fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
	h = logging.StreamHandler()
	h.setFormatter(fmt)
	log.addHandler(h)

	scheduler = BlockingScheduler()
	scheduler.add_job(execute, 'interval', seconds=interval_sec);
	scheduler.start()
	
	


if __name__ == "__main__":
	start();

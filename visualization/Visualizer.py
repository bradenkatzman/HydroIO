
import os

phDataIdx = 0;
ecDataIdx = 1;
tempDataIdx = 2;

phReadings = list();
ecReadings = list();
tempReadings = list();
time = list();


# the function that 'animates' i.e. updates the graph does so on a set interval. Here, we
# set this interval equal to the timer that the monitors operate on. The offset is a rough
# estimate of how long it takes the monitoring process to finish and send updated data to 
# the visualizer class. This way an visualization update will update as it gets new data
offset = 5000;

def initVisualizer():
	print("Initializing Visualizer\n")

	# first, iterate through all files in the results folder and gather the results
	dirpath = os.getcwd();
	resultsPath = dirpath[:dirpath.rfind('/')] + "/results";
	for filename in os.listdir(resultsPath):
	    if filename.endswith(".txt"): 
	    	f = open(resultsPath + "/" + filename, "r");
	    	data = f.read().split(",");
	    	phReadings.append(data[phDataIdx]);
	    	ecReadings.append(data[ecDataIdx]);
	    	tempReadings.append(data[tempDataIdx]);
	
	# x_values
	for x in range(len(phReadings)):
		time.append(x);



# called after each monitor reading to update the plots
def updateData(ph, ec, temp):
	print("Updating visualization data with new readings...\n")
	phReadings.append(ph);
	ecReadings.append(ec);
	tempReadings.append(temp);
	time.append(len(phReadings));


def updatePlots():
	print("Updating plots\n");

	# web hooks here
	

	



		
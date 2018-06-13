
import csv

tp = 0	#True positives
p = 0	#Number of positives
n = 0	#Number of negatives
tn = 0	#True negatives
fn = 0	#False negatives
fp = 0	#False positives

#initializing containers
slengths = [] 

slength = []
swidth = []
plength = []
pwidth = []
label = []

with open('setosa_v_versicolor.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')

	
	for row in spamreader:
		slength = row[0]
		swidth = row[1]
		plength = row[2]
		pwidth = row[3]
		label = int(row[4])
		
		#Here columns 3 and 4 are used with a threshold of 1.0 and 2.0 respectively
		
		prediction = -1;
		if float(row[3]) >= 1.0:
			prediction = 1;
		if float(row[2]) >= 2.0: 
			prediction = 1;
		
		#Counts for the appproriate confustion matrix entry
		if  label == -1 and prediction == -1: 
			tp += 1
		
		if  label == 1 and prediction == 1:
			tn += 1

		if  label == -1 and prediction == 1: 
			fp += 1

		if  label == 1 and prediction == -1: 
			fn += 1	
			
		if label == -1:
			p+=1
		if  label == 1: 
			n+=1
			
		slengths.append(slength)
		
#print(slength)	
#print(slengths)

#displays the values
print("True Positives:" + str(tp))
print("True Negatives:" + str(tn))
print("Positives:" + str(p))
print("Negatives:" + str(n))

print("Sensitivity:" + str(tp / p * 100 ))
print("Precision:" + str(tp/(tp+fp) * 100 ))
print("Specificity:" + str(tn/n * 100 ))
print("Accuracy:" + str((tp+tn)/(tp+tn+fp+fn) *100))

	
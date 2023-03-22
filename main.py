import csv

#Holds the data for our requirements
class bankMonthSum:
    def __init__(self, custID, month, year):
        self.custID = custID
        self.month = month
        self.year = year

    minBalance = 0
    maxBalance = 0
    total = 0

#Name of file to input
inputFile = "testInput1.csv"

#List to hold our objects
objList = []

#Opens the input file
with open(inputFile) as csvfile:
    #Creates an object for reading the csv
    reader = csv.reader(csvfile)
    #Reads each line individually
    for line in reader:
        #Var for telling if obj is already in list
        objListUpdate = False
        #Splits the date apart
        date = line[1].split("/")
        #Searches the list for objects that already exist
        for item in objList:
            if (item.custID == line[0]):
                if (item.month == date[0]):
                    if (item.year == date[2]):
                        #Found one in list so no need to make new object
                        objListUpdate = True
                        item.total = int(line[2]) + item.total
                        if (item.total < item.minBalance):
                            item.minBalance = item.total
                        elif (item.total > item.maxBalance):
                            item.maxBalance = item.total
        #If there isn't one in the list then make a new object
        if (objListUpdate == False):
            bsm = bankMonthSum(line[0], date[0], date[2])
            bsm.total = int(line[2])
            bsm.minBalance = int(line[2])
            bsm.maxBalance = int(line[2])
            objList.append(bsm)

#Name of file to output data
outputFile = "out.csv"

#Opens the output file
with open(outputFile, 'w') as csvfile:
    #Creates an object for writing to the csv
    writer = csv.writer(csvfile)
    #Takes every item in the list of objects we filled and sends its data out to the output file
    for item in objList:
        writer.writerow([item.custID, item.month + '/' + item.year, item.minBalance, item.maxBalance, item.total])
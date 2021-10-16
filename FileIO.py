import csv

#Python Assignment #3

myRecords_list = []

class Record:

    def __init__(self, n, a, d):
        #Initialize donator with 'n' as name
        self.name = n
        self.amount = a
        self.date = d
    
    def getDonation(self):
        # Donator donates 'a' amount of money
        return self.amount
    
    def setDate(self, d):
        # Set self's date of donation to 'd'
        self.date = d

#--------------------------------------------------------------------------
# Next, sort the myrecords list with the following user-defined priority: 
# first by increasing order of date, next by decreasing order of amount, 
# then by alphabetic order of name.
# #------------------------------------------------------------------------ 
    def __lt__(self, other):
        
        nomatch = True
        match = False

        if (self.date < other.date):
            nomatch
            return self.date < other.date
    
        elif (self.date == other.date):
            match
       
            if (self.amount > other.amount):
                nomatch
                return self.amount > other.amount
            
            elif (self.amount == other.amount):
                match
        
                if ( self.name < other.name ):
                    nomatch
                    return self.name < other.name


#--------------------------------------------
# Read from donations-raw.csv and creating
# myrecords, a list of Record objects
#--------------------------------------------
with open('donations-raw.csv', 'r') as myfile:
    reader = csv.reader(myfile)
    next(myfile)
    for row in reader:
        myRecords_list.append(Record(row[0], row[1], row[2]))


#-------------------------------------------------------------
# Sort the myrecords list and print in donationsprocessed.csv
#-------------------------------------------------------------
myRecords_list.sort()


#---------------------------------
# Print in donationsprocessed.csv
#---------------------------------
with open('donationsprocessed.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for Record in myRecords_list:
        writer.writerow([Record.date, Record.amount, Record.name])


#-----------------------------------------------
# Print the contents of donations-processed.csv 
#-----------------------------------------------
filename = 'donationsprocessed.csv'
with open(filename) as file_object:
    for line in file_object:
        print(line)
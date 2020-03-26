#Composite Cutter is a tool to break CSVs given by Ag retailers into individual files per sample. 
#This is used to deal with how the Agrian platform handles sample data with no spatial information
import csv


with open('Manual Sample Upload Harvex.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    fieldNames = reader.fieldnames

    for line in reader:
        currentID = line['SampleID'] +'.csv'

    
        with open(currentID, 'w') as new_file:
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldNames, delimiter=',')

            csv_writer.writeheader()
            csv_writer.writerow(line)
 




  
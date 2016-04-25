import csv

#change to align with your file names
student_prefs = "prefs.csv" #assumes the preferences file is in the same location as this script
                            
student_invens = "inven.csv" #assumes the inventory file is in the same location as this script

#queries the sponser preferences into a readable format
def queryprefs(proj, rank):
    #grabs the file
    csvfile = open(student_prefs,'r')
    prefs = csv.DictReader(csvfile)

    #init results dictionary
    results = {}

    #query prefs file
    for row in prefs:
        if(int(row[proj]) <= int(rank)):
            if(str(row["name"]) in results):
                results[str(row["name"])][proj] = int(row[proj])
            else:
                results[str(row["name"])] = {}
                results[str(row["name"])][proj] = int(row[proj])

    #print
    for student in results:
        print(student + "\n\t" + str(results[student][proj]))
    
    #export to a file?
    output = input("export results to file? (y/n chose 'n' if you querying both files as the results will be outputted in the next query)")
    if(output == 'y'):
        filename = input("filename?(without '.csv' appended)")
        file = open(filename + ".csv",'a')
        file.write("name,company,rank\n")
        for student in results:
            file.write(student + ', ')
            file.write(proj + ',' + str(results[student][proj]) + '\n')
        file.close()

    #return if you want
    return results

#query inven constrained by provided prefs results
def queryinven(presults = {}):
    #grabs the file
    csvfile = open(student_invens,'r')
    invens = csv.DictReader(csvfile)
    results = {}

    #gather parameters
    item = input("what item to search for? (role,languages,tech...)")
    if(presults != {}):
        #query inven file without prefs
        for row in invens:
            for col in row:
                if(item in col):
                    if(str(row["Your Name"]) in presults):
                        if(str(row["Your Name"]) in results):
                            results[str(row["Your Name"])][str(col)] = str(row[col])
                        else:
                            results[str(row["Your Name"])] = {}
                            results[str(row["Your Name"])][str(col)] = str(row[col])

    else:
        #query inven file without prefs
        for row in invens:
            for col in row:
                if(item in col):
                    if(str(row["Your Name"]) in results):
                        results[str(row["Your Name"])][str(col)] = str(row[col])
                    else:
                        results[str(row["Your Name"])] = {}
                        results[str(row["Your Name"])][str(col)] = str(row[col])

    #export to a file?
    output = input("export results to file? (y/n)")
    if(output == 'y'):
        filename = input("filename?(without '.csv' appended)")
        file = open(filename + ".csv",'a')
        file.write("name")
        first = True
        for student in results:
            if(first):
                for cata in list(results[student].keys()):
                    file.write(',' + cata)
                file.write('\n')
                first = False
            file.write(student)
            for cata in results[student]:
                file.write(',' + str(results[student][cata]))
            file.write('\n')
        file.close()

    #print
    for student in results:
        print(student)
        for sub in results[student]:
            print("\t" + sub + " : " + results[student][sub])

    #return if you want
    return results

#does a combined query, taking the list of students 
#from the preference query, and constraining the query of inventory
#based on the results
def queryfiles(proj, rank):
    prefs = queryprefs(proj, rank)
    return queryinven(prefs)

#main driver, asks the user what they want to do
def main(): 
    choice = ""
    while(choice != 'prefs' and choice != 'inven'):
        choice = input("prefs (students who ranked a certain project higher than a certain rank)\n or inven?(students who ranked a certain amount for a inventory item)\n or both(students who ranked a specific project high and with certain inven parameters)>>")
        if(choice == "prefs"):
            proj = input("what project to check for")
            rank = input("minimum rank to search for? (1 high, 14 low)")
            results = queryprefs(proj, rank)
        elif(choice == "inven"):
            results = queryinven({})
        elif(choice == "both"):
            proj = input("what project to check for")
            rank = input("minimum rank to search for? (1 high, 14 low)")
            results = queryfiles(proj, rank)
        else:
            print("must chose either prefs or inven")

        cont = input("another query? (y/n)")
        if(str(cont) == 'y'):
            main() #dirty, and i dont care!
        elif(str(cont) == 'n'):
            break
        else:
            print("I'll take that as a no!")
            break
main()
from flat import Bill, Flatmate    

from reports import PdfReport, FileSharer


amount = float(input("Hey user, enter the bill amount: "))
period = input("What is the period ? E.g. April 2021: ")

name1 = input("What is your name ? : ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house during the bill period? : "))

name2 = input("What is a name of other flatmate ? : ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period? : "))


the_bill = Bill(amount, period)                       # Object of Bill class
flatmate1 = Flatmate(name1, days_in_house1)           # Instance of Flatmate class
flatmate2 = Flatmate(name2, days_in_house2)


print(f"{flatmate1.name} Pays: ", flatmate1.pays(the_bill, flatmate2))      #flatmate2 = CO-Flatmate of flatmate1  #we can give {name1} also instead of {flatmate1.name}
print(f"{flatmate2.name} Pays: ", flatmate2.pays(the_bill, flatmate1))      #flatmate1 = CO-Flatmate of flatmate2


pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")                 #PDF name will be period name     #Instance of PdfReport class
pdf_report.generate(flatmate1, flatmate2, the_bill)

file_sharer = FileSharer(filepath=pdf_report.filename)                    #To generate the link of the pdf in cloud. So user Can Download Bill
print("")
print("Download the Pdf of the Bill =")
print(file_sharer.share())
print("")
print("")
    




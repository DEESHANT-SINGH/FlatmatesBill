import webbrowser             # Automatically view a PDF file when we RUN code

from fpdf import FPDF
from filestack import Client

class PdfReport:
    """
    Creates a Pdf file that contains data about the flatmates such as their names,
    their due amounts and the periods of the bill. 
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):   # Method 

        flatmate1.pay = str(round(flatmate1.pays(bill, flatmate2), 2))         #str will convert float into string and round( , 2) rounds up to 2 precision value
        flatmate2.pay = str(round(flatmate2.pays(bill, flatmate1), 2))         #we have converted into string because our pdf takes value in string other wise it show error.

        pdf = FPDF(orientation='P', unit='pt', format='A4')      #We are creating an instance(pdf) of FPDF
        #orientation = 'Portrait', unit='Points' i.e. 12points = 16pixels   #this line will create pdf without pages
        pdf.add_page()          #so to add pages

        # Add icon
        pdf.image("files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)       #to create rectangular cell & ln=1 is to add next cell under current cell.

        # Insert Period label and value
        pdf.set_font(family="Times", size=16, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family="Times", size=14)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1.pay, border=0, ln=1)  

        # Insert name and due amount of the second flatmate
        pdf.set_font(family="Times", size=14)
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2.pay, border=0, ln=1)    
      
        pdf.output(self.filename)

        webbrowser.open(self.filename)             # Automatically view a PDF file when we RUN the code, browser will automatically open.

class FileSharer:
    
    def __init__(self, filepath, api_key="AR1osvjJuSymJ8a8FFZxjz"):
        self.filepath = filepath
        self.api_key = api_key


    def share(self):                        # It will upload the file to the cloud and return the link url which we can show to the user and user can download the file
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
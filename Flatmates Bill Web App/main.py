from flask.views import MethodView                     #MethodView is a class and it is already defined in flask library
from wtforms import Form, StringField, SubmitField     #wtform is a library & Form is a class which represents webform #StringField class is used to create a form of our webpage by using python code
from flask import Flask, render_template, request                #Flask is a class that represents webapp
from flatmates_bill import flat                         # Our code of flatmate's bill in CLI
from filestack import Client

app = Flask(__name__)              # We have instantiated the Flask class #__name__ is a string that contains a string of current python file i.e main.py


class HomePage(MethodView):        #we are using Inheritance   # HomePage inherits MethodView
    
    def get(self):                 #When user click on url of Homepage then this Get Method is Executed
        return render_template('index.html')     #Flask will automatically understand that this index.html file is on templates folder


class BillFormPage(MethodView):     
    
    def get(self):                          #when some one use url of BillFormPage then this Get method is executed
        bill_form = BillForm()              #initializing bill_form
        return render_template('bill_form_page.html', 
                               billform=bill_form)      #render_template connects python with html page by using {{}} in html


    def post(self):                             # As get method is use to get from webpage same way post method is use to post data on webpage
                                                # when calculate button is clicked then this post request
        billform = BillForm(request.form)       # To extract data we use request.form 
        amount = float(billform.amount.data)    # we put float because it was showing in calculation part as str / str           # To extract data out of billform and store it in amount instance
        period = billform.period.data

        name1= billform.name1.data
        days_in_house1 = float(billform.days_in_house1.data)          # As we want float value for calculation not string Because in class BillForm(Form): we have declared everyting as string.

        name2= billform.name2.data
        days_in_house2 = float(billform.days_in_house2.data)

        the_bill = flat.Bill(amount, period)         # In flat.py ->class Bill = imported file of flat.py (the CLI interface of flatmate's bill)
        flatmate1 = flat.Flatmate(name1, days_in_house1)
        flatmate2 = flat.Flatmate(name2, days_in_house2)
        
        return render_template('bill_form_page.html',
                               result=True,
                               billform=billform, 
                               name1=flatmate1.name,
                               amount1=(round(flatmate1.pays(the_bill, flatmate2), 2)),
                               name2=flatmate2.name,
                               amount2=(round(flatmate2.pays(the_bill, flatmate1), 2)))        


class BillForm(Form):

    amount = StringField("Bill Amount: ", default="1000")              # we created label and textbox from our python code and just refer this in html file by {{billform.amount.label}} <--for label {{billform.amount}} <--for textbox
    period = StringField("Bill Period: ", default="April 2021")       # {{billform.period.label}} to create label ,  {{billform.period}} to create textbox

    name1 = StringField("Name: ", default="Deeshant")
    days_in_house1 = StringField("Days in the house: ", default=25)

    name2 = StringField("Name: ", default="XYZ")
    days_in_house2 = StringField("Days in the house: ", default=19)    

    button = SubmitField("Calculate the Bill")                                 #we are creating button by using SubmitField class



# Assigning url for Each classes
# app is instance of Flask class
app.add_url_rule('/', view_func=HomePage.as_view('home_page'))                  #When url will contaion only '/'  --> Homepage 
#'/' e.g. www.flatmatebill.com/       # .as_view is a method of MethodView class we are using it by inheritance.

app.add_url_rule('/bill_form_page', view_func=BillFormPage.as_view('bill_form_page'))
#'/bill' e.g. www.flatmatebill.com/bill_form_bill


app.run(debug=True)


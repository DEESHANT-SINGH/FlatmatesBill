class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill.
    """

    def __init__(self, amount, period):      #Constructor
        self.amount = amount                 #Instance variables
        self.period = period


class Flatmate:
    """
    Create a flatmate person who lives in the flat and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):                      # Method
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)    # weight is local variable
        to_pay = bill.amount * weight
        return to_pay
class Products:
    
    def __init__(self, name, type, amount = 0):
        self.name = name
        self.type = type
        self.amount = amount

    def info(self):
        return f"Sveiki mani sauc {self.name}. Man ir {self.type} gadi. Es esmu {self.amount}"
    
    def name_change(self, new_product_name):
        self.name = new_product_name

    def type_change(self):
        if self.type == "Auglis":
            self.type = "Dārzenis"
        elif self.type == "Dārzenis":
            self.type = "Ābols"
        elif self.type == "Ābols":
            self.type = "Auglis"

    def amount_change(self, new_product_amount):
        self.amount = new_product_amount
    
    def jam(self, jam_amount):
        self.amount = self.amount-jam_amount*2
    
    def name_repeater(self):
        return self.name

    def amount_repeater(self):
        return self.amount
    
    def type_repeater(self):
        return self.type

    def amount_adder(self, amountading):
        self.amount = int(self.amount) + int(amountading)
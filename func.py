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
            self.type = "Auglis"

    def amount_change(self, new_product_amount):
        self.amount = new_product_amount

# class Women(Person):
    
#     def __init__(self, name, haircolor, age = 0):
#         super().__init__(name,"S", age)
#         self.haircolor = haircolor

# class Men(Person):
    
#     def __init__(self, name, hobby, age = 0):
#         super().__init__(name,"S", age)
#         self.hobby = hobby
class Pizza:
    brand = "Pizza Palace"

    def __init__(self, topping):
        self.topping = topping

    def describe(self):
        return f"This is a {self.topping} pizza from {self.brand}."

    @classmethod
    def change_brand(cls, new_brand):
        cls.brand = new_brand
        return f"Brand updated to {cls.brand}!"

p1 = Pizza("Margherita")
p2 = Pizza("Pepperoni")

print(p1.describe())
print(Pizza.change_brand("Slice Heaven"))
print(p2.describe())

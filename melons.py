"""Classes for melon orders."""

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""
    
    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species.lower() == "christmas":
            base_price = base_price *1.5
            
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True
    


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "domestic", 0.08)
        

    # self.species = species
    #     self.qty = qty
    #     self.shipped = False
    # order_type = "domestic"
    # tax = 0.08

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    
    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, "international", 0.17)

        # self.species = species
        # self.qty = qty
        self.country_code = country_code
        # self.shipped = False
    # order_type = "international"
    # tax = 0.17

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order."""
     
    def __init__(self, species, qty):
        super().__init__(species, qty, "government", 0)
        self.passed_inspection = False #default value for all government melons

    def mark_inspection(self, passed): #boolean input (True or False)
        """Record if melon has passed government inspection"""

        self.passed_inspection = passed #value after running mark_inspection method
        

            

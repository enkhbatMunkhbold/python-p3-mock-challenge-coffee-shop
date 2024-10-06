class Coffee:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, "name") and 3 <= len(name):
            self._name = name
        else:
            raise Exception
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list({order.customer for order in Order.all if order.coffee is self})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        prices = [order.price for order in Order.all if order.coffee is self]
        return sum(prices) / len(prices)

class Customer:
    all = []
    
    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 0 < len(name) <= 15:
            self._name = name
        else:
            raise Exception
           
    def orders(self):
        return [order for order in Order.all if order.customer is self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        customers_orders = {}
        all_orders = [order for order in Order.all if order.coffee is coffee]
        for order in all_orders:
            if order.customer not in customers_orders:
                customers_orders[order.customer] = order.price
            else:
                customers_orders[order.customer] += order.price

        # return max(customers_orders, key=customers_orders.get)
        return customers_orders

    
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise Exception

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if isinstance(price, float) and 1.0 <= price <= 10.0 and not hasattr(self, "price"):
            self._price = price
        else:
            raise Exception
        

breakpoint()
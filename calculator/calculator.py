class Calculator:

    def __init__(self):
        self.first_number: float = float(input("Enter First Number: "))
        self.second_number: float = float(input("Enter Second Number: "))
    
        self.operation = int(input("1: Add\n"
                           "2: Substract\n"
                           "3: Multiply\n"
                           "4: Division\n"
                           "Enter the Corresponding Number (1,2,3,4): "))

    def add(self,first_number, second_number) -> float:
        return first_number + second_number
    
    def substract(self, first_number: float, second_number: float) -> float:
        return first_number - second_number
    
    def multiply(self, first_number, second_number) -> float:
        return first_number * second_number
    
    def division(self, first_number, second_number) -> float:
        return first_number / second_number

    def calculate(self):
        if (self.operation == 1):
            print(self.add(self.first_number, self.second_number))
        elif (self.operation == 2):
           print(self.substract(self.first_number, self.second_number))
        elif (self.operation == 3):
            print(self.multiply(self.first_number, self.second_number))
        elif (self.operation == 4):
            print(self.division(self.first_number, self.second_number))
        else:
            print("Invalid Operation!")


calculator = Calculator()
calculator.calculate()

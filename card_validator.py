class CardValidator:
    # def __init__(self):
    sum= 0
    result =0
    total= 0
    def count_card_number(self,card_number):
        count = 0
        for i in card_number:
            count = count + 1
        return count

    def sum_of_second_numbers (self,card_number):
        for i in range(len(card_number)-2,-1,-2):
            self.sum += int(card_number[i])
        return self.sum

    def multiple_backwards(self,card_number):
        method_sum= 0
        for i in range(len(card_number)-1, -1,-2):
            multiplied = int(card_number[i]) * 2       
            if multiplied >9 :
                number = str(multiplied)
                method_sum = 1+ int(number[1])
                self.result = self.result +method_sum
            else:
                self.result = self.result+ multiplied
        return self.result 

    def card_type(self, card_number):
        
        if card_number[0] == "4":
            print("Visa card")
        elif card_number[0] == "5":
            print("MasterCard ")
        elif card_number[0] == "6":
            print("Discover cards")
        elif card_number[0] == "3" and card_number[1]== "7":
            print("American Express Cards")
        else:
            print("Invalid card type")

    def validity (self,):4388576018410707
        self.total = self.sum + self.result
        # return self.total
        number_two = self.total% 10
        if number_two == 0:
            return "is valid"
        else: 
            return "is not valid"


card = CardValidator()
number = input("Enter your card number ")
print("multiple backwards is : ",card.multiple_backwards(number))
print("sum_of_second_numbers is : ",card.sum_of_second_numbers(number))
card.card_type(number)
print("The card",card.validity())



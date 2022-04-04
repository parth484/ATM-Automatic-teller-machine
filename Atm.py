class Atm:
    def _init_(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
     #ATM

    def check_balance(self):
        print("Your balance is 100000")

    def withdrawl(self,amount):
        new_amount = 100000 - amount
        print("you have withdrawn amount"+str(amount)+"Your'e remaining amount is"+ str(new_amount))


def main():
    Card_number = input("Enter your card number :")
    pin_number  = input("Enter your pin number :")


    new_user = Atm(Card_number , pin_number)

    print("choose your activity")
    print(" 1.Check Balance  2.withdrawl")
    activity= int(input("Enter activity number :"))

   
    if (activity ==1):
        new_user.check_balance()
    elif (activity ==2):
        amount = int(input("Enter the amount :"))
        new_user.withdrawl(amount)
    else:
        print("Enter a valid number ")


print("This Projects is named as ATM , You can check your bank balance and withdrawl amount.......")
print("This project was done by Y.Yasaswini Lakshmi........")
print("Special Thanks to my teacher Arti Pramod Barge......")


if __name__== "__main__":
    main()

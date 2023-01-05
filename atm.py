
# print("welcome to hdfc")   
# print("please insert your card")
# language=input("enter the language:")
# current_balance=25000
# if language=="english" or "hindi" or "kannada" or "telugu":
#     password=int(input("enter the pin"))
#     pin=1234
#     if pin==password:
#         menu=input("select the option:")
#         if menu=="current":
#             if current_balance>0:
#                 print(current_balance)
#             else:
#                 print("zero balance")
#         elif menu=="withdrawl":
#             withdrawal_amount=int(input("enter the amount"))
#             if withdrawal_amount<=current_balance: 
#                 print(current_balance-withdrawal_amount)
#             else:
#                 print("insuffcient balance")
#         elif menu=="deposit":
#             deposit_amount=int(input("enter the deposit amount"))
#             if deposit_amount>0:
#                 print(current_balance+deposit_amount)
#             else:
#                 print(current_balance)
#         else:
#             print("please enter correct menu")
#     else:
#         print("please enter valid pin")
# else:
#     print("select another ")


# print("well come to sbi")
# print("insert your card")
# langauge=input("enter the langauge")
# current_balance=2500
# if langauge=="english":
#     password=int(input("enter the pin"))
#     pin=1234
#     if pin==password:
#         menu=input("enter the menu")
#         if menu=="current":
#             if current_balance>0:
#                 print(current_balance)
#             else:
#                 print("zero amount")
#         elif menu=="withdraw":
#             withdraw_amount=int(input("enter the amount"))
#             if withdraw_amount<=current_balance:
#                 print(current_balance+withdraw_amount)
#             else:
#                 print("insufficience")
#         elif menu=="deposit":
#             deposit_amount=int(input("enter the amount"))
#             if deposit_amount>0:
#                 print(current_balance+deposit_amount)
#             else:
#                 print("current_balance")
#         else:
#             print("entr correct menu")
#     else:
#         print("entr correct password")
# else:
#     print("enter the correct language")


print("well come to sbi")
print("please insert your card")
language=input("enter the langauge")
current_balance=3500
if language=="english":
    password=int(input("enter the pin"))
    pin=1234
    if pin==password:
        menu=input("enter the menu")
        if menu=="current":
            if current_balance>0:
                print(current_balance)
            else:
                print("zero amount")
        elif menu=="withdraw":
            withdraw_amount=int(input("enter the amount"))
            if withdraw_amount<=current_balance:
                print(current_balance-withdraw_amount)
            else:
                print("in sufficient")
        elif menu=="deposit":
            deposit_amount=int(input("enter the amount"))
            if deposit_amount>0:
                print(current_balance+deposit_amount)
            else:
                print("current balance")
        else:
            print("enter correct")
    else:
        print("corect")
else:
    print("correct")
        
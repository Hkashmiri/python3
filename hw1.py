# add your code here please
transactionAmount = input("Enter transaction amount: ")
amountPaid = input("Enter amount paid: ")
change = float(amountPaid) - float(transactionAmount)
total_change = float(amountPaid) - float(transactionAmount)
twenty_dollars = round(change // 20)

change = change % 20

ten_dollars = round(change // 10)

change = change % 10

five_dollars = round(change // 5)

change = change % 5

one_dollars = round(change // 1)

change = change % 1

quarter_dollar = round(change // .25)

change = change % .25

dime_dollar = round(change // .10)

change = change % .10

nickel_dollar = round(change // .05)

change = change % .05

penny_dollar = round(change // .01)

change = change % .01

# Print the results

print(f"Change due is: {total_change}")

print(f"You need {twenty_dollars} - $20")

print(f"You need {ten_dollars} - $10")

print(f"You need {five_dollars} - $5")

print(f"You need {one_dollars} - $1")

print(f"You need {quarter_dollar} - $0.25")

print(f"You need {dime_dollar} - $0.10")

print(f"You need {nickel_dollar} - $0.05")

print(f"You need {penny_dollar} - $0.01")
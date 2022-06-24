#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print('Wellcome to Tip Calculator!')
bill = float(input("How much was the bill? $"))
percent = int(input("What percentage of tip? 10, 12 and 15 ? "))
people = int(input("How many people to split the bill? "))

s = bill * (percent/100)
s1=s + bill
s2=s1/people
s3=round(s2,2)
print(f'Each person should pay ${s3}')

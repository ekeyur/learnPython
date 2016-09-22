total = raw_input("Total bill amount? ")
service = raw_input("Level of service? (good,fair,bad) ")
split = raw_input("Split how many ways? ")

if service == "good":
    tip_amount = float(total) * 0.2
elif service == "fair":
    tip_amount = float(total) * 0.15
else:
    tip_amount = float(total) * 0.1

print "Tip amount: $%.2f" % tip_amount

tip_total = float(total) + tip_amount

print "Total amount: $%.2f" % tip_total

per_person = tip_total / float(split)

print "Amount per person: $%.2f" % per_person

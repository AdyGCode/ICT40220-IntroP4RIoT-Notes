# Set total to 0
total = 0
# set price to $22.5 (try using 20, 22.5 and 25)
price = 22.5

# Add the price ot the total, plus GST at 15%
total = total + price + price * 0.15

if total < 25:
    # add surcharge for totals under $25
    total = total + 5
else:
    # give $5 discount for totals $25 or over
    total = total - 5

# Display total
print(total)

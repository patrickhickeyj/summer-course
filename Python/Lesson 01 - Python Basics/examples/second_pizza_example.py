PI = 3.14
diameter_small = float(input("Choose a diameter for Small Pizzas "))
radius_small = diameter_small / 2
area_small = PI * radius_small ** 2
total_area_small = area_small * 2

diameter_large = float(input("Choose a diameter for the Large Pizza "))
radius_large = diameter_large / 2
area_large = PI * radius_large ** 2


cost_small = float(input("What is the cost of the small pizzas (total)? "))

cost_large = float(input("What is the cost of the large pizza? "))

ppa_small = cost_small / total_area_small
ppa_large = cost_large / area_large

print(f"Small price per: {ppa_small:.4f}")
print(f"Large price per: {ppa_large:.4f}")

if (ppa_large < ppa_small):
    print("Large pizza is better deal")
elif (ppa_small < ppa_large):
    print("Small pizza is better deal")
else:
    print("They are the same value")


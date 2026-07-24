
"""
Rent Calculator
1. Input from user 
2. Input  function & Data types
3. Room rent
4. Food 
5. Electricity 
6. per unit
7. total_bill = electricity * per unit 
8. persons living in room 
9. total monthly rent (room rent + food + total_bill) // Per_persons 
10. print(One month bill per person)
"""

room_rent = int(input("Enter the room rent: "))
food = int(input("Enter the food amount: "))
electricity = int(input("Enter the electricity bill amount: "))
per_unit = int(input("Per Unit charges: "))
persons = int(input("Enter the persons in room: "))

total_bill = electricity * per_unit

total_monthly_room_rent = (room_rent + total_bill + food) // persons

print(f"Monthly room rent per_persons: {total_monthly_room_rent} Tk")

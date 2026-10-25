# Task 7 - Travel Planner
destination = input("Enter destination: ")
distance = float(input("Enter distance in km: "))
speed = float(input("Enter average speed in km/h: "))
time = distance / speed
print("Destination:", destination)
print("Estimated Travel Time:", time, "hours")
"""
# Bonus: show in hours and minutes(this is a bonus inorder to run it uncomment it)
hours = int(time)
minutes = int((time - hours) * 60)
print("That is", hours, "hours and", minutes, "minutes")
"""
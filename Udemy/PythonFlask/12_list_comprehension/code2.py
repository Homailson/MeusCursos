friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]

starts_s = [name for name in friends if name[0].lower() == "s"]

print(starts_s)

starts_s = [name for name in friends if name.lower().startswith("s")]

print(starts_s)
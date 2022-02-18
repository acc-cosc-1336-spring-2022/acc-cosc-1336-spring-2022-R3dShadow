import decisions


options = int(input('Input number for options'))
total = float(input ('Input dividend'))

result = decisions.get_options_ratio(options, total)

print(decisions.get_faculty_rating((result)))
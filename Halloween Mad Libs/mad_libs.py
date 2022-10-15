
def mad_libs_one():
	holiday = input("Enter a holiday: ")
	noun = input("Enter a noun: ")
	place = input("Enter a place: ")
	person = input("Enter a person: ")
	adjective = input("Enter a adjective: ")
	plural_body_part = input("Enter a plural body part: ")
	verb = input("Enter a verb: ")
	adjective_two = input("Enter a second adjective: ")
	noun_two = input("Enter a noun: ")
	food = input("Enter a food: ")
	plural_noun = input("Enter a plural noun: ")

	print(f"I can't believe it\'s already {holiday}! I can't wait to put on my {noun} and visit every {place} in my neighborhood. This year, I am going to dress up as a {person} with {adjective} {plural_body_part}. Before I {verb}, I make sure to grab my {adjective_two} {noun_two} to hold all of my {food}. Finally, all of my {plural_noun} are ready to go!")


def main():
	mad_libs_one()
	# TODO Add more stories to this program for later.

if __name__ == '__main__':
	main()
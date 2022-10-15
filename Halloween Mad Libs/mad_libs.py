def mad_libs_one():
    holiday = input("Enter a holiday: ")
    noun = input("Enter a noun: ")
    place = input("Enter a place: ")
    person = input("Enter a person: ")
    adjective = input("Enter an adjective: ")
    plural_body_part = input("Enter a plural body part: ")
    verb = input("Enter a verb: ")
    adjective_two = input("Enter a second adjective: ")
    noun_two = input("Enter a noun: ")
    food = input("Enter a food: ")
    plural_noun = input("Enter a plural noun: ")
    print(
        f"I can't believe it's already {holiday}! I can't wait to put on my {noun} and visit every {place} in my neighborhood. This year, I am going to dress up as a {person} with {adjective} {plural_body_part}. Before I {verb}, I make sure to grab my {adjective_two} {noun_two} to hold all of my {food}. Finally, all of my {plural_noun} are ready to go!"
    )


def mad_libs_two():
    plural_noun = input("Enter a plural noun: ")
    plural_noun_two = input("Enter a plural noun: ")
    noun = input("Enter a noun: ")
    noun_two = input("Enter a noun: ")
    noun_three = input("Enter a noun: ")
    plural_noun_three = input("Enter a plural noun: ")
    adjective = input("Enter a adjective: ")

    # Second part of the mad libs
    adjective_two = input("Enter an adjective: ")
    noun_four = input("Enter a noun: ")
    adjective_three = input("Enter an adjective: ")
    adjective_four = input("Enter an adjective: ")
    plural_noun_four = input("Enter a plural noun: ")
    plural_noun_five = input("Enter a plural noun: ")
    adjective_five = input("Enter an adjective: ")
    noun_five = input("Enter a noun: ")

    # Final part
    verb = input("Enter a verb: ")
    plural_noun_six = input("Enter a plural noun: ")
    plural_noun_seven = input("Enter a plural noun: ")
    adverb = input("Enter an adverb: ")
    verb_two = input("Enter a verb: ")
    noun_six = input("Enter a noun: ")
    noun_seven = input("Enter a noun: ")
    noun_eight = input("Enter a noun: ")
    verb_three = input("Enter a verb that ends in s: ")

    print(
        f"Halloween is my favorite, because we get to dress up in {plural_noun} and visit {plural_noun_two} in our {noun} saying \"{noun_two} or {noun_three}\"! In exchange for a bag of {plural_noun_three}. It's so {adjective}! This year, I'm going to dress up as a(n) {adjective_two} {noun_four} my costume is going to be so {adjective_three}! It will be made with {adjective_four} {plural_noun_four} and {plural_noun_five}, so it's sure to win the {adjective_five} {noun_five} contest! I also love to {verb} {plural_noun_five} for Halloween! I use special carving {plural_noun_six} to {adverb} {verb_two} a face into my {noun_six} then, we put a {noun_seven} inside and light it so that the {noun_eight} {verb_three}! Spooky!"
    )


def mad_libs_three():
    pass


def main():
    mad_libs_two()
    # TODO Add more stories to this program for later.


if __name__ == "__main__":
    main()

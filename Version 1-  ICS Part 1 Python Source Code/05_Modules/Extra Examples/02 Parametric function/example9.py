# Title: Check Vote Eligibility

def can_vote(name, age):
    if age >= 18:
        print(name, "is eligible to vote.")
    else:
        print(name, "is not eligible to vote.")

can_vote("Sara", 17)

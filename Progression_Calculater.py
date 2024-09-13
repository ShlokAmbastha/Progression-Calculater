print(f"Hello, I am a series calculater. How can I help you? I can help with A.P. (Arithmetic Progression), G.P. (Geometric Progression), and H.P. (Harmonic Progression).")

while True:
    Series_type = input("What series are you working with? (A.P. / G.P. / H.P.): ")

    # Working with A.P.
    if Series_type.lower() == "a.p.":
        # Getting the fundamentals.
        First_term = float(input("Enter the first term: "))
        Second_term = float(input("Enter the second term: "))
        Difference = Second_term - First_term
        print("The Difference is", Difference)

        # What do they want?
        Answer2 = input("Do you want to find the nth term, sum, or the whole series? (nth term / sum / series): ")

        # Calculating.
        if Answer2.lower() == "nth term":
            number = int(input("What's n?: "))
            nth = First_term + (number - 1) * Difference
            print(f"The {number}th term is: {nth}")

        elif Answer2.lower() == "sum":
            number = int(input("What's the nth term?: "))
            Sum = number / 2 * (2 * First_term + (number - 1) * Difference)
            print(f"The sum of the first {number} terms is: {Sum}")

        elif Answer2.lower() == "series":
            n = int(input("How many terms do you want?: "))
            print(f"The first {n} terms of the A.P. are:")
            for i in range(n):
                print(First_term + i * Difference)

        else:
            print("Incorrect answer, please try again!")

    # Working with G.P.
    elif Series_type.lower() == "g.p.":
        # Getting the fundamentals.
        First_term = float(input("Enter the first term: "))
        Second_term = float(input("Enter the second term: "))
        Ratio = Second_term / First_term
        print("The Ratio is", Ratio)

        # What do they want?
        Answer2 = input("Do you want to find the nth term, sum, or the whole series? (nth term / sum / series): ")

        # Calculating.
        if Answer2.lower() == "nth term":
            number = int(input("What's n?: "))
            nth = First_term * Ratio ** (number - 1)
            print(f"The {number}th term is: {nth}")

        elif Answer2.lower() == "sum":
            number = int(input("What's the nth term?: "))
            if Ratio == 1:
                Sum = First_term * number
            else:
                Sum = First_term * (1 - Ratio ** number) / (1 - Ratio)
            print(f"The sum of the first {number} terms is: {Sum}")

        elif Answer2.lower() == "series":
            n = int(input("How many terms do you want?: "))
            print(f"The first {n} terms of the G.P. are:")
            for i in range(n):
                print(First_term * Ratio ** i)

        else:
            print("Incorrect answer, please try again!")

    # Working with H.P. (Harmonic Progression)
    elif Series_type.lower() == "h.p.":
        # Getting the fundamentals (reciprocal of A.P.)
        First_term = float(input("Enter the first term of the corresponding A.P.: "))
        Second_term = float(input("Enter the second term of the corresponding A.P.: "))
        Difference = Second_term - First_term
        print("The Difference in A.P. terms is", Difference)

        # What do they want?
        Answer2 = input("Do you want to find the nth term, sum, or the whole series? (nth term / sum / series): ")

        # Calculating.
        if Answer2.lower() == "nth term":
            number = int(input("What's n?: "))
            nth_ap = First_term + (number - 1) * Difference
            nth_hp = 1 / nth_ap
            print(f"The {number}th term of the H.P. is: {nth_hp}")

        elif Answer2.lower() == "sum":
            print("Sum calculations for H.P. are complex and require advanced formulas.")

        elif Answer2.lower() == "series":
            n = int(input("How many terms do you want?: "))
            print(f"The first {n} terms of the H.P. are:")
            for i in range(n):
                ap_term = First_term + i * Difference
                hp_term = 1 / ap_term
                print(hp_term)

        else:
            print("Incorrect answer, please try again!")

    else:
        print("Incorrect series type, please try again!")

    # Ask if they want to calculate again
    repeat = input("\nWould you like to repeat this program? (yes/no): ")
    if repeat.lower() != 'yes':
        print("Goodbye!")
        break
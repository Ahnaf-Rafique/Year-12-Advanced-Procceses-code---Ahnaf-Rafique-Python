# Input

# instructions
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please answer yes / no")


def instructions():
    print("**** Welcome to the people in need association, This app will help you to proceed and start a living. ****")
    print("**** The app will ask you a lot of personal questions please respond, if you are not comfortable you may leave. ****")
    print("**** Lastly, please share this program to others in need. If you do not proceed and approve of these terms, please leave the program. ****")
    print()
    return ""


# output
show_instructions = yes_no("Have you done a program like this before? ")

if show_instructions == "no":

    instructions()

print("program continues")

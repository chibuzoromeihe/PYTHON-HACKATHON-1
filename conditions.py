# This code checks the age eligibility of a user to vote or not to vote
def vote_eligibility_check(age):
    
    if age >= 18: # using if statement to check if the age is greater than or equal to 18
         
        print("Congratulations! You are eligible to vote."); # the condition is true, print a message indicating eligibility
        
    else:
        print("🚫 Sorry! You are not eligible to vote.");
        
def main():
    # A welcome message for the user
    print("welcome to the Age Eligibilty check.");
    
    try:
        age = int(input("Please! enter your age: ")); # prompt user to provide their age
        
        vote_eligibility_check(age) #here, we call the function to check the eligibilty of the entered age.
        
    except ValueError: #
        #if the user enters a non-interger number.
        print("Oops❗️ invalid input, enter a valid age.")
        
main()  # callthe main function
        
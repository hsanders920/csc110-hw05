"""
Name: Hannah Sanders
Peers: (add any collaborators)
References: 
"""

def get_letter():
    """the function first defines a list of letters: letts
    it prompts the user for a uppercase letter and converts input into string
    if the length of the input is greater than one then the function returns an error
    if the input is not in the list letts, the function returns an error message
    """
    # remove the default return and add your code
    letts = ["A","B","C"]
    while True:
        let= str(input("Give an single uppercase letter: "))
        lenLet= len(let)
        if lenLet != 1:
            print("Error: it needs to be a single character.")
            continue
        elif let not in letts:
            print("Error: You provided the wrong character.")
            continue
        return let
        break
            
   

def get_digit():
    """ the function first defines a list of numbers: nums
    it prompts the user for a number and converts input into string
    if the input is not a digit, the function returns an error
    if the input is not in the list nums, the function returns an err """
    nums = ["1","2","3"]
    while True:
        num = str(input("Give an single number character: "))
        #define var as str for searching purposes
        
        if not num.isdigit():
            print("Error: your input should be only digits.")
            continue
        if num not in nums:
            print("Error: a single digit needs to be in [1,3].")
            continue
        else:
            return num
        break
    


def check_pattern(let, num, st_list):
    """ for every  str in the list, the function checks to see if
    the letter is in it. 
    The function then checks to see if the number is in the str.
    It then goes through every charecter in the string checking to see if the
    charecter is the letter.
    If it is then the function will store the index value as the current step i it has taken through searching the string.
    The function breaks after it finds the first instance.
    This same process is repeated for num, storing its idx value in a different variable.
    If the idx of the first instance of num is greater than the idx of the first instance of let
    (the number comes after the letter), then the string will print and leave a space for any other true strings
    """
    
    print("Strings with the pattern:", end=" ")
    
    for st in st_list:
        if let in st:
            if num in st:
                Tstr= st
                
                for i in range(len(Tstr)):
                    charnow= Tstr[i]
                    if charnow == let:
                        idxlet= i
                        break #breaks so that i does not = the last instance of the let (finishes going through every char)
                for i in range(len(Tstr)):
                    charnow= Tstr[i]
                    if charnow == num:
                        idxnum=i
                        break #breaks so that i does not = the last instance of the let (finishes going through every char)
                if idxnum> idxlet:
                      print(Tstr, end= " ")
        


#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ Calls get_letter(), get_digit() and check_pattern()
    after all 3 have been called will prompt the user if they want to continue
    if yes (input y), then the loop will continue to the begining and the process will restart
    if no (input n) the while loop will be broken out from and 'the end' will print"""
   
    
   

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]
    while True:
        let = get_letter()
        num = get_digit()
        
        check_pattern(let, num, st_list) #calls the returned values of let, num and st_list 
        TA=input("\nTry Again? (y/n):") #on a new line bc of previous end="" on print statement
        if TA == "y":
            continue
        else:
            break 
    print("The End")

    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------

    # Your code Here

    # -------------------------------------------------
    # No need to modify anything Below this line
    
    

# Do not modify these two lines
if __name__ == "__main__":
    main()

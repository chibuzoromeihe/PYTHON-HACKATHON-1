# This program generates the Fibonacci sequence of a specified term n
def To_generate_fibonacci_sequence(n):
    
    fibonacci_sequence = [0, 1] #initializes the Fibonacci sequence with the firstterms (0 and 1)
    
    #looping to generate subsequent terms of the fibonacci sequence
    for x in range(2, n):
        
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2] #calculate the next term by adding the last two terms
        
        #To append the next term to the sequence
        fibonacci_sequence.append(next_term)
        
    return fibonacci_sequence[: n] #This returns the first terms of the fibonacci sequence

def main():
    n = int(input("Enter the number of terms 'n' for fibonacci sequence: "));# Ask user to provide the value of n
    
    fibonacci_sequence = To_generate_fibonacci_sequence(n); # generating the fibonacci sequence
    
    print("Fibonacci Sequence : ");
    print(fibonacci_sequence);
    
main()
    
    
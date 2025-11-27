#Write a script with these tasks:
#Ask user for a list of numbers
#Print even numbers only
#Print sum of odd numbers
#Find the index of highest number manually (no max)
#Reverse the list manually (no slicing)

def process_numbers(numbers):
    even_number = []#declaring an empty array to add even numbers to it
    sum_odd = 0 #declaring a variable initializing with sum=0, to sum the odd numbers from the input list

    for num in numbers:
        #Print even numbers only
        if num % 2 == 0 : #check if number is even
           even_number.append(num) # append to the even_numbers array
        #Print sum of odd numbers
        else :
            sum_odd += num #add sum_odd with the odd number

    #Find the index of highest number manually (no max)
    highest_index = 0 #making the highest index = 0 initially to traverse the array and compare
   
    for i in range(1, len(numbers)): #traversing i from 0 to end of list
        if numbers[i] > numbers[highest_index]: #comparing each number with highest_index no
            highest_index = i #if the number is > highest_index number, storing it in highest_value
            
    #Reverse the list manually (no slicing)
    reversed_list = [] #declaring an empty list to append the reversed values from the original list 
    for i in range(len(numbers)-1, -1, -1): # range(start, stop, step)
        reversed_list.append(numbers[i])
    
    return even_number, sum_odd, highest_index, reversed_list

if __name__ == "__main__":
    raw = input("Enter numbers separated by space:")
    numbers = list(map(int, raw.split()))
    evens, sum, highest_index, reversed_list = process_numbers(numbers)

    print("Even numbers:", evens)
    print("Sum of odd numbers:", sum)
    print("Index of highest value:", highest_index)
    print("Reversed list:", reversed_list)



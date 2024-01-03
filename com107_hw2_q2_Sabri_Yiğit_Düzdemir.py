first_input_number = (input("Please choose the first 3 digit number :"))
second_input_number = (input("Please choose the second 3 digit number :"))

if first_input_number == first_input_number[::-1] and second_input_number == second_input_number[::-1]:
    sum = int(first_input_number) + int(second_input_number)
    print("these numbers are palindromic so the result is :",sum)
elif (first_input_number == first_input_number[::-1] and second_input_number != second_input_number[::-1]) or (first_input_number != first_input_number[::-1] and second_input_number == second_input_number[::-1]):
    sub = abs(int(first_input_number) - int(second_input_number))  
    print("one of the numbers are palinromic so the result is :",sub)
else :
    first_input_number != first_input_number[::-1] and second_input_number != second_input_number[::-1] 
    mult = int(first_input_number) * int(second_input_number)
    print("there is no palindromic numbers here so the result is :",mult)     
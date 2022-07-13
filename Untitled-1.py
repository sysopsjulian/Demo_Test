
# # Create a program to find the positions\locations of the numbers whose addition is equal to input number.
# # arr num={9,5,7,3,12,18}
# # input =12
# # arr num ={18,8,12,9,11,21}
# # Sort the above array in ascending order
# # Note-  For the above programs you will need to write the full logic and 
# # you cannot use any pre-defined function.
 
# num_list = [9,5,7,3,12,18];
# # print(num_list[2])
# for num in num_list:
#    # print(num)
#    count = 0
#    for indx in range(1, len(num_list)+ 1):
#         if num_list[indx - 1] == num:
#             print("This is the current value of num which is ",num)
#             continue;
#         res = num_list[count + 1] + num
#         count+= 1
#         print(res)
    
    

#     # print(num)
#     # print(num_list.index(num))

#     # find the index of any two values(num)
#     # if sum of values(num) is equal to 12 - true
#     # print index of the two values(num)
# Problem 1
num_list = [9,5,7,3,12,18]
for num0 in num_list:
    for num1 in num_list:
        if num0 == num1:
            continue
        result= num0 + num1
        if result == 12:
            print(f"Element: {num0}, has an index of {num_list.index(num0)}.", end=" ")
            print(f"Element: {num1}, has an index of {num_list.index(num1)}.")

# Problem 2


num_list_02 = [18,8,12,9,11,21]
num_list_02.sort()
print(num_list_02)





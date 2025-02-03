
# def sum_numbers(a, b):
#     return a + b

# def minutes_to_seconds(minutes):
#     return minutes * 60

# def is_ten_or_sum_ten(a, b):
#     return a == 10 or b == 10 or (a + b) == 10

# def are_lengths_equal(str1, str2):
#     return len(str1) == len(str2)

# def largest_number(numbers):
#     if numbers:  
#         return max(numbers)
#     return None 

# def char_count(char, string):
#     return string.lower().count(char.lower())



# def reverse_string(string):
#     return string[::-1]

# def multiply_by_two_and_print(n):
#     for i in range(n + 1):
#         print(i * 2, end=" ")

# def greatest_of_three(a, b, c):
#     return max(a, b, c)

# def count_vowels(string):
#     vowels = "aeiou"
#     count = 0
#     for char in string.lower():
#         if char in vowels:
#             count += 1
#     return count


# print(sum_numbers(3, 7))  
# print(minutes_to_seconds(5)) 
# print(is_ten_or_sum_ten(6, 4))  
# print(are_lengths_equal("hello", "world"))  
# print(largest_number([10, 40, 30, 20, 50]))  
# print(char_count("c", "Chamber of secrets"))  
# print(count_vowels("Celebration")) 
# print(reverse_string("Happy Birthday"))  
# multiply_by_two_and_print(5) 
# print(f"{greatest_of_three(4, 8, 2)} is greatest")  

char=input("Enter any character: ")
if char.isalpha()==False:
    print("Not a character")
elif char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
    print("Vowel")
else:
    print("Consonant")
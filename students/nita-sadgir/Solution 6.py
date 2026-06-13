#problem
#leap year
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


print(is_leap_year(2000))  
print(is_leap_year(1900)) 
print(is_leap_year(2024))  
print(is_leap_year(2023)) 


#proble 2
#sum numbers
def sum_to_n(n):
    total = 0 

    for i in range(1, n + 1):
        total += i

    return total


print(sum_to_n(5))   
print(sum_to_n(1))  
print(sum_to_n(10))  


#problem 3
#time table
def times_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

times_table(2)

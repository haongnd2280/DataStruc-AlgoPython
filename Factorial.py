def factorial(n): 
    if n == 0: 
        return 1 
    else: 
        return n * factorial(n - 1)

# Each time the function is invoked, its argument is smaller by one. 
# When a base case is reached, no further recursive calls are made. 

# NOTE: When the execution of a function leads to a nested function call, THE EXECUTION OF THE 
# FORMER CALL IS SUSPENDED AND ITS ACTIVATION RECORD STORES "THE PLACE" IN THE SOURCE CODE 
# AT WHICH THE FLOW OF CONTROL SHOULD COUNTINUE UPON (DUA VAO) RETURN OF THE NESTED CALL. 
# This process is used in both the standard case of one function calling a different funciton, 
# or in the recursive case in which a function invoked itself. 
# 
# 
# Activation record / frame: trang 151. luu trang thai hien tai cua ham dang duoc thuc thi (ham 
# hien dang thuc thi den doan nao roi, luu tham so, bien dia phuong, ...) 
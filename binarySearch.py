def binary_search(data, target, low, high): 
    '''
    Return True if target is found in indicated portion of a Python list.
    The search only considers the portion from data[low] to data[high] inclusive.
    '''
    if low > high: 
        return False   # interval is empty; no match. (Ok, da hieu (ve hinh ra)).  
    else: 
        mid = (low + high) // 2 
        if target == data[mid]: 
            print('Gia tri can tim o vi tri index: %d' % (mid))
            return True
        elif target < data[mid]: 
            # recur on the portion left of the middle. 
            return binary_search(data, target, low, mid - 1)  # return True or False (2 base cases).
        else: 
            # recur on the portion right of the middle. 
            return binary_search(data, target, mid + 1, high)  # return True or False (2 base cases).

    # Chu y: duoi hai doan elif, else mang khoi lenh truy hoi, thi khong con khoi lenh nao khac nua. 
    # Vi vay, viec hinh dung flow of control cua thuat toan rat tuong minh, khong bi overlap cac 
    # function call voi nhau. 

# Nhan xet: Voi bai nay, thi viec hinh dung thuat toan rat de, vi cac bai toan con co du lieu
# la non-overlapping voi nhau.  
# Nhac lai hai dang truy hoi: 
# 1. Dynamic programming (overlapping subproblems)
# 2. Divide and conquer (non-overlapping subproblems)

data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
have_solution = binary_search(data, 10, 0, len(data) - 1)
if have_solution == False:
    print('Khong co gia tri can tim trong list.')

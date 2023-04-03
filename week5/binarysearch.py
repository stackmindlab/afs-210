def binary_Search(sorted_List, target_Value):
    low = 0
    high = len(sorted_List) - 1
    mid = len(sorted_List) // 2

    while low <= high:
        mid = low + (high - low) // 2
        if sorted_List[mid] == target_Value:
            return True
        elif sorted_List[mid] < target_Value:
            low = mid + 1
        else:
            high = mid - 1

    return False

sorted_List1 = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
target_Value1 = 31

sorted_List2 = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
target_Value2 = 77

sorted_List3 = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"]
target_Value3 = "Delta"

print(binary_Search(sorted_List1, target_Value1))
print(binary_Search(sorted_List2, target_Value2))
print(binary_Search(sorted_List3, target_Value3))

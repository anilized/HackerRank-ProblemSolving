def bonAppetit(bill, k, b):
    total_correct = (sum(bill) - bill[k]) / 2
    total_wrong = sum(bill) / 2
    if total_correct != b:
        return int(total_wrong - total_correct)
    else:
        return "Bon Appetit"

bill = [3, 10, 2, 9]
k = 1
b = 12

print(bonAppetit(bill,k,b))
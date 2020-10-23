#!/usr/bin/python3
#Ella Adam
#10/8/19


def total(a_list):
    total = 0
    for i in range(len(a_list)):
        total += a_list[i]
    return total

if __name__ == "__main__":
    bill_items = [5.34, 11.15, 7.22, 3.14]
    total_bill = total(bill_items)
print(total_bill)
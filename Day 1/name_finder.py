import random
# import xlrd
# loc = ("names.xlsx") 
# wb = xlrd.open_workbook(loc) 
# sheet = wb.sheet_by_index(0) 
# sheet.cell_value(0, 0) 
# names = []
# for i in range(sheet.nrows): 
#     val = sheet.cell_value(i, 0)
#     names.append(val)
# def find(L, target):
#     start = 0
#     end = len(L) - 1

#     while start <= end:
#         middle = (start + end)/ 2
#         midpoint = L[middle]
#         if midpoint > target:
#             end = middle - 1
#         elif midpoint < target:
#             start = middle + 1
#         else:
#             return midpoint
# print(names)
# name = input("Enter person naa
# me: ")
# print(find(names, name))

raja =[]
name = input("Enter person name: ")
searchfile = open("names.txt", "r")
for line in searchfile:
    if name in line: 
        raja.append(line)

searchfile.close()

if(len(raja) <= 0):
    print("Name not found")
else:
    print(random.choice(raja))

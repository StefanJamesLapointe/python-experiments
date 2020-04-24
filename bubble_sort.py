print("Welcome to Bubble Sort!")
print("Please enter you numbers separated by commas and spaces.")
input = input("Unsorted list: ")
list = input.split(", ")
for i in range(len(list)):
    if float(list[i]) == round(float(list[i])):
        list[i] = int(list[i])
    else:
        list[i] = float(list[i])
def bubble_sort(list):
    

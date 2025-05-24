numberLargest = int(input("Entre the largest number: "))
numberSmallest = int(input("Enter the smallest number: "))
while numberSmallest:
    numberStore = numberSmallest 
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print("HCF is:", numberLargest)
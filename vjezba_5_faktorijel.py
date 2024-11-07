##while petlja

broj = 1
faktorijel = 1

while broj <= 5:
    faktorijel *= broj
    broj += 1

print("Faktorijel broja 5 je:", faktorijel)

#for petlja

index = 1
for i in range(1, 6):  # range(1, 6) gives numbers from 1 to 5
    index *= i
print(index)
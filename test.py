import random as rd

train_data = open("multi_train.txt")
data = []
for line in train_data:
    lstRow = list(map(int, line.split()))
    classf = lstRow[-1]
    data.append((lstRow[:-1], classf))
train_data.close()

print(len(data))

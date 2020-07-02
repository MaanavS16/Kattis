import random as rd


def probgen():
    if rd.randrange(0,4) == 1:
        return True
    return False


def sign(x):
    if x > 0:
        return 1
    return -1


def argmax(x):
    if x[0] >= x[1]:
        return 0
    return 1


train_data = open("train.txt")
data = []
for line in train_data:
    lstRow = list(map(int, line.split()))
    classf = lstRow[-1]
    data.append((lstRow[:-1], classf))
train_data.close()

wrongCount = 0
total = 0

small_data = data[:1000]

solution_acc = []
solutions = []
for l in range(15):

    neuron_weights = []
    for i in range(30):
        neuron_weights.append([])
        for j in range(51):
            if rd.randrange(0, 2) == 0:
                neuron_weights[-1].append(-1)
            else:
                neuron_weights[-1].append(1)

    for i in data:
        one_reducers = []
        zero_reducers = []
        one_boost = []
        zero_boost = []
        neurons_out = []
        for j in range(30):
            sumVal = 0
            for k in range(51):
                if neuron_weights[j][k] != i[0][k]:
                    if j <= 14:
                        zero_reducers.append((j, k))
                    else:
                        one_reducers.append((j, k))
                else:
                    if j <= 14:
                        zero_boost.append((j, k))
                    else:
                        one_boost.append((j, k))
                sumVal += neuron_weights[j][k] * i[0][k]
            neurons_out.append(sign(sumVal))

        sum_nodes = [0, 0]
        for j in range(30):
            if j <= 14:
                sum_nodes[0] += neurons_out[j]
            else:
                sum_nodes[1] += neurons_out[j]
        print(sum_nodes, argmax(sum_nodes))

        if argmax(sum_nodes) == i[1]:
            total += 1
            print("correct")
        else:
            print("wrong")
            total += 1
            wrongCount += 1
            if i[1] == 0:
                for j in zero_reducers:
                    if probgen():
                        neuron_weights[j[0]][j[1]] *= -1
                for j in one_boost:
                    if probgen():
                        neuron_weights[j[0]][j[1]] *= -1
            else:
                for j in one_reducers:
                    if probgen():
                        neuron_weights[j[0]][j[1]] *= -1
                for j in zero_boost:
                    if probgen():
                        neuron_weights[j[0]][j[1]] *= -1
    accuracy = (total - wrongCount) / total
    solution_acc.append(accuracy)
    solutions.append(neuron_weights)
    print(accuracy)

max_acc = 0
for i in solution_acc:
    if i > max_acc:
        max_acc = i

print(solutions[solution_acc.index(max_acc)])
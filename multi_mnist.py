import random as rd


def probgen(x):
    if rd.randrange(0,x) == 1:
        return True
    return False


def sign(x):
    if x > 0:
        return 1
    return -1


def argmax(x):
    maxIndex = 0
    maxVal = 0
    for r in x:
        if r > maxVal:
            maxVal = r
            maxIndex = x.index(r)
    return maxIndex


train_data = open("mnist10_train.txt")
data = []
for line in train_data:
    lstRow = list(map(int, line.split()))
    classf = lstRow[-1]
    data.append((lstRow[:-1], classf))
train_data.close()

wrongCount = 0
total = 0

small_data = data[:5000]

solution_acc = []
solutions = []
for _ in range(1):

    neuron_weights = []
    for i in range(150):
        neuron_weights.append([])
        for j in range(51):
            if rd.randrange(0, 2) == 0:
                neuron_weights[-1].append(-1)
            else:
                neuron_weights[-1].append(1)

    for i in small_data:
        reducers = [[], [], [], [], [], [], [], [], [], []]
        booster = [[], [], [], [], [], [], [], [], [], []]
        neurons_out = []
        for j in range(150):
            sumVal = 0
            for k in range(51):
                #print(j, k)
                if neuron_weights[j][k] != i[0][k]:
                    if j >= 135:
                        reducers[9].append((j,k))
                    elif j >= 120:
                        reducers[8].append((j, k))
                    elif j >= 105:
                        reducers[7].append((j, k))
                    elif j >= 90:
                        reducers[6].append((j, k))
                    elif j >= 75:
                        reducers[5].append((j, k))
                    elif j >= 60:
                        reducers[4].append((j, k))
                    elif j >= 45:
                        reducers[3].append((j, k))
                    elif j >= 30:
                        reducers[2].append((j, k))
                    elif j >= 15:
                        reducers[1].append((j, k))
                    else:
                        reducers[0].append((j, k))
                else:
                    if j >= 135:
                        booster[9].append((j,k))
                    elif j >= 120:
                        booster[8].append((j, k))
                    elif j >= 105:
                        booster[7].append((j, k))
                    elif j >= 90:
                        booster[6].append((j, k))
                    elif j >= 75:
                        booster[5].append((j, k))
                    elif j >= 60:
                        booster[4].append((j, k))
                    elif j >= 45:
                        booster[3].append((j, k))
                    elif j >= 30:
                        booster[2].append((j, k))
                    elif j >= 15:
                        booster[1].append((j, k))
                    else:
                        booster[0].append((j, k))
                sumVal += neuron_weights[j][k] * i[0][k]
            neurons_out.append(sign(sumVal))

        sum_nodes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range(150):
            if j >= 135:
                sum_nodes[9] += neurons_out[j]
            elif j >= 120:
                sum_nodes[8] += neurons_out[j]
            elif j >= 105:
                sum_nodes[7] += neurons_out[j]
            elif j >= 90:
                sum_nodes[6] += neurons_out[j]
            elif j >= 75:
                sum_nodes[5] += neurons_out[j]
            elif j >= 60:
                sum_nodes[4] += neurons_out[j]
            elif j >= 45:
                sum_nodes[3] += neurons_out[j]
            elif j >= 30:
                sum_nodes[2] += neurons_out[j]
            elif j >= 15:
                sum_nodes[1] += neurons_out[j]
            else:
                sum_nodes[0] += neurons_out[j]

        print(sum_nodes, argmax(sum_nodes), i[1])

        if argmax(sum_nodes) == i[1]:
            total += 1
            print("correct")
        else:
            print("wrong")
            total += 1
            wrongCount += 1
            for j in reducers[i[1]]:
                if probgen(2):
                    neuron_weights[j[0]][j[1]] *= -1
            for j in range(0, 10):
                if probgen(4) and probgen(4):
                    if j != i[1]:
                        if probgen(4):
                            for k in booster[j]:
                                if probgen(3) and sum_nodes[j] >= 0:
                                    neuron_weights[k[0]][k[1]] *= -1
    accuracy = (total - wrongCount) / total
    solution_acc.append(accuracy)
    solutions.append(neuron_weights)
    print(accuracy)

max_acc = 0
for i in solution_acc:
    if i > max_acc:
        max_acc = i

print(solutions[solution_acc.index(max_acc)])
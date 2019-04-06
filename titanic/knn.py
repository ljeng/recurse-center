import csv, numpy, statistics
def read_file(file): return [x for x in list(csv.reader(open(file + '.csv')))[1:]]
train, test = read_file('train'), read_file('test')
def get_title(name): return name[name.index(',') + 2: name.index('.') + 1]
def replace_all(array):
    for x in array:
        x[2] = get_title(x[2])
        x[4] = float(x[4]) if x[4] else None
        x[8] = float(x[8]) if x[8] else None
    return array
train2 = replace_all(train)
def knn(passenger, k):
    score_list = []
    for x in train2:
        score = 0
        for i in range(len(passenger)):
            if not x[4] or not x[8]: break
            if i == 4 and abs(float(passenger[4]) - x[4]) < statistics.stdev(numpy.transpose([y[4] for y in train2 if y[4]])): score += 1
            if i == 8 and abs(float(passenger[8]) - x[8]) < statistics.stdev(numpy.transpose([y[8] for y in train2 if y[8]])): score += 1
            elif passenger[i] == x[i]: score += 1
        score_list += [score]
    print(list(sorted(score_list)))
    arg_index = numpy.argsort(score_list)[-k:]
    output = []
    for i in arg_index: output += [train[i]]
    return output
 
for x in knn(['0', '3', 'Mr.', 'male', '32', '0', '0', '370376', '7.75', '', 'Q'], 10): print(x)

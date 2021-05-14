import inspect
import sys
import math,copy
"""
Raise a "not defined" exception as a reminder
"""

def _raise_not_defined():
    print("Method not implemented: %s" % inspect.stack()[1][3])
    sys.exit(1)


"""
Extract 'basic' features, i.e., whether a pixel is background or
forground (part of the digit)
"""

def flatten_list(temp_list):
    flat_list= []
    for row in temp_list:
        for elem in row:
            flat_list.append(elem)
    return flat_list

def extract_basic_features(digit_data, width, height):
    features = []
    # Your code starts here
    data = copy.deepcopy(digit_data)
    temp = list(map(lambda row: list(map(lambda val: False if val == 0 else True, row)), data))
    return flatten_list(temp)


"""
Extract advanced features that you will come up with
"""

def combine_features(features_set):
    total_count_of_each_feature = len(features_set)
    count_of_each_true = [0]*len(features_set[0])
    for features in features_set:
        for i in range(len(features)):
            if features[i] == True:
                count_of_each_true[i] += 1
    combined_features = []
    for i in range(len(features_set[0])):
        if count_of_each_true[i] > total_count_of_each_feature//2:
            combined_features.append(True)
        else:
            combined_features.append(False)
    return combined_features


def extract_advanced_features(digit_data, width, height):
    features = []
    # Your code starts here
    temp = list(map(lambda row: list(map(lambda val: 2 if val == 2 else True if val == 1 else False, row)),
                    copy.deepcopy(digit_data)))

    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp[i][j] == 2:
                temp[i][j] = True
                if i > 0:
                    temp[i - 1][j] = True
                    if j > 0:
                        temp[i - 1][j - 1] = True
                    if j + 1 < height:
                        temp[i - 1][j + 1] = True
                if i + 1 < width:
                    temp[i + 1][j] = True
                    if j + 1 < height:
                        temp[i + 1][j + 1] = True
                if j > 0:
                    temp[i][j - 1] = True
                    if i + 1 < width:
                        temp[i + 1][j - 1] = True
                if j + 1 < height:
                    temp[i][j + 1] = True

    feature_set1 = flatten_list(temp)


    temp2 = list(map(lambda row: list(map(lambda val: True if val > 0 else False, row)), copy.deepcopy(digit_data)))
    for i in range(len(temp2)):
        for j in range(len(temp2[i])):
            if temp2[i][j] == 0:
                a = b = c = d = True
                if i > 0 and temp2[i-1][j] == False:
                    a = False
                if i<len(temp2)-1 and temp2[i+1][j] == False:
                    b = False
                if j> 0 and temp2[i][j-1] == False:
                    c = False
                if j < len(temp2[i]) - 1 and temp2[i][j+1] == False:
                    d = False
                temp2[i][j] = a and b and c and d

    feature_set2 = flatten_list(temp2)


    temp3 = list(map(lambda row: list(map(lambda val: val, row)), copy.deepcopy(digit_data)))
    for i in range(len(temp3)):
        for j in range(len(temp3[i])):
            if j > 0 and temp3[i][j] < temp3[i][j-1] and temp3[i][j] < temp3[i][j+1] and temp3[i][j] == 0:
                temp3[i][j] = True
            else:
                temp3[i][j]= False
    feature_set3 = flatten_list(temp3)

    features = combine_features([feature_set1,feature_set2,feature_set3])

    return features

def extract_final_features(digit_data, width, height):
    basic_features = extract_basic_features(digit_data, width, height)

    # Your code starts here
    temp = list(map(lambda row: list(map(lambda val: 2 if val == 2 else True if val == 1 else False, row)),
                    copy.deepcopy(digit_data)))

    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp[i][j] == 2:
                temp[i][j] = True
                if i > 0:
                    temp[i - 1][j] = True
                    if j > 0:
                        temp[i - 1][j - 1] = True
                    if j + 1 < height:
                        temp[i - 1][j + 1] = True
                if i + 1 < width:
                    temp[i + 1][j] = True
                    if j + 1 < height:
                        temp[i + 1][j + 1] = True
                if j > 0:
                    temp[i][j - 1] = True
                    if i + 1 < width:
                        temp[i + 1][j - 1] = True
                if j + 1 < height:
                    temp[i][j + 1] = True

    feature_set1 = flatten_list(temp)


    temp2 = list(map(lambda row: list(map(lambda val: True if val > 0 else False, row)), copy.deepcopy(digit_data)))
    for i in range(len(temp2)):
        for j in range(len(temp2[i])):
            if temp2[i][j] == 0:
                a = b = c = d = True
                if i > 0 and temp2[i-1][j] == False:
                    a = False
                if i<len(temp2)-1 and temp2[i+1][j] == False:
                    b = False
                if j> 0 and temp2[i][j-1] == False:
                    c = False
                if j < len(temp2[i]) - 1 and temp2[i][j+1] == False:
                    d = False
                temp2[i][j] = a and b and c and d

    feature_set2 = flatten_list(temp2)


    temp3 = list(map(lambda row: list(map(lambda val: val, row)), copy.deepcopy(digit_data)))
    for i in range(len(temp3)):
        for j in range(len(temp3[i])):
            if j > 0 and temp3[i][j] < temp3[i][j-1] and temp3[i][j] < temp3[i][j+1] and temp3[i][j] == 0:
                temp3[i][j] = True
            else:
                temp3[i][j]= False
    feature_set3 = flatten_list(temp3)

    features = combine_features([feature_set1,feature_set2,feature_set3,basic_features])

    return features


"""
Compupte the parameters including the prior and and all the P(x_i|y). Note
that the features to be used must be computed using the passed in method
feature_extractor, which takes in a single digit data along with the width
and height of the image. For example, the method extract_basic_features
defined above is a function than be passed in as a feature_extractor
implementation.

The percentage parameter controls what percentage of the example data
should be used for training.
"""

prior={}
cond_prob_each_label = {}

def compute_statistics(data, label, width, height, feature_extractor, percentage=100.0):
    # Your code starts here
    total_samples = int(len(data)*(percentage/100))

    # count the labels
    dict_label_count = {}
    for i in range(total_samples):
        if dict_label_count.get(label[i]) == None:
            dict_label_count[label[i]] = 1
        else:
            dict_label_count[label[i]]+=1

    # calculate prior probabilites
    global prior
    for key in dict_label_count:
        if prior.get(key) == None:
            prior[key] = (dict_label_count[key]/total_samples)
    # print(dict_label_count)
    # print(prior)

    # calculate conditional probabilities
    dict_label_features={}
    for i in range(total_samples):
        if dict_label_features.get(label[i]) == None:
            dict_label_features[label[i]] = [feature_extractor(data[i], width, height)]
        else:
            features_for_label = dict_label_features.get(label[i])
            features_for_label.append(feature_extractor(data[i], width, height))
            dict_label_features[label[i]] = features_for_label

    global cond_prob_each_label
    for key in dict_label_features.keys():
        features_for_label = dict_label_features.get(key)
        count_of_feature_i_j = [0]*(width*height)

        # 3-D list
        count_of_all_features = len(features_for_label)
        for features_set in features_for_label:
            for i in range(len(features_set)):
                if features_set[i] == False:
                    count_of_feature_i_j[i] += 1

        est_cond_prob = []
        k = 0.03
        for i in range(width*height):
            est_cond_prob.append((count_of_feature_i_j[i] + k) / (count_of_all_features + k*2))
        cond_prob_each_label[key] = est_cond_prob
    return 0

"""
For the given features for a single digit image, compute the class
"""


def compute_class(features):
    predicted = -1

    # Your code starts here
    global prior,cond_prob_each_label
    labels = prior.keys()
    prob_label = {}
    for label in labels:
        sum = math.log(prior[label])
        temp = 0
        for i in range(len(features)):
                feature = features[i]
                if feature == False:
                    temp += math.log(cond_prob_each_label[label][i])
                else:
                    temp += math.log((1 - cond_prob_each_label[label][i]))
        prob_label[label] = sum + temp
    # print(prob_label)

    # finding max prob label
    max_val = -math.inf
    for key in prob_label.keys():
        if max_val < prob_label[key]:
            max_val = prob_label[key]
            predicted = key

    # Your code ends here
    return predicted,max_val


"""
Compute joint probaility for all the classes and make predictions for a list
of data
"""


def classify(data, width, height, feature_extractor):
    predicted = []
    # Your code starts here
    for i in range(len(data)):
        label,val = compute_class(feature_extractor(data[i], width, height))
        predicted.append(label)
    # Your code ends here
    return predicted

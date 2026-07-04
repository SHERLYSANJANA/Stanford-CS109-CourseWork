'''
Additional classifier questions
'''
import math
import numpy as np

"""
Starter Code for CS 109 Problem Set 6
Written by Tim Gianitsos
Spec by Lisa Yan

*************************IMPORTANT*************************
Do NOT modify the name of any functions. Do not add or remove
parameters to them either. Moreover, make sure your return
value is exactly as described in the PDF handout and in the
provided function comments. Remember that your code is being
autograded. You are free to write helper functions if you so
desire but they are not necessary. Do NOT rename this file.
Do NOT modify any code outside the begin and end code markers.
*************************IMPORTANT*************************
"""

#############################################
########### Naive Bayes Questions ###########
#############################################

def question_nb_a(clf, train_features, train_labels):
    # This fits the model to the training data. Ensure your implementation for 
    # `NaiveBayes.fit()` is correct!
    clf.fit(train_features, train_labels)

    epsilon = 1e-8 # prevents division by zero in case fit() is not implemented
    res = clf.label_counts[1] / ((clf.label_counts[0] + clf.label_counts[1]) or epsilon)
    return res

def question_nb_b(clf, train_features, train_labels):
    clf.fit(train_features, train_labels)
    res = np.zeros(train_features.shape[1])
    

    for j in range(train_features.shape[1]):
        count0=np.sum(train_labels==0)
        if clf.use_mle:
            res[j]=clf.feature_counts.get((0,j,1),0)/count0
        else:
            res[j]=(clf.feature_counts.get((0,j,1),0)+1)/(count0+2)
    
    ### END YOUR CODE

    return res

def question_nb_c(clf, train_features, train_labels):
    clf.fit(train_features, train_labels)
    res = np.zeros(train_features.shape[1])

    ### YOUR CODE HERE
    for j in range(train_features.shape[1]):
        count1=np.sum(train_labels==1)
        if clf.use_mle:
            res[j]=clf.feature_counts.get((1,j,1),0)/count1
        else:
            res[j]=(clf.feature_counts.get((1,j,1),0)+1)/(count1+2)
    ### END YOUR CODE

    return res

def question_nb_d(clf, train_features, train_labels):
    clf.fit(train_features, train_labels)
    res = np.zeros(train_features.shape[1])

    ### YOUR CODE HERE
    res_x_11=question_nb_c(clf, train_features, train_labels) #x=1y=1
    res_x_10=question_nb_b(clf, train_features, train_labels) #x=1,y=0
    res_x_01=np.subtract([1]*len(res_x_11),res_x_11) #x=0,y=1
    res_x_00=np.subtract([1]*len(res_x_10),res_x_10)
    count1=np.sum(train_labels==1)
    count0=np.sum(train_labels==0)

    prob0=count0/(count0+count1)
    prob1=count1/(count0+count1)
                   
    for i in range(len(res_x_11)):
        numerator=res_x_11[i]*prob1/(res_x_11[i]*prob1+res_x_10[i]*prob0)
        denominator= res_x_01[i]*prob1/(res_x_01[i]*prob1+res_x_00[i]*prob0)
        res[i]=numerator/denominator
    ### END YOUR CODE
    res=np.argsort(res)[-1:-6:-1]
    return np.sort(res)
#############################################
####### Logistic Regression Questions #######
#############################################

def question_lr_a(clf, train_features, train_labels):
    clf.fit(train_features, train_labels)
    res = np.zeros(5)
    theta=clf.weights
    ### YOUR CODE HERE
    res=np.argsort(theta)[-1:-6:-1]
    ### END YOUR CODE

    return np.sort(res)

def question_lr_b(clf, train_features, train_labels, test_features, test_labels):
    clf.fit(train_features, train_labels)
    res = 0.0

    ### YOUR CODE HERE
    preds_test=clf.predict(test_features)

    true_positive=0
    false_positive=0
    for i in range(len(preds_test)):
        if(test_labels[i]==1 and preds_test[i]==1):
            true_positive+=1
        elif(test_labels[i]==0 and preds_test[i]==1):
            false_positive+=1
            
    res=true_positive/(true_positive+false_positive)
    ### END YOUR CODE

    return res

def question_lr_c(clf, train_features, train_labels, test_features, test_labels):
    clf.fit(train_features, train_labels)
    res = 0.0

    ### YOUR CODE HERE
    preds_test=clf.predict(test_features)

    true_positive=0
    false_negative=0
    for i in range(len(preds_test)):
        if(test_labels[i]==1 and preds_test[i]==1):
            true_positive+=1
        elif(test_labels[i]==1 and preds_test[i]==0):
            false_negative+=1
            
    res=true_positive/(true_positive+false_negative)
    ### END YOUR CODE

    return res

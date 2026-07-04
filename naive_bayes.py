'''
Naive Bayes Classifier
'''
import math
import numpy as np

"""
Starter Code for CS 109 Problem Set 6
Written by Tim Gianitsos

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

class NaiveBayes:
    '''
    Naive Bayes Classifier

    For a datapoint, the Naive Bayes classifier computes the probability of each label,
    and then it predicts the label with the highest probability. During training,
    it learns probabilities by counting the occurences of feature/label combinations
    that it finds in the training data. During prediction, it uses these counts to
    compute probabilities.
    '''

    def __init__(self, use_mle):
        '''DO NOT RENAME INSTANCE VARIABLES'''
        self.label_counts = {}
        self.feature_counts = {}
        self.use_mle = use_mle # True for MLE, False for MAP with Laplace add-one smoothing

    def fit(self, train_features, train_labels):
        self.label_counts[0] = 0
        self.label_counts[1] = 0

        self.label_counts[0]=np.sum(train_labels == 0)
        self.label_counts[1]=np.sum(train_labels == 1)

        for i in range(len(train_features)):
           sample=train_features[i]
           label=train_labels[i]
           for j in range(len(sample)):
               value=sample[j]
               if((label,j,value) in self.feature_counts.keys()) :
                   self.feature_counts[(label,j,value)]+=1
               else :
                    self.feature_counts[(label,j,value)]=0
                    self.feature_counts[(label,j,value)]+=1
        ### END YOUR CODE

    def predict(self, test_features):
        preds = np.zeros(test_features.shape[0], dtype=np.uint8)
        
        ##number of labels with 0 and 1
        label_count_0=self.label_counts[0]
        label_count_1=self.label_counts[1]

        for i in range(len(test_features)) :
            sample=test_features[i]
            
            p_label_0=math.log(label_count_0/(label_count_0+label_count_1))
            p_label_1=math.log(label_count_1/(label_count_0+label_count_1))
                
            for j in range(len(sample)):
                feature=sample[j]
                
                score1 = self.feature_counts.get((0, j, feature), 0)
                score2 = self.feature_counts.get((1, j, feature), 0)
                
                if self.use_mle :
                    if(score1>0):
                        p_label_0+=math.log(score1/label_count_0)
                    else :
                        p_label_0+=math.log((score1+1)/(label_count_0+2))
                        
                    if(score2>0):
                        p_label_1+=math.log(score2/label_count_1)
                    else:
                        p_label_1+=math.log((score2+1)/(label_count_1+2))
                else :
                    p_label_0+=math.log((score1+1)/(label_count_0+2))
                    p_label_1+=math.log((score2+1)/(label_count_1+2))

            if(p_label_0>p_label_1) :
                preds[i]=0
            else :
                preds[i]=1
        ### END YOUR CODE

        return preds 

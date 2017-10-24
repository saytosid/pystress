
import random
import os
import thread

class Stresser(object):
    """
    docstring for Stresser
    Interface for all Stresses.
    """

    def __init__(self):
        print("Stresser Initialised")

    def doStress(self, intensity=1):
        # @param intensity - Intensity of stress on a scale of 1-5
        print("I am stressing with intensity {}; kiddin! I dont do anything apart from being a loud mouth !".format(intensity))


class CreateFile(Stresser):
    """Creates big file"""

    def __init__(self):
        super(CreateFile, self).__init__()

    def doStress(self, intensity=1):
        filename = str(random.randint(0, 1024))
        with open(filename, 'wb') as f:
            for i in xrange(intensity * 20000):
                if random.random() < 0.4:
                    f.write(' ')  # Sometimes add a space
                if random.random() < 0.2:
                    f.write('\n')  # Sometimes newline
                f.write(str(i))
        return filename

# Large files for multiple tasks
files = []
for intensity in xrange(5):
    files.append(CreateFile().doStress(intensity+1))

################# MICRO LOADS ##################################
class WordCount(Stresser):
    """Creates big file and does wc on it"""

    def __init__(self):
        super(WordCount, self).__init__()
        

    def doStress(self, intensity=1):
        '''Stresses the machine'''
        print os.system('wc {}'.format(files[intensity-1]))

class Sort(Stresser):
    def __init__(self):
        super(Sort, self).__init__()
        
    def doStress(self, intensity=1):
        '''Stresses the machine'''
        print os.system('sort {}'.format(files[intensity-1]))

class Grep(Stresser):
    def __init__(self):
        super(Grep, self).__init__()
        
    def doStress(self, intensity=1):
        '''Stresses the machine'''
        print os.system('cat {} | grep 1'.format(files[intensity-1]))

class Concat(Stresser):
    def __init__(self):
        super(Sort, self).__init__()
        
    def doStress(self, intensity=1):
        '''Stresses the machine'''
        print os.system('cat {}'.format(files[0:intensity]))
#################################################################

############## ML Loads #########################################
from sklearn.datasets import make_classification, make_regression
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.cluster import KMeans

import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

n_samples = 100
regress_datasets = [make_regression(n_samples=n_samples, n_features=100*(intensity+1), n_informative=70*(intensity+1),
    n_targets=1, bias=0.0, effective_rank=None, tail_strength=0.5, noise=0.01, shuffle=True, coef=False,
    random_state=None) for intensity in xrange(5)]

classification_datasets = [make_classification(n_samples=n_samples, 
            n_features=100*(intensity+1), n_informative=50*(intensity+1), 
            n_redundant=30, n_repeated=0, n_classes=5, n_clusters_per_class=4,
            weights=None, flip_y=0.01, class_sep=1.0, hypercube=True, 
            shift=0.0, scale=1.0, shuffle=True, random_state=None) for intensity in xrange(5)]

class NaiveBayesClassifier(Stresser):
    def __init__(self):
        super(NaiveBayesClassifier, self).__init__()
        
    def doStress(self, intensity=1):
        '''Stresses the machine'''
        X,Y,= classification_datasets[intensity-1]
        gnb = GaussianNB()
        print gnb.fit(X, Y)

class NNClassifier(Stresser):
    def __init__(self):
        super(NNClassifier, self).__init__()

    def doStress(self, intensity=1):
        '''Stresses the machine'''
        X,Y,= classification_datasets[intensity-1]
        hidden_layer_sizes = tuple([100 for i in xrange(intensity)] )
        clf = MLPClassifier(hidden_layer_sizes = hidden_layer_sizes,verbose=True,max_iter=100,early_stopping=True,
            tol=0.000001)
        clf.fit(X,Y)

class NNRegressor(Stresser):
    def __init__(self):
        super(NNRegressor, self).__init__()

    def doStress(self, intensity=1):
        '''Stresses the machine'''
        X,Y,= regress_datasets[intensity-1]
        print X.shape
        print Y.shape
        hidden_layer_sizes = tuple([100 for i in xrange(intensity)] )
        reg = MLPRegressor(hidden_layer_sizes = hidden_layer_sizes,verbose=True,max_iter=100,early_stopping=True,
            tol=0.000001)
        reg.fit(X,Y)

class KMeansCluster(Stresser):
    def __init__(self):
        super(KMeansCluster, self).__init__()
        
    def doStress(self, intensity=1):
        '''Stresses the machine'''
        X,Y,= regress_datasets[intensity-1]
        kmeans = KMeans(n_clusters=8*intensity, init='k-means++', n_init=10,
                 max_iter=300, tol=1e-4, precompute_distances='auto',
                 verbose=1, random_state=None, copy_x=True,
                 n_jobs=intensity, algorithm='auto')
        kmeans.fit(X)


if __name__ == '__main__':
    # b = Grep()
    # b.doStress()
    b = KMeansCluster()
    b.doStress(intensity=2)    


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

############## ML Loads #########################################



if __name__ == '__main__':
    b = Grep()
    b.doStress()
    print files
    

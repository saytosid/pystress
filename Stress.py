
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


class CPUComputeLoad(Stresser):
    """docstring for CPUComputeLoad"""

    def __init__(self):
        super(CPUComputeLoad, self).__init__()
        print("CPUComputeLoad Initilised")

    def doStress(self, intensity=1):
        '''Stresses the machine'''
        # Some CPU heavy task
        print("I am stressing CPU with intensity {}".format(intensity))


if __name__ == '__main__':
    b = CPUComputeLoad()
    b.doStress()

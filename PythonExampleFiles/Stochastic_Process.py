import math
import numpy as np
import random
import stochpy
import matplotlib.pyplot as plt

def StochProcess1():
    # This one considers the basic representation through the inverse function of the exponential distribution
    def nextTime(rateParameter):
        return -math.log(1-random.random())/rateParameter
    
    print(nextTime(1/40.0))
    print(sum([nextTime(1/40.0) for i in xrange(1000000)])/1000000)

def StochProcess2():
# this instance is using the Poisson process function included in Python
    t=0
    N=1
    for i in range(1,10):
        t+=random.expovariate(1/40.0)
        print(N,t)

def StochProcess3():
    #This uses the stochpy module
    smod = stochpy.SSA() #Instance of a Stochastic Simulation Algorithm
    smod.DoStochSim(IsTrackPropensities=True)
    smod.PlotSpeciesTimeSeries()
    smod.PlotPropensitiesTimeSeries()
    #Somemore functions
    smod.DoStochSim(end=10**5)
    smod.GetSpeciesAutocorrelations()
    smod.PlotSpeciesAutocorrelations(nlags=25)
    smod.GetWaitingtimes()
    smod.PlotWaitingtimesDistributions()
    stochpy.plt.xlim([10**-4,10**0])

def StochProcess4():
    #this example needs to import numpy and matplotlib
    #generating the fake data
    locations = np.arange(0,50,1)
    medians = locations/(1.0+(locations/5.0)**2)
    disps = 0.1+0.5*locations/(1.0+(locations/5.0)**2.)
    points = np.empty([50,100])
    for i in xrange(50):
        points[i,:] = np.random.normal(loc=medians[i], scale=disps[i], size=100)
    
    #finding percentiles
    pcts = np.array([20,35,45,55,65,80])
    layers = np.empty([50,6])
    for i in xrange(50):
        _sorted = np.sort(points[i,:])
        layers[i,:] = _sorted[pcts]
    
    # plot the layers
    colors = ["blue","green","red","green","blue"]
    for i in xrange(5):
        plt.fill_between(locations, layers[:,i], layers[:,i+1],color=colors[i])
    plt.show()
    
            

if __name__=="__main__":
    #StochProcess1()
    #StochProcess2()
    #StochProcess3()
    StochProcess4()
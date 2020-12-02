from thinkbayes import Pmf

def Distributions():
    pmf = Pmf()    #Probability Mass Function class instance
    for x in [1,2,3,4,5,6]:
        pmf.Set(x,1/6.0)

    for x in [1,2,3,4,5,6]:
        print("Number: ", x, " Probability: ", pmf.Prob(x))

        pmf = Pmf()

        word_list = ["the","the","one","two","country"]
        for word in word_list:
            pmf.Incr(word,1)
        pmf.Normalize()

    for word in word_list:
        print("Word: ", word, " Probability: " , pmf.Prob(word))

def CookieProblem():
    pmf = Pmf()
    pmf.Set("Bowl1", 0.5)
    pmf.Set("Bowl2", 0.5)
    
    pmf.Mult("Bowl1", 0.75)
    pmf.Mult("Bowl2", 0.5)
    
    pmf.Normalize()
    
    print(pmf.Prob("Bowl1"))

def BayesianFramework():
    class Cookie(Pmf):
        def __init__(self,hypos):
            Pmf.__init__(self)
            for hypo in hypos:
                self.Set(hypo, 1)
            self.Normalize()
        
        def Update(self,data):
            for hypo in self.Values():
                like = self.Likelihood(data, hypo)
                self.Mult(hypo, like)
            self.Normalize()
        
        mixes = {"Bowl1": dict(vanilla = 0.75, chocolate = 0.25),
                 "Bowl2": dict(vanilla = 0.5, chocolate = 0.5),
                 }
        
        def Likelihood(self,data,hypo):
            mix = self.mixes[hypo]
            like = mix[data]
            return like
    
    hypos = ["Bowl1","Bowl2"]
    pmf = Cookie(hypos)
    
    dataset = ["vanilla","chocolate","vanilla"]
    for data in dataset:
        pmf.Update(data)
        for hypo, prob in pmf.Items():
            print(hypo, prob)
    
def MontyHall():
    class Monty(Pmf):   
        def __init__(self,hypos):
            Pmf.__init__(self)
            for hypo in hypos:
                self.Set(hypo, 1)
            self.Normalize()
            
        def Update(self,data):
            for hypo in self.Values():
                like = self.Likelihood(data, hypo)
                self.Mult(hypo, like)
            self.Normalize()
            
        def Likelihood(self,data,hypo):
            if hypo == data:
                return 0
            elif hypo == "A":
                return 0.5
            else:
                return 1
    
    hypos = "ABC"        
    pmf = Monty(hypos)
    data = "B"
    pmf.Update(data)
    for hypo, prob in pmf.Items():
        print(hypo, prob)

from thinkbayes import Suite

def SuiteUse():
    #This optiuon uses the suite built-in functions and definitions
    #already contained in thinkbayes.py
    class Monty(Suite):
        
        def Likelihood(self,data,hypo):
            if hypo == data:
                return 0
            elif hypo == "A":
                return 0.5
            else:
                return 1
    
    suite = Monty("ABC")
    suite.Update("B")
    suite.Print()

def MandMProblem():
    class M_and_M(Suite):
        mix94 = dict(brown=30,
            yellow=20,
            red=20,
            green=10,
            orange=10,
            tan=10)
    
        mix96 = dict(blue=24,
            green=20,
            orange=16,
            yellow=14,
            red=13,
            brown=13)        
    
        hypoA = dict(bag1=mix94, bag2=mix96)
        hypoB = dict(bag1=mix96, bag2=mix94)
    
        hypotheses = dict(A=hypoA, B=hypoB)
        
        def Likelihood(self,data,hypo):
            bag,color = data
            mix = self.hypotheses[hypo][bag]
            like = mix[color]
            return like
    
    suite = M_and_M("AB")
    suite.Update(("bag1","yellow"))
    suite.Update(("bag2", "green"))
    
    suite.Print()
if __name__ == "__main__":
    #Distributions()
    #CookieProblem()
    BayesianFramework()
    #MontyHall()
    #SuiteUse()
    #MandMProblem()



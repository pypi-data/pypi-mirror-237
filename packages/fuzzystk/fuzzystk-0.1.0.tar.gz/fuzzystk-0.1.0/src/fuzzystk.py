import numpy as np
import matplotlib.pyplot as plt

class ling_term:
    def __init__(self, n: str, t: str, r: list):
        self.__name = n
        self.__type = t
        self.__range = r

    def getName(self): return self.__name  
    def getType(self): return self.__type
    def getInter(self): return self.__range

    def relevance(self, x: float):
        if self.__type == 'triangular':
            if x > self.__range[0] and x <= self.__range[1]: return (x-self.__range[0])/(self.__range[1]-self.__range[0])
            elif x >= self.__range[1] and x <= self.__range[2]: return (self.__range[2]-x)/(self.__range[2]-self.__range[1])
            else: return 0
        
        elif self.__type == 'trapezoidal':
            if x > self.__range[0] and x <= self.__range[1]: return (x-self.__range[0])/(self.__range[1]-self.__range[0])
            if x >= self.__range[1] and x <= self.__range[2]: return 1
            elif x >= self.__range[2] and x <= self.__range[3]: return (self.__range[3]-x)/(self.__range[3]-self.__range[2])
            else: return 0

        elif self.__type == "gaussian":
            if x >= (self.__range[0]-self.__range[1]) and x <= (self.__range[0]+self.__range[1]): return np.exp( -( (x-self.__range[0])**2 )/(self.__range[2]**2) )
            else : return 0

class ling_var:

    def __init__(self, n: str, r: list):
        self.__name = n
        self.__range = r 
        self.__terms = []

    def getName(self): return self.__name
    def getRange(self): return self.__range
    def getTerms(self): return self.__terms

    def add(self, n, t, r):
        lt = ling_term(n, t, r)
        self.__terms.append(lt)

    def showTerms(self):
        names = [ i.getName() for i in self.__terms]
        return names
    
    def plot(self):
        for i in self.__terms:
            aux = [ i.relevance(j) for j in self.__range ]
            plt.plot(self.__range, aux, label = i.getName() )
        plt.title( self.__name )
        plt.legend() 
        plt.show() 

class controller:

    def __init__(self, r: list, i: list, o: list):
        self.__rules = r
        self.__input = i 
        self.__output = o
        #self.__activate(self, v: list)

    def map(self, values: list):
        rel = []
        for i in range(len(self.__rules)):
            aux = []
            for j in range(len(values)):
                index = self.__input[j].showTerms().index(self.__rules[i][j])
                term = self.__input[j].getTerms()[index]
                aux.append(term.relevance(values[j]))
            rel.append(aux)

        return rel

    def activate(self, values: list):
        m = self.map(values)
        act = []
        for i in range(len(m)): 
            if min(m[i]) != 0: act.append(i)
        return act

    def mandani(self, values: list, defuzzy = 'centroid'):
        act_index = self.activate(values)
        rel = [i for i in self.map(values) if min(i) != 0]
        #print(f'rel: {rel}')
        #print(f'act_index: {act_index}')
      
        names = []
        indexs = []
        for i in act_index:
            for j in range( len( self.__output) ):
                names.append(self.__rules[i][len(self.__input) + j])  
                indexs.append(self.__output[j].showTerms().index(names[j-1])) 
 
        all_act = []
        dom = []
        for i in self.__output:
            p = 0
            for k in indexs:
                aux = []
                for j in i.getRange():
                    result = i.getTerms()[k].relevance(j)
                    if result <= min( rel[p]): aux.append( result )
                    else: aux.append( min(rel[p]) )
                dom.append(aux)
                p += 1
            all_act.append(dom)

        #print('all_act')
        #rint(all_act)

        max_all = []
        #print(f'len(all_act[k][:][1]): {len(all_act[0][:][0])}')
        for k in range( len(self.__output)):
            img = []
            for i in range( len(all_act[k][:][0])):
                m = 0
                for j in range( len(all_act[k])): m = max( all_act[k][j][i], m)
                img.append(m)
            max_all.append(img)

        #print(f'max_all: {max_all}')

        if defuzzy == 'centroid':
            defuzz = []
            for i in range(len(self.__output)):
                d = 0    
                for j in range(len(self.__output[i].getRange())): d += self.__output[i].getRange()[j]*max_all[i][j]   
                d *= 1.0/sum(max_all[i])
                defuzz.append(d)

            return defuzz

        elif defuzzy == 'max center':
            defuzz = []
            for i in range(len(self.__output)):
                mcenter = [j for j in range( len( max_all[i])) if max_all[i][j] == max(max_all[i])] 
                d = (min(mcenter) + max(mcenter))/2.0
                defuzz.append(d)
            
            return defuzz
                
        elif defuzzy == 'max average':
            defuzz = []
            for i in range( len(self.__output)):
                maverage = [j for j in range( len( max_all[i])) if max_all[i][j] == max(max_all[i])] 
                d = sum(maverage)/len(maverage)
                defuzz.append(d)
            
            return defuzz 
        

import random as rng
import math
import sys

try:
    def bernoulli():
        n = sys.argv[1]
        range1 = range(int(n))
        y = [rng.random() for i in range1]
        p = float(sys.argv[3])
        x = None # bernoulli RV
        #print type(x)
        for u in y:
            if u < p:
                x = 1
                print x
            elif u >= p:
                x = 0
                print x
    #bernoulli()
    #binomial distribution
    def binomial():
        p = float(sys.argv[4])
        x = int() #binomial RV
        n = sys.argv[3]
        m = sys.argv[1]
        range1 = range(int(n))
        range2 = range(int(m))
        for e in range2:
            z = [rng.random() for i in range1]
            l = []
            x = 0
            for u in z:
                if u < p:
                    x = x + 1
            print 'X_'+ str(e) +':', x
            result = float(float(x)/float(n))
            print 'probability is:', result

    #binomial()

    #geometric
    def geometric():
        p = float(sys.argv[3])
        n = int(sys.argv[1])
        m = 10000
        range3 = range(n)
        range2 = range(m)
        for k in range3:
            y = [rng.random() for i in range2]
            x = 1
            for u in y:
                if u > p:
                    x = x + 1
                else:
                    break
            print 'X_' + str(k) + ':', x
    #geometric()

    #neg binomial
    def neg_binomial():
        p = float(sys.argv[4])
        n = int(sys.argv[1])
        k = int(sys.argv[3])
        m = k * 1000
        range2 = range(m)
        range1 = range(n)
        for q in range1: # for n neg_binomial RV sample
            y = [rng.random() for i in range2] # generate 1000 random numbers
            x = 1  #atleast one trial
            list = [] # list to store all the measure of trials required through k successes
            for u in y: # iterate through every random number
                if len(list) == k: # when the kth success is achieved
                    break # done for the particular RV
                if u > p: # failure
                    x = x + 1 # increment no of trials
                else: # success occurs
                    list.append(x) # append no of trials required through kth success
                    x = x + 1 # include the success trial in the measure of trials
                    continue
            #print list
            z = list[k-1] # neg_binomial RV
            print 'X_' + str(q) + ':', z

    #neg_binomial()

    #arbitrary discrete distribution
    def arbitrary_discrete():
        n = int(sys.argv[1])
        l = [] # list to hold all the probabilities of the sub intervals
        for e in sys.argv[3:]: # iterate through the probabilities
            l.append(float(e)) # add them to the list
        #print l
        # check if the probabilities add upto 1
        if sum(l) == 1:
            print 'your probabilities for the sub intervals are good'
        else:
            print 'include probabilities which add upto 1.\nfor eg: 0.25, 0.20, 0.55'
            sys.exit()

        range1 = range(n)
        for q in range1:
            x = {} # dictionary to hold up the Discrete RV and it's corresponding probability
            a = 0 # used to maintain lower bound of the sub interval
            b = 0 # used to maintain upper bound of the sub interval
            for i in l: # iterate through the list containing probabilities
                b = b + i # update upper bound
                x[rng.uniform(a,b)] = i  # generate a standard uniform random number for a probability associated with the sub interval
                a = a + i # update the lower bound
            print 'X_' + str(q) + ':', x
        #print x


    #arbitrary_discrete()

    #poisson
    def poisson():
        lbda = int(sys.argv[3])
        n = int(sys.argv[1])
        p_0 = 0.25
        p_1 = 0.20
        p_2 = 0.55
        list = [p_0, p_1, p_2] # list holding the probabilities of the sub intervals
        #print list
        range1 = range(n)
        for e in range1:
            x = [] # list holding the standard uniform random numbers
            a = 0 # used to maintain the lower bound of the interval
            b = 0 # used to maintain the upper bound of the interval
            for i in list: # iterate through the probabilities of the sub intervals
                b = b + i # update the upper bound
                x.append(rng.uniform(a,b)) # generating and appending standard uniform random numbers belonging to the sub intervals to the list
                a = a + i # update the lower bound
                #index = index + 1
            index = 0
            l = [] # list holding the poisson RV
            for j in x: # iterate through the uniform random numbers
                i = 0  # initialze poisson RV
                f = math.exp(-lbda) # initialze f value
                while (x[index] >= f): # increment the Poisson RV value untill condition holds true or else break out
                    f = f + math.exp(-lbda) * math.pow(lbda,i) / math.gamma(i+1) # update f value
                    i = i + 1 # update RV value
                index = index + 1
                l.append(i) # append the RV value; for every artibrary discrete uniform random number there is a poissson RV
        #print l
            #for k in l:
            print "X_" + str(e) + ":", l

    #poisson()

    #exponential
    def exponential():
        lbda = float(sys.argv[3])
        n = int(sys.argv[1])
        range1 = range(n)
        for e in range1: # generate n samples of expo RV
            u = rng.random() # generate standard uniform random number
            #print u
            x = -1 / lbda * math.log(1-u) # compute expo RV
            #y = -1 / lbda
            #print y
            #z = math.log(1-u)
            #print z
            print 'X_' + str(e) + ':', x

    #exponential()

    #gamma
    def gamma():
        alpha = int(sys.argv[3])
        lbda = float(sys.argv[4])
        n = int(sys.argv[1])
        range1 = range(n)
        range3 = range(alpha)
        for e in range1: # generate n gamma RV samples
            U = [rng.random() for i in range3] # generate standard uniform alpha no of random numbers
            #print U
            l = [] # list to hold expo RV
            for u in U: # iterate through all the uniform random numbers
                x = -1 / lbda * math.log(1-u) # compute the equivalent expo RV from a random number
                l.append(x)
            #y = -1 / lb
            #print y
            #z = math.log(1-u)
            #print z
            X = sum(l) # sum all the computed expo RV to get a gamma RV
            print 'X_' + str(e) + ':', X
    #gamma()


    #normal
    def normal():
        mean = float(sys.argv[3])
        s_d = float(sys.argv[4])
        n = int(sys.argv[1])
        range1 = range(n)
        for e in range1: # generate n standard normal RV
            u1 = rng.random() # generate first standard uniform random number
            u2 = rng.random() # generate second standard uniform random number
            #print u1,u2
            # box mueller transformation
            z1 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2) # compute first normal RV
            z2 = math.sqrt(-2 * math.log(u1)) * math.sin(2 * math.pi * u2) # compute second normal RV
            n1 = z1 * s_d + mean # compute first standard normal RV
            n2 = z2 * s_d + mean # compute second standard normal RV
            print 'n1_' + str(e) + ':', n1
            print 'n2_' + str(e) + ':', n2
    #normal()

    #uniform
    def uniform():
        a = int(sys.argv[3])
        b = int(sys.argv[4])
        n = int(sys.argv[1])
        range4 = range(n)
        U = [rng.random() for i in range4] # generate n random number
        #print U
        l = [] # list to hold all the unifrom RV
        for e in range4: # generate n uniform RV
            for u in U: # iterate through n random numbers
                x = u * (b-a) + a # compute the equivalent uniform RV
                l.append(x)
            print 'X_' + str(e) + ':', l[e]
    #uniform()

    if str(sys.argv[2]) == 'bernoulli':
        bernoulli()
    elif str(sys.argv[2]) == 'binomial':
        binomial()
    elif str(sys.argv[2]) == 'geometric':
        geometric()
    elif str(sys.argv[2]) == 'neg_binomial':
        neg_binomial()
    elif str(sys.argv[2]) == 'arbitrary_discrete':
        arbitrary_discrete()
    elif str(sys.argv[2]) == 'poisson':
        poisson()
    elif str(sys.argv[2]) == 'exponential':
        exponential()
    elif str(sys.argv[2]) == 'gamma':
        gamma()
    elif str(sys.argv[2]) == 'normal':
        normal()
    elif str(sys.argv[2]) == 'uniform':
        uniform()
    else:
        print """Error Occured.\nUse the following format only for the differnet probability distributions\n"""
        print """            python simulateDist.py <no. of samples> bernouilli <p>\n
                e.g. : python simulateDist.py 10 bernouilli 0.4\n\n
                python simulateDist.py <no. of samples> binomial  <n> <p>\n
                e.g. : python simulateDist.py 20 binomial 30 0.23\n\n
                python simulateDist.py <no. of samples> geometric <p>\n
                e.g. : python simulateDist.py 5 geometric 0.43\n\n
                python simulateDist.py <no. of samples> neg_binomial <k> <p>\n
                e.g. : python simulateDist.py 12 neg_binomial 20 0.58\n\n
                python simulateDist.py <no. of samples> arbitrary_discrete <p0> <p1> <p2> ...... <pn>\n
                e.g. : python simulateDist.py 15 arbitrary_discrete 0.2 0.1 0.3......0.1\n\n
                python simulateDist.py <no. of samples> poisson <lambda>\n
                e.g. : python simulateDist.py 8 poisson 3\n\n
                python simulateDist.py <no. of samples> exponential <lambda>\n
                e.g. : python simulateDist.py 9 exponential 7\n\n
                python simulateDist.py <no. of samples> gamma <alpha> <lambda>\n
                e.g. :python simulateDist.py 13 gamma 5 10\n\n
                python simulateDist.py <no. of samples> normal <mean> <s.d.>\n
                e.g. :python simulateDist.py 15 normal 5 1\n\n
                python simulateDist.py <no. of samples> uniform <a> <b>\n
                e.g. :python simulateDist.py 6 uniform 2 4"""

except:
    print """Error Occured.\nUse the following format only for the differnet probability distributions\n"""
    print """            python simulateDist.py <no. of samples> bernouilli <p>\n
            e.g. : python simulateDist.py 10 bernouilli 0.4\n\n
            python simulateDist.py <no. of samples> binomial  <n> <p>\n
            e.g. : python simulateDist.py 20 binomial 30 0.23\n\n
            python simulateDist.py <no. of samples> geometric <p>\n
            e.g. : python simulateDist.py 5 geometric 0.43\n\n
            python simulateDist.py <no. of samples> neg_binomial <k> <p>\n
            e.g. : python simulateDist.py 12 neg_binomial 20 0.58\n\n
            python simulateDist.py <no. of samples> arbitrary_discrete <p0> <p1> <p2> ...... <pn>\n
            e.g. : python simulateDist.py 15 arbitrary_discrete 0.2 0.1 0.3......0.1\n\n
            python simulateDist.py <no. of samples> poisson <lambda>\n
            e.g. : python simulateDist.py 8 poisson 3\n\n
            python simulateDist.py <no. of samples> exponential <lambda>\n
            e.g. : python simulateDist.py 9 exponential 7\n\n
            python simulateDist.py <no. of samples> gamma <alpha> <lambda>\n
            e.g. :python simulateDist.py 13 gamma 5 10\n\n
            python simulateDist.py <no. of samples> normal <mean> <s.d.>\n
            e.g. :python simulateDist.py 15 normal 5 1\n\n
            python simulateDist.py <no. of samples> uniform <a> <b>\n
            e.g. :python simulateDist.py 6 uniform 2 4"""

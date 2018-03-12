import numpy as np

import theano
import theano.tensor as T


class PRank:
    def __init__(self, n_classes, n_features):
        #aprendizado por linha (n_samples, n_features)
        X = T.dvector('x')
        #classe de saída é um inteiro
        Y = T.iscalar('y')

        W = theano.shared(np.zeros(n_features))
        
        init_bias = np.zeros(n_classes)

        b = theano.shared(init_bias)
        
        self.params = [W,b]

        z = T.dot(X, W) #(n_samples)
        z = z.dimshuffle('x')#(n_samples, 1)

        b_hat = b.copy()

        scores = T.cumsum(z-b_hat) #(n_samples, n_classes)
        output = T.argmax(scores) #n_samples integers

        self.score = theano.function([X],scores)
        self.pred = theano.function([X],output)

        #Loss function
        L = T.sum(scores[output] - scores[Y])
        #error count
        err = T.sum(T.neq(output,Y))
        
        #compute gradient
        updates = []
        for p in self.params:
            gP = T.grad(L,p)
            updates.append((p,p-gP))

        #compile train function
        self.train = theano.function([X,Y],[L,err],updates=updates)
        self.err = theano.function([X,Y],err)
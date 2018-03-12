import numpy as np

import theano
import theano.tensor as T

# Algoritmo do Ordinal Perceptron

class OrdinalPerceptron:

    def __init__(self, n_classes, n_features):
        #aprendizado por linha
        X = T.dvector('x')
        #classe de saída é um inteiro
        Y = T.iscalar('y')

        W = theano.shared(np.zeros((n_classes, n_features)))
        
        self.params = [W]
        
        z = T.dot(X, W.T) #(n_samples, n_classes)
        scores = T.cumsum(z) #(n_samples, n_classes)
        output = T.argmax(scores) #n_samples integers

        self.pred = theano.function([X],output)

        #Loss function
        L = T.sum(scores[output] - scores[Y])
        #error count
        err = T.sum(T.neq(output,Y))

        #compute gradient
        gW = T.grad(L,W)

        #update
        updates = [(W,W-gW)]
        self.train = theano.function([X,Y],[L,err],updates=updates)

        self.err = theano.function([X,Y],err)
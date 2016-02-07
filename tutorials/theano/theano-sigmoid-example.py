import theano
import theano.tensor as T
x = T.dmatrix('x')
s = 1 / (1 + T.exp(-x))
logistic = theano.function([x], s)
x=logistic([[0, 1], [-1, -2]])
print(x)
first_row=x[0]
assert first_row[0] == 0.5
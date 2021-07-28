scikit tutorial


#splitting dataset:

from sklearn.model_selection import train_test_split
x,y,X,Y=train_test_split('inp,out,test-size,random_state')

random_state:- It is used to guarantee that the split will always be the same.

#train the model:

1.from sklearn.linear_model import Linearregression

2.import LogisticRegression ('penalty,random_state,solver,multi classs')

penalty:-regularization L1,L2
solver:-represents which algo to use in optimization problem
    liblinears: small datasets,L1,for multiclass
    newton-cg: L2
    lbfgs: L2,for multiclass -multinomial loss
    saga: large datasets,for multiclass-multinomial loss,L1
    sag: similar to saga
max_iter:-max number of iterations for solvers to converge

3.import Ridge('alpha,fit_intercept'): loss func-linear least squares,L2

alpha:-tuning param decides how much to penalize
fit_intercept:-default to False

4.import Bayesianridge(): Bayesian regression allows a natural mechanism to survive insufficient data or poorly distributed data by formulating linear regression using probability distributors rather than point estimates.

5.import Lasso():LASSO-Least Absolute Shrinkage and Selection Operator

LASSO is the regularisation technique that performs L1 regularisation. It modifies the loss function by adding the penalty (shrinkage quantity) equivalent to the summation of the absolute value of coefficients.

#Model persistence

to save the model
from sklearn.externals import joblib
joblib.dump(trained_model,'name')
joblib.load('name')

#preprocessing data

form sklearn import preprocessing

1.binarisation:when we need to convert our numerical values into Boolean values.
preprocessing.Binarizer('threshold=').transform(inp_data)

the value above threshold converted to 1

2.mean removal: used to eliminate the mean from feature vector so that every feature centered on zero.

x=preprocessing.scale('inp_data')
x.mean('axis') / x.std('axis')

3.Scaling: scaling feature vectors -should not be synthetically large or small.

x = preprocessing.MinMaxScaler('feature_range=()')
x.fit_transform('inp_data')

4.Normalisation

preprocessing.normailze('input_data,norm=l1/l2')




from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler


class FsProblem :
    def __init__(self,data,qlearn):
        self.data=data
        self.nb_attribs= len(self.data.columns)-1 
        self.outPuts=self.data.iloc[:,self.nb_attribs]
        self.ql = qlearn
        self.nb_actions = len(self.ql.actions)
        self.classifier = KNeighborsClassifier(n_neighbors=3)

    def evaluate(self,solution):
        list=[i for i, n in enumerate(solution) if n == 1]
        if (len(list)== 0):
            return 0
        df = self.data.iloc[:,list]
        
        
        array=df.values
        nb_attribs =len(array[0])
        
        X = array[:,0:nb_attribs]
        Y = self.outPuts
        train_X, test_X, train_y, test_y = train_test_split(X, Y, 
                                                    random_state=0,
                                                    test_size=0.3
                                                    )
        
        """
        sc_X = StandardScaler()
        train_X = sc_X.fit_transform(train_X)
        test_X = sc_X.transform(test_X)
        self.classifier= SVC(random_state=0, kernel='rbf')  
        """
        self.classifier.fit(train_X,train_y)
        predict= self.classifier.predict(test_X) 
        return metrics.accuracy_score(predict,test_y)
    
    def nbrUn(self,solution):
        return len([i for i, n in enumerate(solution) if n == 1])
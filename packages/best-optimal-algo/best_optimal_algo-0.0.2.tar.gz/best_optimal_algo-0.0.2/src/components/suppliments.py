from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from catboost import CatBoostClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
import numpy

models = {
    # "Logistic Regression": LogisticRegression(),
    # "K-Nearest Neighbors": KNeighborsClassifier(),
    # "Support Vector": SVC(),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(),
    "XGB": XGBClassifier(), 
    "CatBoosting ": CatBoostClassifier(verbose=False),
    "AdaBoost ": AdaBoostClassifier(),
    "GradientBoost": GradientBoostingClassifier()
}

params={    
            # "Logistic Regression":{},   
            
            # "K-Nearest Neighbors":{ 
            #     'n_neighbors' : [5,7,9,11,13,15],
            #     'weights' : ['uniform','distance'],
            #     'metric' : ['minkowski','euclidean','manhattan']},
            
            # "Support Vector": {},
     
            "Decision Tree":{
                'max_depth':[3,5,7,10,15],
                'min_samples_leaf':[3,5,10,15,20],
                'min_samples_split':[8,10,12,18,20,16],
                'criterion':['gini','entropy']},

            "Random Forest":{
                'criterion':['gini', 'log_loss', 'entropy'],
                'max_features':['sqrt','log2',None],
                'n_estimators': [8,16,32,64,128,256]
                },

            "XGB":{
                'learning_rate':[.1,.01,.05,.001],
                'n_estimators': [8,16,32,64,128,256]
                },

            "CatBoosting ":{
                'depth': [6,8,10],
                'learning_rate': [0.01, 0.05, 0.1],
                'iterations': [30, 50, 100]
                },

            "AdaBoost ":{
                'learning_rate':[.1,.01,0.5,.001],
                # 'loss':['algorithm', 'base_estimator', 'estimator', 'learning_rate', 'n_estimators', 'random_state'],
                'n_estimators': [8,16,32,64,128,256]
                },

            "GradientBoost":{
                'loss':['exponential', 'log_loss'],
                'learning_rate':[.1,.01,.05,.001],
                'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                'criterion':['squared_error', 'friedman_mse'],
                'max_features':['auto','sqrt','log2'],
                'n_estimators': [8,16,32,64,128,256]
                }
                
            }

def metrics(true, predicted):
    
    accuracy = accuracy_score(true, predicted)
    f1 = f1_score(true, predicted)
    precision = precision_score(true, predicted)
    recall = recall_score(true, predicted) 
    eval_metric = [accuracy, f1, precision, recall]

    return eval_metric
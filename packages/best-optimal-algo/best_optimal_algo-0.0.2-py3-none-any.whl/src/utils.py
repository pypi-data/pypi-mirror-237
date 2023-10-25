from sklearn.model_selection import GridSearchCV
from src.components.suppliments import params, models, metrics
import pandas as pd
import numpy as np

def evaluate_models(X_train, y_train,X_test,y_test):
    try:
        accuracies = []
        f1Score = []
        precisionScore = []
        recallScore = []
        applied_params = []
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=params[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train, np.ravel(y_train))

            model.set_params(**gs.best_params_)
            
            para:dict =  gs.best_params_
            # print(para)
            
            model.fit(X_train,np.ravel(y_train))
            
            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            eval_metric: list = metrics(y_test, y_test_pred)

            accuracies.append(eval_metric[0])
            f1Score.append(eval_metric[1])
            precisionScore.append(eval_metric[2])
            recallScore.append(eval_metric[3])
            applied_params.append(para)

            model_score = pd.DataFrame(list(zip( accuracies, f1Score, precisionScore, recallScore, applied_params)), columns=['Accuracy', 'F1-score', 'Precision', 'Recall', 'Parameters']).sort_values(by=["Accuracy"],ascending=False)

            report[list(models.keys())[i]] = model_score

            model_summary = pd.DataFrame(list(zip(models, accuracies, f1Score, precisionScore, recallScore)), columns=['Model Name', 'Accuracy', 'F1-score', 'Precision', 'Recall']).sort_values(by=["Accuracy"],ascending=False)

            param_summary = pd.DataFrame(list(zip(models, accuracies, applied_params)), columns=['Model Name', 'Accuracy', 'Parameters']).sort_values(by=["Accuracy"],ascending=False)

        return model_summary, param_summary
    except Exception as e:
        print(e)
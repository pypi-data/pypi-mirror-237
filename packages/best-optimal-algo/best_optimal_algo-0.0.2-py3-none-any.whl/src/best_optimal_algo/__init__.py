from src.utils import evaluate_models

def best_optimal_algo(X_train , X_test, y_train, y_test):
        
    # self.X_train = X_train
    # self.X_test = X_test
    # self.y_train = y_train
    # self.y_test = y_test

    model, params = evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test)
        
        # best_model_score = max(sorted(model_report.values()))

        ## To get best model name from dict
        # best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
        
    print(model)
    for p in params['Parameters']:
            #print(list(zip(p.keys(),p.values())))
        print(p)

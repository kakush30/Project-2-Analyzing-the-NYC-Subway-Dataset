import matplotlib.pyplot as plt
import pandas
import statsmodels.api as sm
import scipy
import numpy as np



"""
In this question, you need to:
1) implement the linear_regression() procedure
2) Select features (in the predictions procedure) and make predictions.

"""

def predictions_and_rsq(files):
    """
    Perform linear regression given a data set with an arbitrary number of features.
    
    This can be the same code as in the lesson #3 exercise.
    """
    
    ###########################
    ### YOUR CODE GOES HERE ###
    ###########################
    df = pandas.read_csv(files)
    df = df[:13000]
    features = df[['rain', 'precipi', 'Hour', 'meantempi']]
    dummy_units = pandas.get_dummies(df['UNIT'], prefix='unit')
    features = features.join(dummy_units)
    values = df['ENTRIESn_hourly']
    
   
   
    features = sm.add_constant(features)
    model = sm.OLS(values, features).fit()
    results_rsquare = model.rsquared
    results = model.summary()
    results_params = model.params
    
    results_predict = model.predict(features)
    
    data = df['ENTRIESn_hourly']
    #data_exits = df['EXITSn_hourly'].sum()
    #print(data_entries)
    #print(data_exits)
    s1 = np.sum((data - results_predict)**2)
    s2 = np.sum((data - np.mean(data))**2)
    rsquare_formula = 1 - s1/s2    
    
    #(df['ENTRIESn_hourly'] - results_predict).hist(bins=200)
    #plt.suptitle('Residual')
    #plt.xlabel('Residuals')
    #plt.ylabel('Frequency')
    scipy.stats.probplot(data - results_predict,plot=plt)
    
    #plt.plot(df['ENTRIESn_hourly'] - results_predict)
    
    plt.show()
        
    #return model_prob
    
if __name__ == '__main__':
    
    print predictions_and_rsq('turnstile_data_master_with_weather.csv')

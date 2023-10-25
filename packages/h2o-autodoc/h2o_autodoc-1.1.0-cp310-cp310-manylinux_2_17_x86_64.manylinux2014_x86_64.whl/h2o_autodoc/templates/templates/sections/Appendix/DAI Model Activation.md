{% if ('IsolationForestAnomalyModel' in final_model._final_model_string) %}

**Under Expert Settings, setting the enable_isolation_forest**

Isolation Forest https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html is useful for identifying anomalies or outliers in data.

This option lets you specify whether to return the anomaly score of each sample. This is disabled by default, until the model is selected explicitly for use.

**Under Expert Settings, setting the isolation_forest_nestimators**

Specify the number of estimators for Isolation Forest https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html encoding. 

This value defaults to 200.

{% endif %}

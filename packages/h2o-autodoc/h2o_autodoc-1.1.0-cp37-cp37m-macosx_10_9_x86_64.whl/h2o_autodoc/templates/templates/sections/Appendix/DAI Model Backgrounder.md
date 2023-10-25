{% if ('IsolationForestAnomalyModel' in final_model._final_model_string) %}

This section details the isolation forest algorithm used in the DAI unsupervised learning module.

Isolation forest as based on this published paper https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/icdm08b.pdf isolates or identifies the anomalous entries by randomly splitting the decision trees. 

The idea is that an *outlier* will lie farther away from the regular observations in the feature space and hence will require fewer random splits to isolate to the terminal node of a tree. 

Isolation Forest is useful for identifying anomalies or outliers in data. Isolation Forest isolates observations by randomly selecting a feature and then randomly selecting a split value between the maximum and minimum values of that selected feature. 

This split depends on how long it takes to separate the points. Random partitioning produces noticeably shorter paths for anomalies. 

When a forest of random trees collectively produces shorter path lengths for particular samples, they are highly likely to be anomalies.

The algorithm assigns an anomaly score to each observation based on its path length (from root node to terminal node) in the forest. The lower the score, the more likely it is that the row is an anomaly.

Internally, Driverless AI runs sklearn's Isolation Forest https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html implementation.

{% endif %}

### Assumptions and Limitations

Driverless AI trains all models based on the training data provided (in this case: *{{experiment.parameters.dataset.display_name|e}}*). It is the assumption of Driverless AI that this dataset is representative of the data that will be seen when scoring.

{% if experiment.score_f_name != 'UNSUPERVISED' %}

Driverless AI may perform shift detection between the {{data_info._comparison_string}}.  If a shift in distribution is detected, this may indicate that the data that will be used for scoring may have distributions not represented in the training data.  {% if valid_predictions_path == '' %} The model may have poorer performance than seen on the internal validation data. {% endif %}

For this experiment, Driverless AI {% if experiment.test_predictions_path == '' and experiment.valid_predictions_path == ''%} was not able to detect any shift in distribution between {{data_info._comparison_string}} because no validation or test data was provided. {% elif experiment_overview._internal_args.check_distribution_shift == False %} did not detect any shift in distribution because shift detection was turned off due to the accuracy setting (increase accuracy setting for shift detection). {% elif data_info._shift_table == None %} performed shift detection but found no significant changes in the distribution of the {{data_info._comparison_string}}. {% else %} performed shift detection and found significant differences described below: 

{{data_info._shift_table}}

{% endif %}
{% endif %}


{% if ('IsolationForestAnomalyModel' in final_model._final_model_string) %}

DAI uses out-of-range imputation that fills missing values with the values beyond the maximum.

DAI does not scale numerical features from with Isolation Forest. As the algorithm can get all outlier data points regardless of the scale used, normalization should not make a difference.

The model only utilizes all numeric features. If it encounters any categorical features, the categorical columns are first converted to numeric, then utilized as part of the training data set.

When using Isolation Forest, pre-transformers procedures are activated by default. However, text features will be ignored. TF/IDF is a poor embedding for anomaly detection.

Any date/time features will also be transformed using Frequency Transformation when makes sense, e.g. in cases where date/time is treated as a categorical feature. Otherwise, date/time features are also ignored for the most part. No feature engineering process is performed on date/time features.

The model will produce scores for anomalies in the form of a float. The lower (or more negative) the score, the higher likelihood that the data is an anomaly. There is no standardized range as it is highly dependent on the type of data you are utilizing and in most cases, is a business-driven decision, e.g. it will not be bounded by a range from -1 to +1.

It is up to the user to create labels from these scores. Quantile value can be used as a (contamination) threshold. For example, if you know that 5% of the rows are anomalous in your dataset, then this can be used to calculate the 95th quantile of the scores. This quantile can act as a threshold to classify each row as being an anomaly or not.

{% endif %}
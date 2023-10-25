{% if ('IsolationForestAnomalyModel' in final_model._final_model_string) %}

Given an anomaly detection experiment, you can create predictions on the training dataset, including all original columns, and re-upload into Driverless AI to run a supervised experiment. 

For a given similar dataset (in production), you now have an unsupervised scorer that tells you the anomaly score for each row, and supervised scorer which makes Shapley per-feature contribution reason codes to explain why each row is an anomaly or not.

{% endif %}

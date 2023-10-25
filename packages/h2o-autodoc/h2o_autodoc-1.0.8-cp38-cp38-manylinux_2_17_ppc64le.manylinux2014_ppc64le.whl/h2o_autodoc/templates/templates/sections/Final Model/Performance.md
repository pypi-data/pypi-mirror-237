**Performance of Final Model**

{% if params._params.is_classification == True %}

Some metrics below require the probabilities to be converted into labels. Predicted labels are generated based on some probability threshold. 
For example, we may say the label is "YES" if the probability is greater than 0.5.

Choosing this threshold can greatly change the performance metric. 
This can be seen in the ROC and Precision Recall curves on the Driverless AI UI, where different thresholds on the curve are highlighted, that marks the best Accuracy, the best MCC, and the best F1.

In the Performance Table below, some metrics that require labels have been calculated so that the threshold chosen optimizes the metric. 
The metrics whose thresholds are optimized are: Accuracy, MCC, F1, F05, and F2.
Other metrics that require labels like Precision and Recall choose the threshold that optimizes the 
{{config.threshold_scorer}} because these are trivial to optimize (i.e, Recall will always be perfect when the threshold is 0).

{% endif %} 

{{final_model.get_final_model_scores()}}

{% if params._params.is_classification and final_model._confusion_matrix != {} and "validation" in final_model._confusion_matrix.keys()%}

**Validation Confusion Matrix**

Here for the confusion matrix, Driverless AI chose the threshold that maximizes the {{config.threshold_scorer}} value on the validation data. 

If no validation data was explicitly provided and Driverless AI used cross validation, 
then the threshold that maximizes the {{config.threshold_scorer}} value would be found for each internal fold and, the mean of these thresholds would be calculated.

Note: By default, the confusion matrix that results in best F1 value on some holdout data will be displayed here. 
This can be configured/changed by assigning different scorer to [threshold scorer in recipe settings](https://docs.h2o.ai/driverless-ai/1-10-lts/docs/userguide/expert_settings/recipes_settings.html#threshold-scorer).

{%if final_model.valid_cm_threshold| e == 'argmax' %}The prediction label is assigned to the class with the highest predicted probability.{% else %}*Threshold {{final_model.valid_cm_threshold}}*{% endif %}

{{final_model._confusion_matrix.validation}}

{% endif %} 

{% if params._params.is_classification and experiment.test_score != None  and final_model._confusion_matrix != {} and "test" in final_model._confusion_matrix.keys() %} 

**Test Confusion Matrix**

Here for the confusion matrix, Driverless AI chose the threshold that maximizes the {{config.threshold_scorer}} value on the validation data. 

If no validation data was explicitly provided and Driverless AI used cross validation, 
then the threshold that maximizes the {{config.threshold_scorer}} value would be found for each internal fold and, the mean of these thresholds would be calculated.

Note: By default, the confusion matrix that results in best F1 value on some holdout data will be displayed here. 
This can be configured/changed by assigning different scorer to [threshold scorer in recipe settings](https://docs.h2o.ai/driverless-ai/1-10-lts/docs/userguide/expert_settings/recipes_settings.html#threshold-scorer).

{%if final_model.test_cm_threshold| e == 'argmax' %}The prediction label is assigned to the class with the highest predicted probability.{% else %}*Threshold {{final_model.test_cm_threshold}}*{% endif %}

{{final_model._confusion_matrix.test}}

{% endif %} 

{% if experiment.test_score == None %}

{% for key, value in final_model._plots.items() %}

*{{ value.desc |e}}*

{{ images.get(value.validation_filename)}}


{% endfor %} {% else %} 

{% for key, value in final_model._plots.items() %}

*{{ value.desc |e}}*

{{ images.get(value.validation_filename, '')}}
{{ images.get(value.test_filename, '')}}

{% endfor %} 

{% endif %}

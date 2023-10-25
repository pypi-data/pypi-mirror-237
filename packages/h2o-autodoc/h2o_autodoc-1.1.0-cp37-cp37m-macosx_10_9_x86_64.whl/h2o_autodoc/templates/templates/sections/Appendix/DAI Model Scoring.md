{% if ('IsolationForestAnomalyModel' in final_model._final_model_string) %}

When building a model, the Accuracy and Time knobs of Driverless AI can be toggled to adjust the effort spent on model tuning as appropriate. Presently as there is no scorer being used for isolation forest. 

When doing genetic algorithm, the model will converge immediately and use one of the models from the tuning phase as the final model. 

The Interpretability knob is ignored in the default set up. The number of trees or n_estimators for the isolation forest model can be adjusted with the “isolation_forest_nestimators” expert setting parameter.

After building the model, the anomaly scores can be obtained by predicting on the same dataset. The lower the scores for the row, the more likely it is an outlier or anomaly as determined by the model. 

The Visualize Scoring Pipeline option summarizes the features used and transformations applied in building the model.

To create binary classification **labels** from these scores, quantile value can be used as a threshold. For example, if you know that 5% of the rows are anomalous in your dataset, then this can be used to calculate the 95th quantile of the scores. This quantile can act as a threshold to classify each row as being an anomaly or not. Alternatively, one can also use the anomaly scores as is, i.e. as a numerical float feature or target for another model.


{% endif %}

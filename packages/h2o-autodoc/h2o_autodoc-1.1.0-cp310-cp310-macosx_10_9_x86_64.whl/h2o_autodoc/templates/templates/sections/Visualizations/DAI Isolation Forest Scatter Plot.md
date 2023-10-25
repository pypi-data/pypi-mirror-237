### Isolation Forest Scatter Plots

To interpret the output of an Isolation Forest model, you can examine the scores for each sample and identify those with low scores as potential outliers. You can also use the scores to create a threshold and label samples with scores below the threshold as outliers.

It's important to note that Isolation Forest is sensitive to the contamination parameter, which determines the proportion of outliers in the dataset. If the contamination parameter is set too low, the model may not identify any outliers, and if it is set too high, the model may identify too many outliers. Therefore, it's important to tune the contamination parameter appropriately for your dataset.

When documenting the output and results of an Isolation Forest model, data scientists typically focus on the following aspects:
- The contamination parameter: This is an important parameter that determines the proportion of outliers in the dataset. Data scientists often document the value of the contamination parameter used in the model and how it was determined.
- The number of samples identified as outliers: Data scientists typically report the number of samples that were identified as outliers and the percentage of the total dataset that they represent.
- The distribution of outlier scores: Data scientists often plot the distribution of outlier scores to visually assess the relative isolation of each sample. This can be helpful in identifying any clusters of outliers and understanding the overall distribution of scores.
- The performance of the model: Data scientists may also report the performance of the model, such as the accuracy or F1 score, depending on the evaluation metric used when the anomaly score or label is used as the target label of a supervised model.
- The implications of the results: Data scientists often discuss the implications of the results and how the identified outliers might be further investigated or used in subsequent analysis.

It's important to note that the specific details that data scientists look for when documenting the output and results of an Isolation Forest model will depend on the context and the goals of the analysis.

#### Plot Details
This will create a scatter plot with the x-axis representing the index of each sample and the y-axis representing the isolation score. You can then visually inspect the plot to identify any clusters of low scores, which correspond to outlier samples.

The scatter plot created will have with blue points for non-outlier samples and red points for outlier samples. Each plot assumes various contamination thresholds set at 1%, 3%, and 5% for further analysis.

A scatter plot can be used to visualize the isolation scores for each sample in the dataset. This can be helpful in identifying any clusters of low scores, which correspond to outlier samples.

{% for title, rendered_image in unsupervised_plots["isolation_forest_plots"].scatter_plots.items() %}

**Scatter plot with {{ title }}**

{{ rendered_image }}

{% endfor %}

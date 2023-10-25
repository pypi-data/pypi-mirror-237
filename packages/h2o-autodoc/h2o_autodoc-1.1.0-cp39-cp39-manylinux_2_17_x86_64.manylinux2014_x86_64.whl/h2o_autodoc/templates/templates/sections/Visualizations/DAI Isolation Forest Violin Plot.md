### Isolation Forest Violin Plots

The violin plot is a combination of a box plot and a kernel density plot. It shows the distribution of data along with the actual data points, which can be helpful in understanding the shape and spread of the anomalies. 


#### Plot Details

This will create violin plots with the x-axis representing the anomaly category, True (colored Amber) being an anomaly, and False (colored Blue) being not an anomaly. You can then visually inspect the plot to identify any clusters of low scores, which correspond to outlier samples.

Each plot assumes various contamination thresholds set at 1%, 3%, and 5% for further analysis.

Violin plots can be useful for comparing the distribution of isolation scores across the anomaly label categories.

{% for title, rendered_image in unsupervised_plots["isolation_forest_plots"].violin_plots.items() %}

**Violin plot with {{ title }}**

{{ rendered_image }}

{% endfor %}

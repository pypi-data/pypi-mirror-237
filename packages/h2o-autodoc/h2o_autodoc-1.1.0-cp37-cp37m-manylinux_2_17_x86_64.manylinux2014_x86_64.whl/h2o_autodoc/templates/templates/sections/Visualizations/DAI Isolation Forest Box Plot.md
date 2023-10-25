### Isolation Forest Box Plots

The Isolation Forest box plot will show the distribution of a dataset by displaying the minimum, first quartile, median, third quartile, and maximum values. 

#### Plot Details

This will create a boxplot with the x-axis representing the anomaly category, True (colored Amber) being an anomaly, and False (colored Blue) being not an anomaly. This created in context of the contamination parameter. You can then visually inspect the plot to identify any clusters of low scores, which correspond to outlier samples.

Each plot assumes various contamination thresholds set at 1%, 3%, and 5% for further analysis.

Boxplot can be useful for comparing the distribution of isolation scores across anomaly labels. This can be helpful in identifying any clusters of low scores, which correspond to outlier samples. It can also sometimes show outlying stragglers that might assist in setting the correct contamination threshold for further analysis.

{% for title, rendered_image in unsupervised_plots["isolation_forest_plots"].box_plots.items() %}

**Box plot with {{ title }}**

{{ rendered_image }}

{% endfor %}

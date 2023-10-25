### Isolation Forest Histograms

The Isolation Forest histogram is a graphical display of data that shows the frequency or probability of different score values in a dataset.

#### Plot Details

The histograms show the relative frequency of different values of the variable by dividing the range of the variable into bins and plotting the frequency of observations that fall into each bin as a bar.

The histogram created will have the x-axis representing the isolation scores in a 20-bin bucket, and the y-axis showing the count of each bin. You can then visually inspect the plot to identify any clusters of low scores, which correspond to outlier samples.

The bars colored red gives a visual cue that the anomaly scores are of a negative value, in contrast with the positive values, colored in blue . A negative anomaly score might not necessarily mean that it’s an anomaly, and thus, would warrant more analysis to determine what threshold the true anomalies start at.

The histograms can be used to visualize the distribution of isolation scores and understand the relative frequency of different score values.

**Isolation Forest Score Histogram**

{{ unsupervised_plots["isolation_forest_plots"].histogram }}

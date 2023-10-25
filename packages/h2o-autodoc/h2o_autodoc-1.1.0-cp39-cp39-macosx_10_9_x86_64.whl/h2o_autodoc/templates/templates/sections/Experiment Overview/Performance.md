### Performance

{% if experiment.score_f_name != 'UNSUPERVISED' %}{{experiment_overview.get_performance_table()}}{% else %}There are no performance metrics, no validation, and no holdout tests done on this model. It's mostly just uses the Scikit-Learn sklearn IsolationForest.{% endif %}

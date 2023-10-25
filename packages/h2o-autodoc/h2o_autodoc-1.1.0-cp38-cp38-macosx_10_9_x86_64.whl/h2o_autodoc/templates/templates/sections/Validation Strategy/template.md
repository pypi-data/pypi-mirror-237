{% if experiment.score_f_name != 'UNSUPERVISED' %}

{% if validation_schema.user_provided_valid_data %}{{ validation_schema.user_provided_valid_text }}{% elif validation_schema._ga_disabled %} {{ section.render('Validation Strategy.DAI Recipe Validation') }} {% elif params._params.time_col != '[OFF]'%} {{ section.render('Validation Strategy.DAI Time Series Validation')}} {% else %} {{ section.render('Validation Strategy.DAI Fold Information')}} {% endif %}

{% else %}

Driverless AI did not perform any validation testing. This is not applicable to this model type.

{% endif %}

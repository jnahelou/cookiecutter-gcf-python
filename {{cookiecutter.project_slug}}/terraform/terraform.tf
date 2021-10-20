terraform {
  required_providers {
		{%- if cookiecutter.use_monitoring == "datadog" %}
    datadog = {
      source = "datadog/datadog"
    }
		{%- endif %}
    google = {
      source = "hashicorp/google"
    }
  }
  required_version = ">= 1.0.0"
}

{%- if cookiecutter.use_monitoring == "datadog" %}
provider "datadog" {
  api_url = "https://api.datadoghq.eu/"
}

resource "datadog_monitor" "alert-slack" {
  name           = "{{cookiecutter.app_display_name}} function errored"
  type           = "metric alert"
  message        = "{{cookiecutter.app_display_name}} completion in error !"
  query          = "sum(last_5m):sum:gcp.cloudfunctions.function.execution_count{function_name:${var.function_name},status:error,project_id:${var.project_id}}.as_count() > 0"
  timeout_h      = 1
  notify_no_data = false
  monitor_thresholds {
    critical = 0.1
  }
  notify_audit   = false
  new_host_delay = 300

  tags = var.tags
}
{%- endif %}
{%- if cookiecutter.use_monitoring == "operation" %}
resource "google_monitoring_alert_policy" "alert_policy" {
  display_name = "{{cookiecutter.app_display_name}} function errored"
	combiner     = "AND"
  conditions {
    display_name = "completion failed"
    condition_threshold {
      filter     = "metric.type=\"cloudfunctions.googleapis.com/function/execution_count\" AND resource.type=\"cloud_function\" AND resource.function_name == \"${var.function_name}\" AND metric.status != \"ok\""
      duration   = "60s"
			threshold_value = 0
      comparison = "COMPARISON_GT"
      aggregations {
        alignment_period   = "60s"
        per_series_aligner = "ALIGN_RATE"
      }
    }
  }
}
{%- endif %}

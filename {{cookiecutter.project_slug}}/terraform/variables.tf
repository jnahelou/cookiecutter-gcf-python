variable "project_id" {
  type        = string
  description = "Project used to deploy"
}

variable "tags" {
  type        = set(string)
  description = "Tags to set on components"
  default     = ["service:hello-function"]
}

variable "function_name" {
  type        = string
  description = "Name of the Google Cloud Function"
  default     = "hello-function"
}

locals {
  labels = {
    creator = "terraform"
  }
}

provider "google" {
  region  = "europe-west1"
  project = var.project_id
}

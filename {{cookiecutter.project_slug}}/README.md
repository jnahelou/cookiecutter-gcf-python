# {{cookiecutter.project_slug}}

{{cookiecutter.project_short_description}}


## How to deploy

Configure `direnv` config file `.envrc` to configure Google settings and credentials

### Set IAM permissions

Create a service account used to run the function.
```
gcloud iam service-accounts create {{cookiecutter.project_slug}} --project $GOOGLE_PROJECT
```

Grant SA IAM permissions to run. Note : This part can be done using Terraform code !

```
gcloud projects add-iam-policy-binding --member "serviceAccount:{{cookiecutter.project_slug}}@$GOOGLE_PROJECT.iam.gserviceaccount.com" --role 'roles/monitoring.metricWriter' $GOOGLE_PROJECT
```

### Deploy the function

```
gcloud functions deploy hello-function --trigger-http --entry-point main --runtime python38 --region europe-west1 --service-account={{cookiecutter.project_slug}}@$GOOGLE_PROJECT.iam.gserviceaccount.com --set-env-vars="GOOGLE_PROJECT=$GOOGLE_PROJECT" --project $GOOGLE_PROJECT
```

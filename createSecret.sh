gcloud sql databases create kinmusic-kinideas-profile-database --instance=kinmusic-postgresql-v14

gcloud secrets create kinideas_profile_settings --replication-policy automatic
gcloud secrets versions add kinideas_profile_settings --data-file .env

gcloud secrets add-iam-policy-binding kinideas_profile_settings \
    --member serviceAccount:299791645258@cloudbuild.gserviceaccount.com \
    --role roles/secretmanager.secretAccessor
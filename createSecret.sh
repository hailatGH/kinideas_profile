gcloud sql databases create kinmusic-kinideas-profile-database-dev --instance=kinmusic-postgresql-v14

gcloud secrets create kinideas_profile_settings_dev --replication-policy automatic
gcloud secrets versions add kinideas_profile_settings_dev --data-file .env.dev

gcloud secrets add-iam-policy-binding kinideas_profile_settings_dev \
    --member serviceAccount:299791645258@cloudbuild.gserviceaccount.com \
    --role roles/secretmanager.secretAccessor
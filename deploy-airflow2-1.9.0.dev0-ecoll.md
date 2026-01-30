# DEPLOY

```shell
ansible-helper -i ecoll.yml -e deploy_type=airflow_dags -e deploy_services_suffix=_af -e artifact_name=airflow_dags -e artifact_version=1.9.0.dev0 -e skip_deploy=False -e artifact_checksum={CHECKSUM_SHA1_DELLO_ZIP} -e artifact_checksum_type=sha1 tplatform_deploy_nexus.yml --limit ecoll-esg

```

```shell
-- 9c6058c93ce5aff9473eafd863f14a2c5af00850
ansible-helper -i ecoll.yml -e deploy_type=airflow_dags -e deploy_services_suffix=_af -e artifact_name=airflow_dags -e artifact_version=1.9.0.dev0 -e skip_deploy=False -e artifact_checksum=9c6058c93ce5aff9473eafd863f14a2c5af00850 -e artifact_checksum_type=sha1 tplatform_deploy_nexus.yml --limit ecoll-esg

```



import akerbp.mlops.model_manager as mm

# Need to run this when deploying trend curves model in bitbucket CI/CD pipeline
if __name__ == "__main__":
    mm.setup()

    models = ["automatic_vsh"]
    envs = ["prod"]
    versions = [22]

    for model, env, version in zip(models, envs, versions):
        mm.download_deployment_folder(
            model_name=model,
            env=env,
            version=version,
            files_to_ignore=[
                "requirements.txt",
                "handler.py",
                "mlops_service_settings.yaml",
            ],
            target_path="model_code",
        )

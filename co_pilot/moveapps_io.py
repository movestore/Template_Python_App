import os
import logging


class MoveAppsIo:

    @staticmethod
    def get_app_file_path(appspec_local_file_setting_id: str, fallback_to_provided_files: bool = True) -> str:
        """
        Provides the path to app-files. App-files are files that
        - are needed by the app to work during run time
        - gets uploaded by the user of this app during configuration time
        - there will be no warning if the requested file-set is not available (eg the user did not upload anything and the
          app developer did not provide any fallback)
        - can also be provided by the app developer and gets bundled into the app during build time (the fallback)

        :param appspec_local_file_setting_id The ID of the requested set of app-files
            (see counterpart in `appspec.json` (setting[type=LOCAL_FILE].id))
        :param fallback_to_provided_files Fallback to bundled directory of requested set of app-files
            (in case the app-developer provided a fallback)?
        :return: Path to the requested set of files (the app-file parent directory).
            Or `NULL` if user did not upload anything and no fallback was provided
        """
        if appspec_local_file_setting_id:
            local_app_files_root = os.environ.get('LOCAL_APP_FILES_DIR', './resources/local_app_files')
            user_upload_dir = os.path.join(
                local_app_files_root,
                os.environ.get('LOCAL_APP_FILES_UPLOADED_SUB_DIR', 'uploaded-app-files'),
                appspec_local_file_setting_id
            )
            if os.path.exists(user_upload_dir) and len(os.listdir(user_upload_dir)) > 0:
                # directory exists and is not empty: user provided some files
                logging.info(f'Detected app-files provided by user for \'{appspec_local_file_setting_id}\'.')
                return user_upload_dir
            elif fallback_to_provided_files:
                # fallback to directory provided by app developer
                provided_dir = os.path.join(
                    local_app_files_root,
                    os.environ.get('LOCAL_APP_FILES_PROVIDED_SUB_DIR', 'provided-app-files'),
                    appspec_local_file_setting_id
                )
                if os.path.exists(provided_dir) and len(os.listdir(provided_dir)) > 0:
                    logging.info(
                        f'Using fallback files provided by app developer for \'{appspec_local_file_setting_id}\'.'
                    )
                    return provided_dir
        logging.warning(
            f'No files present for app-files \'{appspec_local_file_setting_id}\': '
            f'User did not upload anything and the app did not provide fallback files.'
        )

    @staticmethod
    def create_artifacts_file(artifact_file_name: str) -> str:
        """
        Provides the path to an app-artifact.
        You can write the app generated file to this path and it will become available on MoveApps after each app run.

        :param artifact_file_name: The name of the artifact
        :return: Path for the artifact. Use it to write your data
        """
        app_artifacts_dir = os.environ.get('APP_ARTIFACTS_DIR', './resources/output')
        return os.path.join(app_artifacts_dir, artifact_file_name)

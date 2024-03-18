import os
import logging
from deprecated import deprecated


class MoveAppsIo:

    @staticmethod
    def get_auxiliary_file_path(appspec_user_file_setting_id: str, fallback_to_provided_file: bool = True) -> str | None:
        """
        Provides the path to the auxiliary file.
        An auxiliary file is a file that
        - is needed by the app to work during run time
        - gets uploaded by the user of this app during configuration time
        - there will be no warning if the requested file is not available (eg the user did not upload anything and
            the app developer did not provide any fallback)
        - can also be provided by the app developer and gets bundled into the app during build time (the fallback)

        :param appspec_user_file_setting_id The ID of the requested set of app-files
            (see counterpart in `appspec.json` (setting[type=USER_FILE].id))
        :param fallback_to_provided_file: Fallback to bundled directory of requested auxiliary file
            (in case the app-developer provided a fallback)?
        :return Path to requested file. Or `None` if user did not upload anything and no fallback was provided.
        """
        local_app_files_root = os.environ.get('USER_APP_FILE_HOME_DIR', './resources/auxiliary/user-files')
        user_upload_dir = os.path.join(
            local_app_files_root,
            os.environ.get('USER_APP_FILE_UPLOAD_DIR', 'uploaded-app-files')
        )
        app_dev_fallback_dir = os.path.join(
            local_app_files_root,
            os.environ.get('USER_APP_FILE_FALLBACK_DIR', 'provided-app-files')
        )
        path = MoveAppsIo.get_upload_dir_or_fallback_dir(
            appspec_user_file_setting_id,
            fallback_to_provided_file,
            user_upload_dir,
            app_dev_fallback_dir
        )
        if path is None:
            return None
        if len(os.listdir(path)) != 1:
            logging.warning(
                f'[\'{appspec_user_file_setting_id}\'] '
                f'A App setting of type `USER_FILE` must contain exactly 0 or 1 file(s). '
                f'The setting contains \'{len(os.listdir(path))}\' file(s). Therefor returning `None`..'
            )
            return None
        file = os.listdir(path)[0]
        result = os.path.join(path, file)
        logging.info(f'[\'{appspec_user_file_setting_id}\'] Resolved file-name: \'{result}\'')
        return result

    @deprecated(reason="Replaced by app-setting type `USER_FILE` and `get_auxiliary_file_path()`")
    @staticmethod
    def get_app_file_path(appspec_local_file_setting_id: str, fallback_to_provided_files: bool = True) -> str | None:
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
            Or `None` if user did not upload anything and no fallback was provided
        """
        local_app_files_root = os.environ.get('LOCAL_APP_FILES_DIR', './resources/auxiliary/local-files')
        user_upload_dir = os.path.join(
            local_app_files_root,
            os.environ.get('LOCAL_APP_FILES_UPLOADED_SUB_DIR', 'uploaded-app-files')
        )
        app_dev_fallback_dir = os.path.join(
            local_app_files_root,
            os.environ.get('LOCAL_APP_FILES_PROVIDED_SUB_DIR', 'provided-app-files')
        )
        return MoveAppsIo.get_upload_dir_or_fallback_dir(
            appspec_local_file_setting_id,
            fallback_to_provided_files,
            user_upload_dir,
            app_dev_fallback_dir
        )

    @staticmethod
    def get_upload_dir_or_fallback_dir(
            appspec_setting_id: str,
            fallback_to_provided_files: bool,
            user_upload_dir: str,
            app_dev_fallback_dir: str
    ) -> str | None:
        if appspec_setting_id:
            user_upload = os.path.join(
                user_upload_dir,
                appspec_setting_id
            )
            if os.path.exists(user_upload) and len(os.listdir(user_upload)) > 0:
                # directory exists and is not empty: user provided some files
                logging.info(f'[\'{appspec_setting_id}\'] Detected app-files provided by user.')
                return user_upload
            elif fallback_to_provided_files:
                # fallback to directory provided by app developer
                app_dev_fallback = os.path.join(
                    app_dev_fallback_dir,
                    appspec_setting_id
                )
                if os.path.exists(app_dev_fallback) and len(os.listdir(app_dev_fallback)) > 0:
                    logging.info(
                        f'[\'{appspec_setting_id}\'] Using fallback files provided by app developer.'
                    )
                    return app_dev_fallback
        logging.warning(
            f'[\'{appspec_setting_id}\'] No files present for app-files. '
            f'User did not upload anything and the app did not provide fallback files.'
        )
        return None

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

# Changelog SDK

## 2025-07 `v2.3.0`

- introduce app-setting-type `SECRET`

## 2024-09

- switch to [miniforge](https://github.com/conda-forge/miniforge)

## 2024-03 `v2.1.0`

- introduce app-setting-type `USER_FILE`
- deprecate app-setting-type `LOCAL_FILE`

## 2024-02 `v2.0.1`

- introduce `appspec.json` version `1.2`
    - removed `createsArtifacts`. It is safe to remove it completely from your `appspec.json` - MoveApps tries now to fetch artifacts for every running App.
    - verify to include the `null` option for setting types `DROPDOWN` and `RADIOBUTTONS` if `defaultValue` is set to `null`.

## 2023-10 `v2.0.0`

- introduces template versioning (starting w/ `v2.0.0` as this is the second major iteration)
- renamed this GH project from _Python SDK_ to _Template_Python_App_.
- introduces a _Template Synchronization_ GH action. Use it to synchronize your forked app with template updates. If you already forked from the template _before_ SDK `v2.0.0` you can manually add the files `.github/workflows/template-sync.yml` and `.github/.templatesyncignore` to your fork. With these files you can manually execute the GH action named _Template Synchronization_.

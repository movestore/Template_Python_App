# Changelog SDK

## 2023-10 `v2.0.0`

- introduces template versioning (starting w/ `v2.0.0` as this is the second major iteration)
- renamed this GH project from _Python SDK_ to _Template_Python_App_.
- introduces a _Template Synchronization_ GH action. Use it to synchronize your forked app with template updates. If you already forked from the template _before_ SDK `v2.0.0` you can manually add the files `.github/workflows/template-sync.yml` and `.github/.templatesyncignore` to your fork. With these files you can manually execute the GH action named _.github/workflows/template-sync.yml_.

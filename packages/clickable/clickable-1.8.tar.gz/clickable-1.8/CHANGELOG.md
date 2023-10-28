# 1.8 (2023-10-27)

Fix installation (cython 3.0 issue with pyyaml)

# 1.5 (2021-12-25)

Fix packaging.

# v1.4 (2021-12-24)

Publishing procedure update.

# v1.3 (2021-09-24)

Fix subprocess import in syncing module.

# v1.2 (2021-09-24)

Fix subprocess import in sphinx module.

# v1.1 (2021-08-31)

Fix virtualenv syntax issues:

```
AttributeError: 'str' object has no attribute 'decode'
```

```
Uncaught error during execution: name 'e' is not defined
```


# 1.0 (2021-08-31)

* cleaned build system
* tests reworked
* updated dependencies
* updated versioning scheme (major/minor)
* python requirement: mandatory 3.6+ (previously 2.7+)
* ruamel.yaml replaced by PyYAML


# 0.3.0 (2018-12)

* remove clickable.bootstrap module
* clickable.click use 'main' as default function when searching
  an entry-point in clickables.py
* tasks.py renamed to clickables.yml
* added an helper to load base configuration from clickables.yml
  (clickables.utils.load_config)
* python3 support


# 0.2.0 (2018-12-26)

(delayed release, used from @dev branch for 6 months)

* added clickable.bootstrap
* added helpers for sphinx commands
* added workaround for selinux and virtualenv

# 0.1.1 (2018-02-10)

* fix rsync ``options`` arg behavior


# 0.1.0 (2018-02-10)

* added rsync handler


# 0.0.3 (2017-10-17)

* correctly handle clear_env in sphinx:sphinx_script
* update cryptography, tox, sphinx, wheel


# 0.0.1 (2017-09-10)

* First release on PyPI.


# 0.0.2.dev4 (2017-09-10)

* Fixed ignored excludes in lftp_sync

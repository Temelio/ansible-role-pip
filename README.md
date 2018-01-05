# pip

[![Build Status](https://img.shields.io/travis/Temelio/ansible-role-pip/master.svg?label=travis_master)](https://travis-ci.org/Temelio/ansible-role-pip)
[![Build Status](https://img.shields.io/travis/Temelio/ansible-role-pip/develop.svg?label=travis_develop)](https://travis-ci.org/Temelio/ansible-role-pip)
[![Updates](https://pyup.io/repos/github/Temelio/ansible-role-pip/shield.svg)](https://pyup.io/repos/github/Temelio/ansible-role-pip/)
[![Python 3](https://pyup.io/repos/github/Temelio/ansible-role-pip/python-3-shield.svg)](https://pyup.io/repos/github/Temelio/ansible-role-pip/)
[![Ansible Role](https://img.shields.io/ansible/role/14263.svg)](https://galaxy.ansible.com/Temelio/pip/)

Install pip package.

## Requirements

This role requires Ansible 2.2 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Trusty
- Ubuntu Xenial

and use:
- Ansible 2.2.x
- Ansible 2.3.x
- Ansible 2.4.x

### Running tests

#### Using Docker driver

```
$ tox
```

## Role Variables

### Default role variables

``` yaml
# General variables
pip_packages: "{{ _pip_packages }}"


# Specific Debian family vars
pip_repository_update_cache: True
pip_repository_cache_valid_time: 3600
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: Temelio.pip }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Temelio company)
- http://www.temelio.com
- alexandre.chaussier [at] temelio.com

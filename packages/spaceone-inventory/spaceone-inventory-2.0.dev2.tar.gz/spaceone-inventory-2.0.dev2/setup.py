#
#   Copyright 2020 The SpaceONE Authors.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import os
from setuptools import setup, find_packages

setup(
    name='spaceone-inventory',
    version=os.environ.get('PACKAGE_VERSION'),
    description='SpaceONE inventory service',
    long_description='',
    url='https://www.spaceone.dev/',
    author='MEGAZONE SpaceONE Team',
    author_email='admin@spaceone.dev',
    license='Apache License 2.0',
    packages=find_packages(),
    install_requires=[
        'spaceone-api',
        'mongoengine',
        'redis',
        'langcodes',
        'ipaddress',
        'python-consul',
        'fakeredis',
        'mongomock',
        'pandas',
        'openpyxl',
        'requests',
        'jinja2',
    ],
    package_data={
        'spaceone': ['inventory/template/*.html']
    },
    zip_safe=False,
)

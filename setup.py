# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import io
import os

import setuptools  # type: ignore

package_root = os.path.abspath(os.path.dirname(__file__))

version = {}
with open(
    os.path.join(package_root, "google/cloud/documentai_toolbox/version.py")
) as fp:
    exec(fp.read(), version)
version = version["__version__"]

readme_filename = os.path.join(package_root, "README.rst")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

packages = [
    package
    for package in setuptools.find_namespace_packages()
    if package.startswith("google")
]

setuptools.setup(
    name="google-cloud-documentai-toolbox",
    author="Google LLC",
    author_email="googleapis-packages@google.com",
    url="https://github.com/googleapis/python-documentai-toolbox",
    version=version,
    license="Apache 2.0",
    long_description=readme,
    long_description_content_type="text/x-rst",
    packages=packages,
    platforms="Posix; MacOS X; Windows",
    include_package_data=True,
    package_data={
        "google.cloud.documentai_toolbox": ["templates/*.xml.j2"],
    },
    install_requires=(
        "google-api-core>=2.15.0, <3.0.0",
        "pandas[performance,gcp]>=2.0.0, <3.0.0",
        "pyarrow>=15.0.0, <16.0.0",
        "tabulate>=0.9.0, <1.0.0",
        "proto-plus>=1.22.3, <2.0.0",
        "proto-plus >= 1.25.0, <2.0.0; python_version>='3.13'",
        "grpc-google-iam-v1>=0.12.6, <1.0.0",
        "google-cloud-bigquery>=3.5.0, <4.0.0",
        "google-cloud-documentai>=2.29.2, <4.0.0",
        "google-cloud-storage>=1.31.0, <4.0.0",
        "google-cloud-vision>=2.7.0, <4.0.0",
        "numpy>=1.23.5, <2.0.0",
        "intervaltree>=3.0.0",
        "pikepdf>=8.0.0, <9.0.0",
        "immutabledict>=2.0.0, <5.0.0",
        "Pillow>=10.0.0, <11.0.0",
        "Jinja2>=3.1.0, <4.0.0",
    ),
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False,
)

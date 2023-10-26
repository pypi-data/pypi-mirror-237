from datetime import date
import sys
from setuptools import setup, find_packages
# pylint: disable = relative-import
import ddba

pkgs = find_packages()

if __name__ == '__main__':
    name = 'ddba'

    requirements = ['Flask', "openai", "flask_cors"]

    long_description = ''
    # with open('README.md', 'r') as f:
    #     long_description = f.read()

    setup(
        name=name,
        version='0.0.1',
        description='',
        long_description=long_description,
        author='',
        # author_email='noreply@noreply.com',
        python_requires=">=3.6.0",
        url='',
        keywords='',
        packages=pkgs,
        install_requires=requirements,
        entry_points={
            'console_scripts': ['ddba = ddba.command:cli']
        },
        include_package_data=True,
        # package_data={'ddba': ['ddba/frontend/*']},

        # license='Apache License Version 2.0'
    )

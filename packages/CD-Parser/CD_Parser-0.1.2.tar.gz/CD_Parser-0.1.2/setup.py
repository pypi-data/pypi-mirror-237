from setuptools import setup, find_packages
from cd_parser.version import (__version__)


setup(
    name='CD_Parser',
    version=__version__,
    description='An wrapper around the wonderful re and lmxl libraries to make it easier for new users and old. To scrape pages',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='codedocta',
    author_email='codedocta@gmail.com',
    url='https://codedocta.com',
    packages=find_packages(),
    install_requires=[
        'lxml==4.9.3',
    ],
    classifiers=[
        # For a list of valid classifiers, see https://pypi.org/classifiers/
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    project_urls={
        'Bug Reports': 'https://github.com/codedocta/CD_Parser/issues',  # Replace with your issues URL
        'Source': 'https://github.com/codedocta/CD_Parser/',  # Replace with your repository URL
    },

)

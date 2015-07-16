from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()
with open('CHANGELOG.rst') as f:
    changelog = f.read()

setup(
    name='pawesome',
    description='Example demonstration of devpi and setuptools_scm',
    long_description=readme + '\n\n' + changelog,
    packages=find_packages(exclude=['tests']),
    use_scm_version=True,
    setup_requires=['setuptools_scm', 'sphinx'],
    url='https://github.com/StephanErb/pawesome',
    author='Stephan Erb',
    author_email='stephan.erb@blue-yonder.com',
)

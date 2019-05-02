from setuptools import setup
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

def required(requirements_file):
    """ Read requirements file and remove comments and empty lines. """
    with open(os.path.join(BASEDIR, requirements_file), 'r') as f:
        requirements = f.read().splitlines()
        return [pkg for pkg in requirements
                if pkg.strip() and not pkg.startswith("#")]


setup(
    name='ResponsiveVoice',
    version='0.2.2',
    packages=['responsive_voice'],
    url='https://github.com/JarbasAl/py_responsivevoice',
    install_requires=required('requirements.txt'),
    license='MIT',
    author='jarbasAI',
    author_email='jarbasai@mailfence.com',
    description='unofficial python wrapper for responsive voice'
)

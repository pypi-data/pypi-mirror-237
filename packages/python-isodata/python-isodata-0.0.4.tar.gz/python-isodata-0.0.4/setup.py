from setuptools import setup

setup(
    name='python-isodata',
    version='0.0.4',
    packages=['src'],
    url='https://github.com/CaffeineLab/isodata',
    license='GNU General Public License v3.0',
    author='Glenn',
    author_email='glenn@caffeinelab.com',
    description='Energy Market downloading tools',
    install_requires=[
        'loguru',
        'python-dateutil',
        'requests'
    ]
)

from setuptools import setup, find_packages

setup(
    name='Glog',
    version='1',
    packages=find_packages(),
    install_requires=[
        'psutil'
    ],
    author='Jonatan Gani',
    author_email='JonatanGani@Protonmail.com',
    description='Complete logging on separate process'
)

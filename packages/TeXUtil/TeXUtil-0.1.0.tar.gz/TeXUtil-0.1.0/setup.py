from setuptools import setup, find_packages

setup(
    name='TeXUtil',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'txu = texutil.scripts.txu:cli'
        ]
    },
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)

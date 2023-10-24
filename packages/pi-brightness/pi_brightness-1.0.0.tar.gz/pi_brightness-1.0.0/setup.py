from setuptools import setup

setup(
    name='pi_brightness',
    version='1.0.0',
    description='Controls Raspberry Pi screen brightness (or other Linux devices)',
    author='Joseph McMahon',
    packages=['module'],
    install_requires=[
        'os',
        'enum',
        'subprocess',
    ],
)
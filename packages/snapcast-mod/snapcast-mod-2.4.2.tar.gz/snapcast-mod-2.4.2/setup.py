from setuptools import setup

setup(
    name='snapcast-mod',
    version='2.4.2',
    description='Control Snapcast.',
    url='https://github.com/SantiagoSotoC/python-snapcast/',
    license='MIT',
    author='happyleaves',
    author_email='happyleaves.tfr@gmail.com',
    packages=['snapcast', 'snapcast.control', 'snapcast.client'],
    install_requires=[
        'construct>=2.5.2',
        'packaging',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ]
)

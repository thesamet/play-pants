from setuptools import setup, find_packages

setup(
    name = 'com.actioniq.play',
    version = '0.2.6',
    description = 'Play plugin for Pants',
    url = 'https://github.com/ActionIQ-OSS/play-pants',
    author = 'Nadav Sr. Samet, Alex Moore, Nitay Joffe',
    author_email = 'alex@actioniq.com',
    license = 'Apache License, Version 2.0',
    zip_safe = True,
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    entry_points={
        'pantsbuild.plugin': [
            'build_file_aliases = com.actioniq.play.register:build_file_aliases',
            'register_goals = com.actioniq.play.register:register_goals',
            'global_subsystems = com.actioniq.play.register:global_subsystems'
        ]
    },
    namespace_packages = [
        'com',
        'com.actioniq',
        'com.actioniq.play',
    ],
    packages = find_packages(),
    install_requires = [
        'boto3==1.4.4',
        'pantsbuild.pants>=1.1.0',
        'pyjavaproperties==0.6',
        'six>=1.9.0,<2'
    ],
    package_dir = {
        '': 'src/python'
    },
)

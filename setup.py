from setuptools import setup

setup(**
{   'classifiers': [   'Intended Audience :: Developers',
                       'License :: OSI Approved :: MIT License',
                       'Operating System :: OS Independent',
                       'Programming Language :: Python',
                       'Topic :: Software Development :: Build Tools'],
    'description': 'Play plugin for pants',
    'entry_points': {   'pantsbuild.plugin': [   'build_file_aliases = com.actioniq.play.register:build_file_aliases',
                                                 'register_goals = com.actioniq.play.register:register_goals',
                                                 'global_subsystems = com.actioniq.play.register:global_subsystems']},
    'install_requires': [   'boto3==1.4.4',
                            'pantsbuild.pants>=1.1.0',
                            'pyjavaproperties==0.6',
                            'six>=1.9.0,<2'],
    'license': 'MIT',
    'long_description': 'Play plugin for pants',
    'maintainer': 'Nadav Sr. Samet, Alex Moore, Nitay Joffe',
    'maintainer_email': 'alex@actioniq.com',
    'name': 'com.actioniq.play',
    'namespace_packages': ['com', 'com.actioniq', 'com.actioniq.play'],
    'package_data': {   },
    'package_dir': {   '': 'src/python'},
    'packages': ['com', 'com.actioniq', 'com.actioniq.play'],
    'url': 'https://github.com/ActionIQ-OSS/play-pants',
    'version': '0.2.1',
    'zip_safe': True}
)

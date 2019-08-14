python_library(
  name = 'com.actioniq.play',
  sources = rglobs('*.py'),
  dependencies = [
    '3rdparty/python:boto3',
    '3rdparty/python:pantsbuild.pants',
    '3rdparty/python:pyjavaproperties',
    '3rdparty/python:six',
  ],
  provides = setup_py(
    name = 'com.actioniq.play',
    version = '0.2.1',
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
    namespace_packages=['com', 'com.actioniq'],
    entry_points={
      'pantsbuild.plugin': [
        'build_file_aliases = com.actioniq.play.register:build_file_aliases',
        'register_goals = com.actioniq.play.register:register_goals',
        'global_subsystems = com.actioniq.play.register:global_subsystems']
    },
  )
)

python_library(
  name = 'play_packaged',
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
    namespace_packages=[
      'com',
      'com.actioniq',
      'com.actioniq.play',
      'com.actioniq.play.tasks',
      'com.actioniq.play.tasks.routes_gen',
      'com.actioniq.play.tasks.twirl_gen',
      'com.actioniq.play.targets',
      'com.actioniq.play.targets.play_project',
      'com.actioniq.play.targets.routes_library',
      'com.actioniq.play.targets.twirl_library',
    ],
    entry_points={
      'pantsbuild.plugin': [
        'build_file_aliases = com.actioniq.play.register:build_file_aliases',
        'register_goals = com.actioniq.play.register:register_goals',
        'global_subsystems = com.actioniq.play.register:global_subsystems'
      ]
    },
  )
)

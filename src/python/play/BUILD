python_library(
  name = 'play',
  sources = rglobs('*.py'),
  dependencies = [
    # TODO: copy root install-requires here
  ],
  provides = setup_py(
    name = 'play',
    version = '0.2.1',
    description = 'Play plugin for Pants',
    url = 'https://github.com/ActionIQ/play-pants',
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
    namespace_packages=['play'],
    entry_points={
      'pantsbuild.plugin': [
        'build_file_aliases = play.register:build_file_aliases',
        'register_goals = play.register:register_goals',
        'global_subsystems = play.register:global_subsystems']
    },
  )
)

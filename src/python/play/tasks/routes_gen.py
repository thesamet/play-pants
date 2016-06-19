from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

import os
import re

from pants.backend.codegen.tasks.simple_codegen_task import SimpleCodegenTask
from pants.backend.jvm.targets.jar_dependency import JarDependency
from pants.backend.jvm.targets.java_library import JavaLibrary
from pants.backend.jvm.tasks.nailgun_task import NailgunTask
from pants.base.build_environment import get_buildroot
from pants.base.exceptions import TaskError
from pants.java.distribution.distribution import DistributionLocator

from play.targets.routes_library import RoutesLibrary
from play.targets.play_project import PlayProject


class RoutesGen(SimpleCodegenTask, NailgunTask):
  def __init__(self, *args, **kwargs):
    super(RoutesGen, self).__init__(*args, **kwargs)

  @classmethod
  def register_options(cls, register):
    super(RoutesGen, cls).register_options(register)
    cls.register_jvm_tool(register, 'play-pants-tool',
        classpath=[
          JarDependency(org='com.thesamet', name='play-pants-tool', rev='0.0.6'),
        ])

  def synthetic_target_type(self, target):
    return JavaLibrary

  def is_gentarget(self, target):
    return isinstance(target, (RoutesLibrary, PlayProject))

  def _is_routes_file(self, fname):
      head, tail = os.path.split(fname)
      return tail == 'routes' or tail.endswith('.routes')

  def execute_codegen(self, target, target_workdir):
    if not isinstance(target, (RoutesLibrary, PlayProject)):
      raise TaskError('Invalid target type "{class_type}" (expected RoutesLibrary)'
                      .format(class_type=type(target).__name__))

    classpath = self.tool_classpath('play-pants-tool')
    main = 'playpants.RoutesGen'
    build_root = get_buildroot()

    sources = [os.path.join(build_root, s) for s in target.sources_relative_to_buildroot() if self._is_routes_file(s)]
    routes_imports = target.payload.default_routes_imports + target.payload.routes_imports
    if not sources:
        return
    args = [
      '--sources', ','.join(sources),
      '--generate_reverse_router', str(target.payload.generate_reverse_router),
      '--generate_forward_router', str(target.payload.generate_forward_router),
      '--namespace_reverse_router', str(target.payload.namespace_reverse_router),
      '--target', target_workdir
    ]
    if routes_imports:
      args += ['--routes_imports', ','.join(routes_imports)]

    result = self.runjava(classpath=classpath, main=main, args=args, workunit_name='routes-gen')

    if result != 0:
      raise TaskError('routes-gen ... exited non-zero ({code})'.format(code=result))


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

from play.targets.twirl_library import TwirlLibrary


class TwirlGen(SimpleCodegenTask, NailgunTask):
  def __init__(self, *args, **kwargs):
    super(TwirlGen, self).__init__(*args, **kwargs)

  @classmethod
  def register_options(cls, register):
    super(TwirlGen, cls).register_options(register)
    cls.register_jvm_tool(register, 'play-pants-tool',
        classpath=[
          JarDependency(org='com.thesamet', name='play-pants-tool', rev='0.0.6'),
        ])

  def synthetic_target_type(self, target):
    return JavaLibrary

  def is_gentarget(self, target):
    return isinstance(target, TwirlLibrary)

  def execute_codegen(self, target, target_workdir):
    if not isinstance(target, TwirlLibrary):
      raise TaskError('Invalid target type "{class_type}" (expected TwirlLibrary)'
                      .format(class_type=type(target).__name__))

    classpath = self.tool_classpath('play-pants-tool')
    main = 'playpants.TwirlGen'
    build_root = get_buildroot()

    sources = [os.path.join(build_root, s) for s in target.sources_relative_to_buildroot()]
    source_dir = os.path.join(build_root, target.payload.source_dir)
    template_imports = target.payload.default_template_imports + target.payload.template_imports
    template_imports_mod = [f.replace('%format%', 'html') for f in template_imports]

    args = [
      '--sources', ','.join(sources),
      '--source_dir', source_dir,
      '--template_imports', ','.join(template_imports_mod),
      '--target', target_workdir
    ]

    result = self.runjava(classpath=classpath, main=main, args=args, workunit_name='twirl-gen')

    if result != 0:
      raise TaskError('twirl-gen ... exited non-zero ({code})'.format(code=result))


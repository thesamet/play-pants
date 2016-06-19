from pants.backend.jvm.targets.jar_dependency import JarDependency
from pants.backend.jvm.targets.jvm_target import JvmTarget
from pants.backend.jvm.tasks.jvm_task import JvmTask
from pants.backend.jvm.tasks.jvm_tool_task_mixin import JvmToolTaskMixin
from pants.java.distribution.distribution import DistributionLocator


class PlayDev(JvmToolTaskMixin, JvmTask):
  _RUNNER_MAIN = 'org.pantsbuild.tools.runner.PantsRunner'

  @classmethod
  def register_options(cls, register):
    super(PlayDev, cls).register_options(register)
    register('--main', default='playpants.tool.PlayDev',
             help='The entry point for running play in Dev mode.')

    cls.register_jvm_tool(register, 'play-pants', classpath=[
        JarDependency(org='com.thesamet', name='play-pants-tool', rev='0.0.5'),
    ], main='playpants.tool.PlayDev')

    cls.register_jvm_tool(register, 'pants-runner', classpath=[
        JarDependency(org='org.pantsbuild', name='pants-runner', rev='0.0.1'),
    ], main=PlayDev._RUNNER_MAIN)

  @classmethod
  def select_targets(cls, target):
    return isinstance(target, JvmTarget)

  def execute(self):
      target = self.require_single_root_target()
      classpath = (
          self.tool_classpath('pants-runner') +
          self.tool_classpath('play-pants') +
          self.classpath([target]))

      args = ['--projectPath', '/home/thesamet/Development/play-pants-example',
              '--mainClass', 'play.core.server.DevServerStart']

      DistributionLocator.cached().execute_java(classpath=classpath,
                                                main=PlayDev._RUNNER_MAIN,
                                                jvm_options=self.jvm_options,
                                                args=[self.get_options().main] + args + self.args,
                                                create_synthetic_jar=True)


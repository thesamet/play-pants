from com.actioniq.play.targets.play_project import PlayProject
from com.actioniq.play.targets.routes_library import RoutesLibrary
from com.actioniq.play.targets.twirl_library import TwirlLibrary
from com.actioniq.play.tasks.routes_gen import RoutesGen
from com.actioniq.play.tasks.twirl_gen import TwirlGen
from pants.build_graph.build_file_aliases import BuildFileAliases
from pants.goal.task_registrar import TaskRegistrar as task


def build_file_aliases():
    return BuildFileAliases()
#        targets={
#            'play_project': PlayProject,
#            'twirl_library': TwirlLibrary,
#            'routes_library': RoutesLibrary
#        })


def register_goals():
    task(name='twirl', action=TwirlGen).install('gen')
    task(name='routes', action=RoutesGen).install('gen')

def global_subsystems():
    return set()

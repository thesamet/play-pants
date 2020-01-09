from __future__ import absolute_import


from com.actioniq.play.tasks import routes_gen

def mock():
    """a simple object you can add properties to.
    replace with unittest.mock when this is moved to python3
    """
    return lambda *args, **kwargs: None

def test_routes_gen():
    options = mock()
    options.bootstrap = True
    options.scope = ''
    routes_gen.RoutesGen.register_options(options)

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

from pants.backend.jvm.targets.jvm_target import JvmTarget
from pants.base.payload import Payload
from pants.base.payload_field import PrimitiveField


DEFAULT_ROUTES_IMPORTS = [
    'controllers.Assets.Asset',
]


class RoutesLibrary(JvmTarget):
  def __init__(self, payload=None,
               default_routes_imports=None,
               routes_imports=None,
               generate_reverse_router=True,
               generate_forward_router=True,
               namespace_reverse_router=False,
               **kwargs):
    payload = payload or Payload()
    payload.add_fields({
      'routes_imports': PrimitiveField(routes_imports or []),
      'default_routes_imports': PrimitiveField(default_routes_imports or DEFAULT_ROUTES_IMPORTS),
      'generate_reverse_router': PrimitiveField(generate_reverse_router),
      'generate_forward_router': PrimitiveField(generate_forward_router),
      'namespace_reverse_router': PrimitiveField(namespace_reverse_router),
    })
    super(RoutesLibrary, self).__init__(payload=payload, **kwargs)


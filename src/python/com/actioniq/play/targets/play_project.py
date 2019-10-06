from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

from pants.backend.jvm.targets.jvm_target import JvmTarget
from pants.base.payload import Payload
from pants.base.payload_field import PrimitiveField


class PlayProject(JvmTarget):
  def __init__(self, payload=None,
               **kwargs):

    payload = payload or Payload()
    payload.add_fields({
      'routes_imports': PrimitiveField([]),
      'default_routes_imports': PrimitiveField([]),
      'generate_reverse_router': PrimitiveField(False),
      'generate_forward_router': PrimitiveField(True),
      'namespace_reverse_router': PrimitiveField(False),
    })
    super(PlayProject, self).__init__(payload=payload, **kwargs)


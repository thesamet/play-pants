from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

from pants.backend.jvm.targets.jvm_target import JvmTarget
from pants.base.payload import Payload
from pants.base.payload_field import PrimitiveField


COMMON_TEMPLATE_IMPORTS = [
    "models._",
    "controllers._",
    "play.api.i18n._",
    "views.%format%._",
    "play.api.templates.PlayMagic._"
]

JAVA_TEMPLATE_IMPORTS = COMMON_TEMPLATE_IMPORTS + [
    "java.lang._",
    "java.util._",
    "scala.collection.JavaConversions._",
    "scala.collection.JavaConverters._",
    "play.core.j.PlayMagicForJava._",
    "play.mvc._",
    "play.data._",
    "play.api.data.Field",
    "play.mvc.Http.Context.Implicit._",
]

SCALA_TEMPLATE_IMPORTS = COMMON_TEMPLATE_IMPORTS + [
    "play.api.mvc._",
    "play.api.data._",
]

class TwirlLibrary(JvmTarget):
  """A Java library generated from JAXB xsd files."""

  def __init__(self, payload=None, source_dir=None,
               default_template_imports=None,
               template_imports=None,
               **kwargs):
    """
    :param package: java package (com.company.package) in which to generate the output java files.
      If unspecified, Pants guesses it from the file path leading to the schema
      (xsd) file. This guess is accurate only if the .xsd file is in a path like
      ``.../com/company/package/schema.xsd``. Pants looks for packages that start with 'com', 'org',
      or 'net'.
    :param string language: only 'java' is supported. Default: 'java'
    """

    payload = payload or Payload()
    payload.add_fields({
      'source_dir': PrimitiveField(source_dir or ''),
      'default_template_imports': PrimitiveField(default_template_imports or SCALA_TEMPLATE_IMPORTS),
      'template_imports': PrimitiveField(template_imports or [])
    })
    super(TwirlLibrary, self).__init__(payload=payload, **kwargs)

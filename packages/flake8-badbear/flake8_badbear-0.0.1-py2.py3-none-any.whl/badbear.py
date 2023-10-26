from typing import Any
from ast import Subscript, Call
from flake8_plugin_utils import Error, Visitor, Plugin


class BB001(Error):
    # Check pattern E.g. a()[2]
    code = 'BB001'
    message = 'Prone to Error "NoneType" object is not iterable. Check None or list length.'


class BadBearVisitor(Visitor):

    def visit_Subscript(self, node: Subscript) -> Any:
        if isinstance(node, Subscript) and isinstance(node.value, Call):   
            self.error_from_node(BB001, node)        


class BadBearPlugin(Plugin):
    name = 'BadBearPlugin'
    version = '0.0.1'
    visitors = [BadBearVisitor]

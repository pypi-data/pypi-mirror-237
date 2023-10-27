# Generated file; do not edit. See the Rust `schema-gen` crate.

from .prelude import *

from .automatic_execution import AutomaticExecution
from .code_error import CodeError
from .cord import Cord
from .duration import Duration
from .executable import Executable
from .execution_dependant import ExecutionDependant
from .execution_dependency import ExecutionDependency
from .execution_digest import ExecutionDigest
from .execution_required import ExecutionRequired
from .execution_status import ExecutionStatus
from .execution_tag import ExecutionTag
from .timestamp import Timestamp


@dataclass(init=False)
class CodeExecutable(Executable):
    """
    Abstract base type for executable code nodes (e.g. `CodeChunk`).
    """

    type: Literal["CodeExecutable"] = field(default="CodeExecutable", init=False)

    code: Cord
    """The code."""

    programming_language: Optional[str] = None
    """The programming language of the code."""

    def __init__(self, code: Cord, id: Optional[str] = None, auto_exec: Optional[AutomaticExecution] = None, compilation_digest: Optional[ExecutionDigest] = None, execution_digest: Optional[ExecutionDigest] = None, execution_dependencies: Optional[List[ExecutionDependency]] = None, execution_dependants: Optional[List[ExecutionDependant]] = None, execution_tags: Optional[List[ExecutionTag]] = None, execution_count: Optional[int] = None, execution_required: Optional[ExecutionRequired] = None, execution_kernel: Optional[str] = None, execution_status: Optional[ExecutionStatus] = None, execution_ended: Optional[Timestamp] = None, execution_duration: Optional[Duration] = None, errors: Optional[List[CodeError]] = None, programming_language: Optional[str] = None):
        super().__init__(id = id, auto_exec = auto_exec, compilation_digest = compilation_digest, execution_digest = execution_digest, execution_dependencies = execution_dependencies, execution_dependants = execution_dependants, execution_tags = execution_tags, execution_count = execution_count, execution_required = execution_required, execution_kernel = execution_kernel, execution_status = execution_status, execution_ended = execution_ended, execution_duration = execution_duration, errors = errors)
        self.code = code
        self.programming_language = programming_language

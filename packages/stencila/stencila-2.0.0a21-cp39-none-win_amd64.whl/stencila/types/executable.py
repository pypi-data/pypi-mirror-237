# Generated file; do not edit. See the Rust `schema-gen` crate.

from .prelude import *

from .automatic_execution import AutomaticExecution
from .code_error import CodeError
from .duration import Duration
from .entity import Entity
from .execution_dependant import ExecutionDependant
from .execution_dependency import ExecutionDependency
from .execution_digest import ExecutionDigest
from .execution_required import ExecutionRequired
from .execution_status import ExecutionStatus
from .execution_tag import ExecutionTag
from .timestamp import Timestamp


@dataclass(init=False)
class Executable(Entity):
    """
    Abstract base type for executable nodes (e.g. `CodeChunk`, `CodeExpression`, `Call`).
    """

    type: Literal["Executable"] = field(default="Executable", init=False)

    auto_exec: Optional[AutomaticExecution] = None
    """Under which circumstances the code should be automatically executed."""

    compilation_digest: Optional[ExecutionDigest] = None
    """A digest of the content, semantics and dependencies of the node."""

    execution_digest: Optional[ExecutionDigest] = None
    """The `compileDigest` of the node when it was last executed."""

    execution_dependencies: Optional[List[ExecutionDependency]] = None
    """The upstream dependencies of this node."""

    execution_dependants: Optional[List[ExecutionDependant]] = None
    """The downstream dependants of this node."""

    execution_tags: Optional[List[ExecutionTag]] = None
    """Tags in the code which affect its execution."""

    execution_count: Optional[int] = None
    """A count of the number of times that the node has been executed."""

    execution_required: Optional[ExecutionRequired] = None
    """Whether, and why, the code requires execution or re-execution."""

    execution_kernel: Optional[str] = None
    """The id of the kernel that the node was last executed in."""

    execution_status: Optional[ExecutionStatus] = None
    """Status of the most recent, including any current, execution."""

    execution_ended: Optional[Timestamp] = None
    """The timestamp when the last execution ended."""

    execution_duration: Optional[Duration] = None
    """Duration of the last execution."""

    errors: Optional[List[CodeError]] = None
    """Errors when compiling (e.g. syntax errors) or executing the node."""

    def __init__(self, id: Optional[str] = None, auto_exec: Optional[AutomaticExecution] = None, compilation_digest: Optional[ExecutionDigest] = None, execution_digest: Optional[ExecutionDigest] = None, execution_dependencies: Optional[List[ExecutionDependency]] = None, execution_dependants: Optional[List[ExecutionDependant]] = None, execution_tags: Optional[List[ExecutionTag]] = None, execution_count: Optional[int] = None, execution_required: Optional[ExecutionRequired] = None, execution_kernel: Optional[str] = None, execution_status: Optional[ExecutionStatus] = None, execution_ended: Optional[Timestamp] = None, execution_duration: Optional[Duration] = None, errors: Optional[List[CodeError]] = None):
        super().__init__(id = id)
        self.auto_exec = auto_exec
        self.compilation_digest = compilation_digest
        self.execution_digest = execution_digest
        self.execution_dependencies = execution_dependencies
        self.execution_dependants = execution_dependants
        self.execution_tags = execution_tags
        self.execution_count = execution_count
        self.execution_required = execution_required
        self.execution_kernel = execution_kernel
        self.execution_status = execution_status
        self.execution_ended = execution_ended
        self.execution_duration = execution_duration
        self.errors = errors

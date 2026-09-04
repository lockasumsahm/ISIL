from dataclasses import dataclass
from enum import Enum


class Permission(str, Enum):
    READ = "read"
    WRITE = "write"
    ADMIN = "admin"


@dataclass(frozen=True)
class AuthorizationContext:
    user_id: str
    organization_id: str
    workspace_id: str | None = None
    project_id: str | None = None


class AuthorizationError(Exception):
    pass


def authorize(
    context: AuthorizationContext,
    permission: Permission,
    *,
    resource_owner_id: str | None = None,
) -> None:
    """
    Central authorization boundary.

    This is intentionally conservative until the persistent
    policy model is implemented.
    """
    if not context.user_id:
        raise AuthorizationError("Missing user identity")

    if resource_owner_id is not None and resource_owner_id != context.user_id:
        raise AuthorizationError("Resource access denied")

    if permission not in Permission:
        raise AuthorizationError("Unknown permission")

import uuid
from typing import Dict, Str  # noqa

# Could be an internal domain or an HTTP API client - we don't care!
from src.authors.apis import AuthorAPI


# plain example
def update_author_name(*, author_name: Str, author_guid: uuid.UUID) -> None:
    AuthorAPI.update_author_name(
        guid=author_guid,
        name=author_name,
    )


# class example
class AuthorInterface:
    @staticmethod
    def get_author(*, guid: uuid.UUID) -> Dict:
        return AuthorAPI.get(guid=guid)

    @staticmethod
    def update_author_name(
        *,
        author_name: Str,
        author_guid: uuid.UUID,
    ) -> None:
        AuthorAPI.update_author_name(
            guid=author_guid,
            name=author_name,
        )

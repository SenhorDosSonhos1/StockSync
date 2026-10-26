"""setup_inicial

Revision ID: f8d2de65bf53
Revises: 
Create Date: 2026-10-26 16:54:06.304839

"""  
from typing import Sequence, Union

# revision identifiers, used by Alembic.
revision: str = 'f8d2de65bf53'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

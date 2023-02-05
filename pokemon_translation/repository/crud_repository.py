"""リポジトリのインターフェース
"""
from typing import Generic, TypeVar, Optional
from abc import abstractmethod

T = TypeVar("T")


class CrudRepository(Generic[T]):
    """CRUD操作を実行するリポジトリ

    Args:
        Generic (_type_): エンティティのタイプ
    """

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[T]:
        """IDからデータを取得します

        Args:
            id (str): ID

        Returns:
            T: 取得したデータ
        """
        pass

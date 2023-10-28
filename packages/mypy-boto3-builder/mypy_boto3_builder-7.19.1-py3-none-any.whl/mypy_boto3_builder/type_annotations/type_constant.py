"""
Wrapper for constant like `False` or `"test"`.
"""

from typing import TypeVar

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation

_R = TypeVar("_R", bound="TypeConstant")


class TypeConstant(FakeAnnotation):
    """
    Wrapper for constant like `False` or `"test"`.

    Arguments:
        value -- Constant value.
    """

    def __init__(self, value: object) -> None:
        self.value: object = value

    def render(self, parent_name: str = "") -> str:
        """
        Render type annotation to a valid Python code for local usage.

        Returns:
            A string with a valid type annotation.
        """
        if self.value is Ellipsis:
            return "..."

        return repr(self.value)

    def copy(self: _R) -> _R:
        """
        Create a copy of type annotation wrapper.
        """
        return self.__class__(self.value)

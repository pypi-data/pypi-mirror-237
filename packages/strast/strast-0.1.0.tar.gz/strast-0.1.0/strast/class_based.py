from . import c


class Strast:
    """
    A class-based interface to the `strast.core.strast` function, allowing for persistent default configurations.

    This class provides a way to create instances of `Strast` with specific default behaviors,
    such as type-checking, AST enforcement, automatic type detection, and ensuring the input is
    strictly a string. Once an instance is configured, its `transform` method or direct call
    can be used to process values with the predefined settings.

    Attributes:
        default_only_types (type or Any): Default types for the result.
        default_grab_types (bool or None): Default setting for automatic type deduction.
        default_force_ast (bool): Default setting for enforcing AST representation.
        default_force_str (bool): Default setting for ensuring input is a string.

    Methods:
        transform(val, *only_types, grab_types=None, force_ast=None, force_str=None):
            Transforms the input value based on the instance's configurations and provided overrides.

        __call__(*only_types, grab_types=None, force_ast=None, force_str=None):
            Alias for the transform method, allowing the instance to be called directly.

    Usage:
        >>> import strast
        >>> converter = strast.S(int, default_force_str=True)
        >>> converter.transform("123")  # Uses default settings from the instance
        123

        >>> converter("123", float)  # Overrides the default settings
        ValueError: Expected result type to be among (<class 'float'>,), but got <class 'int'>.
    """

    def __init__(
        self,
        *default_only_types,
        default_grab_types=None,
        default_force_ast=False,
        default_force_str=False
    ):
        self.default_only_types = default_only_types
        self.default_grab_types = default_grab_types
        self.default_force_ast = default_force_ast
        self.default_force_str = default_force_str

    def transform(
        self, val, *only_types, grab_types=None, force_ast=None, force_str=None
    ):
        if grab_types is None:
            grab_types = self.default_grab_types
        if force_ast is None:
            force_ast = self.default_force_ast
        if force_str is None:
            force_str = self.default_force_str
        if not only_types:
            only_types = self.default_only_types

        return c(
            val,
            *only_types,
            grab_types=grab_types,
            force_ast=force_ast,
            force_str=force_str
        )

    def __call__(self, *only_types, grab_types=None, force_ast=None, force_str=None):
        return self.transform(
            *only_types, grab_types=grab_types, force_ast=force_ast, force_str=force_str
        )

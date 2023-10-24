from . import c


def strast(
    *default_only_types,
    default_grab_types=None,
    default_force_ast=False,
    default_force_str=False
):
    """
    Factory function to create a configured `strast.core.strast` function with specific default behaviors.

    This factory allows for pre-configuring the `strast.core.strast` function with specific default parameters,
    such as type-checking (`default_only_types`), AST enforcement (`default_force_ast`),
    automatic type detection (`default_grab_types`), and ensuring the input is strictly a string (`default_force_str`).

    Args:
        *default_only_types (type or Any): Default types for the result when using the generated function.
        default_grab_types (bool or None, optional): Default setting for automatic type deduction.
        default_force_ast (bool, optional): Default setting for enforcing AST representation.
        default_force_str (bool, optional): Default setting for ensuring input is a string.

    Returns:
        function: A `strast` function pre-configured with the provided default settings.

    Usage:
        >>> import strast
        >>> custom_strast = strast.f(int, default_force_str=True)
        >>> custom_strast("123")  # Uses default settings from the factory
        123

        >>> custom_strast("123", float)  # Overrides the default settings
        ValueError: Expected result type to be among (<class 'float'>,), but got <class 'int'>.
    """

    def strast_closure(
        val, *only_types, grab_types=None, force_ast=False, force_str=False
    ):
        if grab_types is None:
            grab_types = default_grab_types
        if force_ast is None:
            force_ast = default_force_ast
        if force_str is None:
            force_str = default_force_str
        if not only_types:
            only_types = default_only_types

        return c(
            val,
            *only_types,
            grab_types=grab_types,
            force_ast=force_ast,
            force_str=force_str
        )

    return strast_closure

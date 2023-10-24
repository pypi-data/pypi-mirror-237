import ast


def strast(val, *only_types, grab_types=None, force_ast=False, force_str=False):
    """
    Transforms a string representation of a Python literal into the corresponding Python object.
    Additional parameters offer control over the transformation, such as type checking (`only_types`),
    enforcement of AST representation (`force_ast`), automatic type detection (`grab_types`),
    and ensuring the input is strictly a string (`force_str`).

    Args:
        val (str or Any): A string representation of a Python literal or any object.
                          Must be a string if `force_str` is set to True.
        *only_types (type or None): Expected types for the result. Behavior varies based on `grab_types` and the number of arguments:
            - Type checking occurs post-transformation, and `val` passes if its type is among `only_types`.
            - If no arguments are passed: No type checking is performed.
            - If `grab_types` is False: Only specified types are allowed.
            - If `grab_types` is True: Types are auto-detected from the passed values.
            - If `grab_types` is None: Values can be either types or `None`.
        grab_types (bool or None, optional): Automatically deduces type from input values.
                                             For instance, with input 1, it would infer int type.
                                             Defaults to None.
        force_ast (bool, optional): Enforces that the input is a valid string representation
                                    of a Python literal (from AST). Raises an error otherwise. Defaults to False.
        force_str (bool, optional): Ensures that the input is a string. Raises an error otherwise.
                                    Defaults to False.

    Raises:
        TypeError: If there's a mismatch between input types and expected types based on parameters.
        ValueError: If the transformed result doesn't match the expected types.

    Returns:
        Any: The transformed Python object or the original input, depending on the parameters.

    Examples:
        # Basic usage
        >>> import strast
        >>> strast.c("123")
        123

        # With type checking
        >>> strast.c("123", int)
        123

        # Raises error for type mismatch
        >>> strast.c("123", str)
        ValueError: Expected result type to be among (<class 'str'>,), but got <class 'int'>.

        # With automatic type detection
        >>> strast.c("123", 1, grab_types=True)
        123

        # AST enforcement
        >>> strast.c("hello", str, force_ast=True)
        Raises: ValueError: malformed node or string: <_ast.Name object at ...> from ast.literal_eval
        >>> strast.c("'hello'", str, force_ast=True)
        'hello'

        # String input enforcement
        >>> strast.c(123, force_str=True)
        TypeError: Expected 'val' to be a string, but got <class 'int'>.

    """

    assert (
        (isinstance(grab_types, bool) or grab_types is None)
        and isinstance(force_ast, bool)
        and isinstance(force_str, bool)
    )
    if force_str and not isinstance(val, str):
        raise TypeError(
            f"Expected 'val' to be a string, but got {val} of type {type(val)}."
        )

    only_types = list(only_types)
    for i, t in enumerate(only_types):
        if not isinstance(t, type):
            if grab_types:
                only_types[i] = type(t)
            elif grab_types is None:
                if t is None:
                    only_types[i] = type(t)
                else:
                    raise TypeError(
                        f"Expected 'only_types' values to be types or None, but found {t}."
                    )
            else:
                raise TypeError(
                    f"Expected 'only_types' values to be types, but found {t}"
                )
        only_types = tuple(only_types)

    try:
        return_val = ast.literal_eval(val)
    except Exception as e:
        if force_ast:
            raise e
        return_val = val
    if not only_types:
        return return_val
    elif isinstance(return_val, only_types):
        return return_val
    else:
        raise ValueError(
            f"Expected result type to be among {only_types}, but got {return_val} of type {type(return_val)}."
        )

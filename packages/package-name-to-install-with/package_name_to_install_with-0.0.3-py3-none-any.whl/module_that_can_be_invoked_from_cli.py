"""Calculate arithmetic expressions from command line."""
import argparse
import sys
import typing

import pydantic

import package_name_to_import_with


@pydantic.validate_call(validate_return=True)
def capture_user_inputs() -> dict[str, typing.Any]:
    """Capture user inputs for arithmetic expression.

    Returns
    -------
    dict[str, typing.Any]
        captured user inputs
    """
    parser = argparse.ArgumentParser(description="calculator for console", add_help=True)

    parser.add_argument("first_number", help="first number")
    parser.add_argument("operator", help="arithmetic operator")
    parser.add_argument("second_number", help="second number")

    parsed_arguments, _ = parser.parse_known_args()

    return vars(parsed_arguments)


@pydantic.validate_call(validate_return=True)
def console_calculator() -> None:
    """Calculate arithmetic expressions."""
    user_inputs = capture_user_inputs()

    try:
        operation_result = package_name_to_import_with.calculate_results(
            user_inputs["first_number"], user_inputs["operator"], user_inputs["second_number"]
        )
    except Exception as error:  # noqa: BLE001  # pylint: disable=broad-except
        sys.stderr.write(f"Error: {error}")
    else:
        sys.stdout.write(f"Result = {operation_result}")


if __name__ == "__main__":
    console_calculator()

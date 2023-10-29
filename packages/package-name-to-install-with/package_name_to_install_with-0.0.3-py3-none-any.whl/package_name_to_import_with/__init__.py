"""Expose selected package contents."""
from .calculator_sub_package import calculate_results
from .data_using_module import METADATA
from .garbage_collection_module import define_garbage_collection_decorator

__all__ = ["calculate_results", "define_garbage_collection_decorator"]
__version__: str = METADATA.Version

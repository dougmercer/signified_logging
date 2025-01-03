from __future__ import annotations

import logging
from typing import Any

from signified import Variable
from signified.plugin import hookimpl, pm


class ReactiveLogger:
    """A logger plugin for tracking reactive value lifecycle."""

    def __init__(self, logger: Any | None = None):
        """Initialize with optional logger, defaulting to standard logging."""
        if logger is None:
            _logger = logging.getLogger(__name__)
            handler = logging.StreamHandler()
            formatter = logging.Formatter("%(message)s")
            handler.setFormatter(formatter)
            _logger.addHandler(handler)
            _logger.setLevel(logging.INFO)
        else:
            _logger = logger
        self.logger = _logger

    @hookimpl
    def created(self, value: Variable[Any, Any]) -> None:
        """Log when a reactive value is created.

        Args:
            value: The created reactive value
        """
        self.logger.info(f"Created {self._name(value)} with value: {value.value}")

    @hookimpl
    def updated(self, value: Variable[Any, Any]) -> None:
        """Log when a reactive value is updated.

        Args:
            value: The updated reactive value
        """
        self.logger.info(f"Updated {self._name(value)} to value: {value.value}")

    @hookimpl
    def named(self, value: Variable[Any, Any]) -> None:
        """Log when a reactive value is named.

        Args:
            value: The reactive value that was assigned a name.
        """
        self.logger.info(f"Named {type(value).__name__}(id={id(value)}) as {self._name(value)}")

    @staticmethod
    def _name(value: Variable[Any, Any]) -> str:
        return value.name if value.name != "" else f"{type(value).__name__}(id={id(value)})"


DEFAULT_LOGGING_PLUGIN = ReactiveLogger()
pm.register(DEFAULT_LOGGING_PLUGIN)

# Signified Logging

[![PyPI - Downloads](https://img.shields.io/pypi/dw/signified_logging)](https://pypi.org/project/signified_logging/)
[![PyPI - Version](https://img.shields.io/pypi/v/signified_logging)](https://pypi.org/project/signified_logging/)
[![Tests Status](https://github.com/dougmercer/signified_logging/actions/workflows/test.yml/badge.svg)](https://github.com/dougmercer/signified_logging/actions/workflows/test.yml?query=branch%3Amain)

---

**Documentation**: [https://dougmercer.github.io/signified_logging](https://dougmercer.github.io/signified_logging)

**Source Code**: [https://github.com/dougmercer/signified_logging](https://github.com/dougmercer/signified_logging)

---

A logging plugin for the Signified reactive programming library. Automatically logs when reactive values are created, updated, or named.

## Installation

```console
pip install signified signified_logging
```

The plugin will be automatically registered when imported.

```python
import signified_logging
...
```

## Basic Usage

The plugin works automatically once imported. Here's a simple example:

```python
import signified_logging
from signified import Signal

# Create and name some signals
x = Signal(1).add_name("x")
y = (x + 2).add_name("y")

# Update values
x.value = 5
```

Output:
```
Created Signal(id=1234) with value: 1
Named Signal(id=1234) as x
Created Computed(id=5678) with value: 3
Named Computed(id=5678) as y
Updated x to value: 5
Updated y to value: 7
```

## Using a Custom Logger

By default, the plugin uses Python's built-in logging module with minimal formatting. To use your own logger, first unregister the default one, then register your custom logger:

```python
from signified_logging import DEFAULT_LOGGING_PLUGIN, ReactiveLogger
from signified.plugin import pm

# Unregister the default logger
pm.unregister(DEFAULT_LOGGING_PLUGIN)

# Configure a custom logger
import logging
custom_logger = logging.getLogger("my_logger")
custom_logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(message)s"))
custom_logger.addHandler(handler)

# Register it
pm.register(ReactiveLogger(custom_logger))
```

### Using Loguru

[Loguru](https://github.com/Delgan/loguru) is a great alternative to the standard logging module. Here's how to use it:

```python
from signified_logging import DEFAULT_LOGGING_PLUGIN, ReactiveLogger
from signified.plugin import pm

# Unregister the default logger first
pm.unregister(DEFAULT_LOGGING_PLUGIN)

# Register loguru
from loguru import logger
pm.register(ReactiveLogger(logger))
```

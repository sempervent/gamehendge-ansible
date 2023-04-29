"""Initialize the playbooks CLI."""
try:
    import click
except ImportError:
    raise ImportError(
        "The 'click' package is required for using the 'cli' module. Please run 'pip install playbooks[cli]'."
    )

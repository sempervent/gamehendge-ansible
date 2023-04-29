"""Initialize the TUI."""
try:
    import textual
except ImportError:
    raise ImportError(
        "The 'textual' package is required for using the 'tui' module. Please run 'pip install playbooks[tui]'."
    )

def total(items):
    """Return the sum of item prices (demo only)."""
    return sum(item.get("price", 0) for item in items)

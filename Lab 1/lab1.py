def generic_hi(name = "world"):
    """Says hello to {name}"""
    return f"Hello, {name}!"


assert generic_hi() == "Hello, world!"
assert generic_hi("Ada") == "Hello, Ada!"
assert generic_hi("CSE2050") == "Hello, CSE2050!"

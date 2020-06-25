import os
from match_pattern import Pattern

# with glob
assert Pattern("*ab").test("this is a long text that ends with ab") is True

# with regex
assert Pattern("re::^.*ab$").test("this is a long text that ends with ab") is True

# multiple glob (or)
assert Pattern("*ab|*kd").test("this is a long text that ends with kd") is True

# multiple types (or)
assert Pattern(["*ab", "*cd", "re::^.*ef$", Pattern("*gh")]).test("this is a long text that ends with gh") is True


# replace
assert Pattern("ab", is_full_match=False).replace("cd", "abcd") == "cdcd"

# format
assert Pattern.format("""{[msg]}""", custom_start_pattern="{[", custom_end_pattern="]}", msg="ok") == "ok"


# Find all test files in the current folder and subfolders.
pattern = Pattern("*_test.py")
src_path = os.path.abspath(os.path.dirname(__file__))

test_files = pattern.scan_path(src_path)

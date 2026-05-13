from pathlib import Path
import re

version_file = Path("analytics/_version.py")
text = version_file.read_text(encoding="utf-8")

match = re.search(r"__version__\s*=\s*['\"](\d+)\.(\d+)\.(\d+)['\"]", text)
if not match:
    raise SystemExit("Could not parse __version__ in analytics/_version.py")

major, minor, _patch = map(int, match.groups())
new_version = f"{major}.{minor + 1}.0"

updated = re.sub(
    r"__version__\s*=\s*['\"]\d+\.\d+\.\d+['\"]",
    f"__version__ = '{new_version}'",
    text,
    count=1,
)

version_file.write_text(updated, encoding="utf-8")
print(f"Bumped version to {new_version}")

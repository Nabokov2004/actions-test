import re, os

PATTERN = r"__version__\s*=\s*['\"]([^'\"]+)['\"]"

def get_version():
    content = open("analytics/_version.py").read()
    m = re.search(PATTERN, content)
    if not m:
        raise SystemExit('Could not parse __version__ in analytics/_version.py')
    return f"v{m.group(1)}"

def get_sha():
    sha = os.environ.get('MERGE_COMMIT_SHA')
    if not sha:
        raise SystemExit('MERGE_COMMIT_SHA environment variable not set')
    return sha

def set_output(key, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
        f.write(f"{key}={value}\n")

if __name__ == '__main__':
    tag = get_version()
    sha = get_sha()
    print(f"New tag: {tag} → {sha}")
    set_output("new_tag", tag)
    set_output("full_sha", sha)

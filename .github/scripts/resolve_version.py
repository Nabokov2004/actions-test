import re, sys, subprocess, os

def get_version():
    content = open("analytics/_version.py").read()
    m = re.search(r"__version__\s*=\s*['\"]([^'\"]+)['\"]", content)
    if not m:
        sys.exit("Could not find __version__ in analytics/_version.py")
    return f"v{m.group(1)}"

def get_merge_sha():
    # Prefer the env var GitHub sets, fall back to HEAD
    return os.environ.get("MERGE_COMMIT_SHA") or \
           subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()

def set_output(key, value):
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write(f"{key}={value}\n")

if __name__ == "__main__":
    tag = get_version()
    sha = get_merge_sha()
    print(f"New tag: {tag} → {sha}")
    set_output("new_tag", tag)
    set_output("full_sha", sha)

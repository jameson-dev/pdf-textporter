import importlib.metadata
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
requirements_file = os.path.join(parent_dir, 'requirements.txt')


def load_requirements(filename=requirements_file):
    with open(filename, 'r') as file:
        requirements = [line.strip() for line in file if line.strip() and not line.startswith('#')]
    return requirements


def check_modules(requirements):
    missing_modules = []
    for req in requirements:
        package, _, version = req.partition('==')
        try:
            installed_version = importlib.metadata.version(package)
            if installed_version != version:
                missing_modules.append(req)
        except importlib.metadata.PackageNotFoundError:
            missing_modules.append(req)
    return missing_modules

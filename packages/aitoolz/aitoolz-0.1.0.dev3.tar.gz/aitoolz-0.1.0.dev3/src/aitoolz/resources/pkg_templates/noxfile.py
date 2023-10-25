"""Developer task automation."""
import nox

PYTHON = ["3.10"]


@nox.session(python=PYTHON)
def run_tests(session: nox.Session):
    """Run unit tests."""
    session.install(".[dev]")
    pytest_args = session.posargs if session.posargs else []
    session.run("pytest", "-s", *pytest_args)


@nox.session(python=PYTHON, reuse_venv=True)
def format_code(session: nox.Session):
    """Lint code and re-format where necessary."""
    session.install(".[dev]")
    session.run("black", "--config=pyproject.toml", ".")
    session.run("ruff", "check", ".", "--config=pyproject.toml", "--fix")


@nox.session(python=PYTHON, reuse_venv=True)
def check_code_formatting(session: nox.Session):
    """Check code for formatting errors."""
    session.install(".[dev]")
    session.run("black", "--config=pyproject.toml", "--check", ".")
    session.run("ruff", "check", ".", "--config=pyproject.toml")


@nox.session(python=PYTHON, reuse_venv=True)
def check_types(session: nox.Session):
    """Run static type checking."""
    session.install(".[dev]")
    session.run("mypy", "src", "tests", "noxfile.py")

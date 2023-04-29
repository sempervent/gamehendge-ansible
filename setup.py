"""An ansible automation system in python."""
from pathlib import Path
from setuptools import setup, find_packages

HERE = Path(__file__).parent
ENC = 'utf-8'

README = (HERE / 'README.md').read_text(encoding=ENC)

setup(
    name="playbooks",
    author="Joshua N. Grant",
    author_email="jgrant@live.com",
    description="Ansible playbooks generator for configuring servers",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sempervent/gamehendge-ansible",
    packages=find_packages(exclude=["tests"]),
    package_data={
        "playbooks": [
            "templates/*.j2",
            "examples/*.yaml",
        ]
    },
    install_requries=[
        "jinja2",
        "pydantic",
    ],
    extras_requries={
        "cli": ["click"],
        "tui": ["textual"],
        "dev": [
            "pytest",
            "black",
            "flake8",
            "pylint",
            "mypy",
            "pipenv",
            "sphinx",
            "pytest-cov",
        ],
    },
    python_requires=">=3.9"
)
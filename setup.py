from setuptools import setup

setup(
    name="task-cli",
    version="1.0",
    packages=["taskcli"],
    entry_points={
        "console_scripts": ["task-cli = taskcli.__main__:main"]
    },
    description="A CLI task tracker written in Python",
    author="Joseph Emmanuel Tamayo",
    install_requires=[
        "tabulate >=0.10",
    ],
)
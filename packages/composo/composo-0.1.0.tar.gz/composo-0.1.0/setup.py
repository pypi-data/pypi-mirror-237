from setuptools import setup

setup(
    name="composo",
    version="0.1.0",
    description="Composo Python Package",
    author="Luke Markham",
    author_email="luke@composo.ai",
    packages=["composo"],
    install_requires=[
        "requests>=2.25.1",
        "colorama>=0.4.4",
    ],
    python_requires=">=3.8",
)

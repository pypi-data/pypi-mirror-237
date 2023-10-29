from setuptools import setup, Extension
from Cython.Build import cythonize


def readme():
    with open("README.md") as f:
        return f.read()


ext_modules = [
    Extension(
        "",
        sources=["webp_support/webp_support.pyx", "webp_support/webp_support_c.c"],
        extra_compile_args=["-O3"],
        extra_link_args=["-O3"],
    ),
]

setup(
    name="webp_support",
    ext_modules=cythonize(
        ext_modules,
        language_level=3,
        compiler_directives={
            "language_level": 3,
            "boundscheck": False,
            "wraparound": False,
        },
    ),
    package_data={
        "": [
            "webp_support/webp_support.pyi",
            "webp_support/webp_support.pyx",
            "webp_support/webp_support_c.c",
            "webp_support/webp_support_c.h",
            "webp_support/webp_support.pxd",
        ]
    },
    include_package_data=True,
    author="bymoye",
    author_email="s3moye@gmail.com",
    version="0.2.8",
    url="https://github.com/bymoye/webp_support",
    description="A Quickly determine whether Webp is supported from UserAgent.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Cython",
        "Programming Language :: C",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    packages=["webp_support"],
)

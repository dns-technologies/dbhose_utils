from setuptools import (
    Extension,
    setup,
)
from Cython.Build import cythonize


extensions = [
    Extension(
        "dbhose_utils.common",
        ["src/dbhose_utils/common.pyx"],
    ),
]


setup(
    name="dbhose_utils",
    version="0.0.2.5",
    package_dir={"": "src"},
    ext_modules=cythonize(extensions, language_level="3"),
    py_modules=[
        "dbhose_utils.common",
    ],
    packages=["dbhose_utils"],
    package_data={
        "dbhose_utils": [
            "**/*.pyx",
            "**/*.pyi",
            "**/*.pxd",
            "*.pxd",
            "*.pyd",
            "*.md",
            "*.txt",
        ]
    },
    exclude_package_data={
        "": ["*.c"],
        "dbhose_utils.common": ["**/*.c"],
    },
    include_package_data=True,
    setup_requires=["Cython>=0.29.33"],
    zip_safe=False,
)

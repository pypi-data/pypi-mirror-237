import os
import re
import subprocess
import sys
import site
from pathlib import Path
import sysconfig

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext
from distutils.command.install_headers import install_headers as install_headers_orig

with open("VERSION", "r") as f:
    VERSION = f.read().strip()

# Convert distutils Windows platform specifiers to CMake -A arguments
PLAT_TO_CMAKE = {
    "win32": "Win32",
    "win-amd64": "x64",
    "win-arm32": "ARM",
    "win-arm64": "ARM64",
}

### taken from: https://github.com/pybind/cmake_example/blob/master/setup.py
# A CMakeExtension needs a sourcedir instead of a file list.
# The name must be the _single_ output extension from the CMake build.
# If you need multiple extensions, see scikit-build.
class CMakeExtension(Extension):
    def __init__(self, name: str, install_name: str = "", sourcedir: str = "") -> None:
        super().__init__(name, sources=[])
        self.sourcedir = os.fspath(Path(sourcedir).resolve())
        self.install_name = install_name


class CMakeBuild(build_ext):
    def build_extension(self, ext: CMakeExtension) -> None:
        # Must be in this form due to bug in .resolve() only fixed in Python 3.10+
        ext_fullpath = Path.cwd() / self.get_ext_fullpath(ext.name)  # type: ignore[no-untyped-call]
        extdir = ext_fullpath.parent.resolve()

        # Using this requires trailing slash for auto-detection & inclusion of
        # auxiliary "native" libs

        rel_w_debg = int(os.environ.get("RELWITHDEBINFO", 0)) == 1
        debug = int(os.environ.get("DEBUG", 0)) == 1 if self.debug is None else self.debug
        cfg = "RelWithDebInfo" if rel_w_debg else ("Debug" if debug else "Release")

        # CMake lets you override the generator - we need to check this.
        # Can be set with Conda-Build, for example.
        cmake_generator = os.environ.get("CMAKE_GENERATOR", "")

        # Set Python_EXECUTABLE instead if you use PYBIND11_FINDPYTHON
        # EXAMPLE_VERSION_INFO shows you how to pass a value into the C++ code
        # from Python.
        cmake_args = [
            f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}{os.sep}",
            f"-DPython_EXECUTABLE={sys.executable}",
            f"-DCMAKE_BUILD_TYPE={cfg}",  # not used on MSVC, but no harm
            f"-DPython_LIBRARY={sysconfig.get_config_var('LIBDIR')}",
            f"-DPython_INCLUDE_DIR={sysconfig.get_path('include')}",
            f"-DLIB_SPS_VERSION={VERSION}",
        ]

        for arg_PRE in ["DIMENSIONS_", "ORTHOTOPE_", "STORAGE_",]:
            for arg_POST in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]:
                arg_name = arg_PRE + arg_POST
                if "SPS_" + arg_name in os.environ:
                    cmake_args.append("-D" + arg_name + "=" + os.environ["SPS_" + arg_name])
        if "SPS_WITH_STXXL" in os.environ:
            cmake_args.append("-DWITH_STXXL =" + os.environ["SPS_WITH_STXXL"])
        if "SPS_UNROLL_FOR_ALL_COMBINATIONS" in os.environ:
            cmake_args.append("-DUNROLL_FOR_ALL_COMBINATIONS =" + os.environ["SPS_UNROLL_FOR_ALL_COMBINATIONS"])

        build_args = []
        # Adding CMake arguments set as environment variable
        # (needed e.g. to build for ARM OSx on conda-forge)
        if "CMAKE_ARGS" in os.environ:
            cmake_args += [item for item in os.environ["CMAKE_ARGS"].split(" ") if item]

        if self.compiler.compiler_type != "msvc":
            # Using Ninja-build since it a) is available as a wheel and b)
            # multithreads automatically. MSVC would require all variables be
            # exported for Ninja to pick it up, which is a little tricky to do.
            # Users can override the generator with CMAKE_GENERATOR in CMake
            # 3.15+.
            if not cmake_generator or cmake_generator == "Ninja":
                try:
                    import ninja  # noqa: F401

                    ninja_executable_path = Path(ninja.BIN_DIR) / "ninja"
                    cmake_args += [
                        "-GNinja",
                        f"-DCMAKE_MAKE_PROGRAM:FILEPATH={ninja_executable_path}",
                    ]
                except ImportError:
                    pass

        else:

            # Single config generators are handled "normally"
            single_config = any(x in cmake_generator for x in {"NMake", "Ninja"})

            # CMake allows an arch-in-generator style for backward compatibility
            contains_arch = any(x in cmake_generator for x in {"ARM", "Win64"})

            # Specify the arch if using MSVC generator, but only if it doesn't
            # contain a backward-compatibility arch spec already in the
            # generator name.
            if not single_config and not contains_arch:
                cmake_args += ["-A", PLAT_TO_CMAKE[self.plat_name]]

            # Multi-config generators have a different way to specify configs
            if not single_config:
                cmake_args += [
                    f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{cfg.upper()}={extdir}"
                ]
                build_args += ["--config", cfg]

        if sys.platform.startswith("darwin"):
            # Cross-compile support for macOS - respect ARCHFLAGS if set
            archs = re.findall(r"-arch (\S+)", os.environ.get("ARCHFLAGS", ""))
            if archs:
                cmake_args += ["-DCMAKE_OSX_ARCHITECTURES={}".format(";".join(archs))]

        # Set CMAKE_BUILD_PARALLEL_LEVEL to control the parallel build level
        # across all generators.
        if "CMAKE_BUILD_PARALLEL_LEVEL" not in os.environ:
            # self.parallel is a Python 3 only way to set parallel jobs by hand
            # using -j in the build_ext call, not supported by pip or PyPA-build.
            if hasattr(self, "parallel") and self.parallel:
                # CMake 3.12+ only.
                build_args += [f"-j{self.parallel}"]

        build_temp = Path(self.build_temp) / ext.name
        if not build_temp.exists():
            build_temp.mkdir(parents=True)

        subprocess.run(
            ["cmake", ext.sourcedir] + cmake_args, cwd=build_temp, check=True
        )
        subprocess.run(
            ["cmake", "--build", "."] + build_args, cwd=build_temp, check=True
        )
        for install_name in ext.install_name:
            subprocess.run(
                ["cmake", "--install", ".", "--prefix", os.path.join(site.getsitepackages()[0], install_name)], 
                cwd=build_temp, check=True
            )


setup(
    name="libsps",
    version=VERSION,
    author='Markus Schmidt',
    license='MIT',
    url='https://github.com/Siegel-Lab/libSps',
    description="O(1) region count queries using sparse prefix sums",
    long_description="""
libSps is a versatile C++ library designed for efficiently analyzing n-dimensional data. Specifically, it implements constant-time hyperrectangle count queries using a sparse prefix sum index. libSps is available as a header-only library for C++ as well as a Python 3 module.

The library is ideal for processing interactome data (https://en.wikipedia.org/wiki/Chromosome_conformation_capture), and is therefore used in Smoother (https://github.com/Siegel-Lab/BioSmoother).

libSps's documentation is available at https://libsps.readthedocs.io/.
    """,
    ext_modules=[CMakeExtension("sps", ["libsps", "stxxl"])],
    cmdclass={"build_ext": CMakeBuild},
    extras_require={"test": "pytest"},
    zip_safe=False,
    python_requires=">=3.6",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ]
)

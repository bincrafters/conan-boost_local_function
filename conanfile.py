#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/testing")

class BoostLocal_FunctionConan(base.BoostBaseConan):
    name = "boost_local_function"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_local_function"
    lib_short_names = ["local_function"]
    header_only_libs = ["local_function"]
    b2_requires = [
        "boost_config",
        "boost_mpl",
        "boost_preprocessor",
        "boost_scope_exit",
        "boost_type_traits",
        "boost_typeof",
        "boost_utility"
    ]

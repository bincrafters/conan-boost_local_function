from conans import ConanFile, tools, os

class BoostLocal_FunctionConan(ConanFile):
    name = "Boost.Local_Function"
    version = "1.65.1"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-local_function"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["local_function"]
    requires =  "Boost.Config/1.65.1@bincrafters/stable", \
                      "Boost.Mpl/1.65.1@bincrafters/stable", \
                      "Boost.Preprocessor/1.65.1@bincrafters/stable", \
                      "Boost.Scope_Exit/1.65.1@bincrafters/stable", \
                      "Boost.Type_Traits/1.65.1@bincrafters/stable",\
                      "Boost.Typeof/1.65.1@bincrafters/stable",\
                      "Boost.Utility/1.65.1@bincrafters/stable"

                      #config0 mpl5 preprocessor0 scope_exit6 type_traits3 typeof5 utility5

    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()
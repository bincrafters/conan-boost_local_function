from conans import ConanFile, tools, os

class BoostLocal_FunctionConan(ConanFile):
    name = "Boost.Local_Function"
    version = "1.64.0"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-local_function"
    source_url = "https://github.com/boostorg/local_function"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["local_function"]
    requires =  "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Mpl/1.64.0@bincrafters/testing", \
                      "Boost.Preprocessor/1.64.0@bincrafters/testing", \
                      "Boost.Scope_Exit/1.64.0@bincrafters/testing", \
                      "Boost.Type_Traits/1.64.0@bincrafters/testing",\
                      "Boost.Typeof/1.64.0@bincrafters/testing",\
                      "Boost.Utility/1.64.0@bincrafters/testing"

                      #config0 mpl5 preprocessor0 scope_exit6 type_traits3 typeof5 utility5

    def source(self):
        for lib_short_name in self.lib_short_names:
            self.run("git clone --depth=1 --branch=boost-{0} https://github.com/boostorg/{1}.git"
                     .format(self.version, lib_short_name)) 

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()
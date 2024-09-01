from pythonforandroid.recipe import CompiledComponentsPythonRecipe

class MerakiRecipe(CompiledComponentsPythonRecipe):
    version = "0.5.2"
    url = 'https://github.com/Telestai-Project/meraki/archive/{version}.zip'
    site_packages_name = 'meraki'
    depends = ['openssl', 'six', 'setuptools', 'cffi', 'python3', 'shared', 'pycparser', 'libffi']
    call_hostpython_via_targetpython = False
    need_stl_shared = True

    def should_build(self, arch):
        return True


recipe = MerakiRecipe()

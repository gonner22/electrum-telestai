from pythonforandroid.recipe import CythonRecipe

class AlgoModuleRecipe(CythonRecipe):
    version = "1.1.3"
    url = 'https://github.com/electrum-altcoin/AlgoLib/archive/{version}.zip'
    depends = ['setuptools']

recipe = AlgoModuleRecipe()

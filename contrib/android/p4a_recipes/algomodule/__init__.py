from pythonforandroid.recipe import CythonRecipe

class AlgoModuleRecipe(CythonRecipe):
    version = "2.0.0"
    url = 'https://github.com/electrum-altcoin/AlgoLib/archive/{version}.zip'
    depends = ['setuptools']

recipe = AlgoModuleRecipe()

from pythonforandroid.recipe import CythonRecipe

class MerakiRecipe(CythonRecipe):
    version = "0.5.2"
    url = 'https://github.com/Telestai-Project/meraki/archive/{version}.zip'
    depends = ['setuptools']

recipe = MerakiRecipe()

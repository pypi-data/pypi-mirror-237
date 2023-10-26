"""
Very simple test, just check that all modules are importable
"""
from types import ModuleType

from wbBase.application import App
from wbBase.applicationInfo import ApplicationInfo, PluginInfo

appinfo = ApplicationInfo(
    Plugins=[PluginInfo(Name="htmlpanel", Installation="default")]
)


def test_import():
    import wbpHTMLpanel
    assert isinstance(wbpHTMLpanel, ModuleType)


def test_plugin():
    app = App(test=True, info=appinfo)
    assert "htmlpanel" in app.pluginManager
    app.Destroy()



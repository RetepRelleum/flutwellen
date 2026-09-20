# coding=utf-8
"""Lifecycle tests: classFactory -> initGui -> unload."""

from unittest.mock import MagicMock


def test_class_factory_returns_instance(qgis_iface):
    """classFactory returns a plugin instance."""
    from Flutwellen.Flutwellen import Flutwellen
    plugin = Flutwellen(qgis_iface)
    assert plugin is not None


def test_init_gui_registers_action(qgis_iface):
    """initGui registers an action for the plugin."""
    from Flutwellen.Flutwellen import Flutwellen
    plugin = Flutwellen(qgis_iface)
    plugin.initGui()
    assert plugin.actions
    plugin.unload()


def test_unload_removes_action(qgis_iface, monkeypatch):
    """unload removes the toolbar icon via iface."""
    from Flutwellen.Flutwellen import Flutwellen
    remove_toolbar_icon = MagicMock()
    monkeypatch.setattr(qgis_iface, "removeToolBarIcon", remove_toolbar_icon)
    plugin = Flutwellen(qgis_iface)
    plugin.initGui()
    plugin.unload()
    remove_toolbar_icon.assert_called()

cd /home/retep/shell/qgis/pluginTest/flutwellen
source ../venv/bin/activate
pyside6-rcc -o resources.py resources.qrc
deactivate
rm -r -f /home/retep/.local/share/QGIS/QGIS4/profiles/default/python/plugins/flutwellen
cp -r ../flutwellen/ /home/retep/.local/share/QGIS/QGIS4/profiles/default/python/plugins/flutwellen
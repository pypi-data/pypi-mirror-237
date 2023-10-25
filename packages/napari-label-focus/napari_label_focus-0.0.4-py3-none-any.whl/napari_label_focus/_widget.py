import napari.layers
from qtpy.QtWidgets import QComboBox, QGridLayout, QWidget

import napari.layers

from ._table import Table

class TableWidget(QWidget):
    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer

        self.setLayout(QGridLayout())
        self.cb = QComboBox()
        self.layout().addWidget(self.cb, 0, 0)
        self.table = Table(viewer=self.viewer)
        self.layout().addWidget(self.table, 1, 0)

        self.cb.currentTextChanged.connect(self._on_cb_change)

        self.viewer.layers.events.inserted.connect(self._add_rename_event)
        self.viewer.layers.events.inserted.connect(self._on_layer_change)
        self.viewer.layers.events.removed.connect(self._on_layer_change)
        self.viewer.layers.events.removed.connect(self._on_layer_remove)
        self._on_layer_change(None)

    def _add_rename_event(self, e):
        source_layer = e.value
        source_layer.events.name.connect(lambda _: self._on_layer_change(None))
        source_layer.events.set_data.connect(lambda _: self.table.update_content(source_layer))

    def _on_layer_change(self, e):
        self.cb.clear()
        for x in self.viewer.layers:
            if isinstance(x, napari.layers.Labels):
                self.cb.addItem(x.name, x.data)

    def _on_layer_remove(self, e):
        print('Layer removed.')
        self.table.update_content(None)

    def _on_cb_change(self, selection: str):
        selected_layer = None
        for l in self.viewer.layers:
            if l.name == selection:
                selected_layer = l
                break

        if selected_layer is None:
            return

        self.table.update_content(selected_layer)


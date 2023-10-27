#!/usr/bin/env python3

"""
** Interactive window for help to choose the export settings. **
----------------------------------------------------------------
"""

import pathlib

from qtpy import QtWidgets

from cutcutcodec.core.compilation.export.default import suggest_export_params
from cutcutcodec.core.compilation.tree_to_graph import tree_to_graph
from cutcutcodec.core.exceptions import IncompatibleSettings
from cutcutcodec.core.io.write import ContainerOutputFFMPEG
from cutcutcodec.gui.base import CutcutcodecWidget
from cutcutcodec.gui.export.container import ContainerSettings
from cutcutcodec.gui.export.encodec import EncoderSettings
from cutcutcodec.gui.tools import WaitCursor



class WindowsExportSettings(CutcutcodecWidget, QtWidgets.QDialog):
    """
    ** Show the exportation settings. **
    """

    def __init__(self, parent):
        super().__init__(parent)
        self._parent = parent

        with WaitCursor(self.main_window):
            self._container_settings = ContainerSettings(self)
            self._encoders = [
                EncoderSettings(self, stream) for stream in self.app.tree().in_streams
            ]

            self.setWindowTitle("Export settings")

            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(self._container_settings)

            streams_w = QtWidgets.QWidget()
            layout_streams = QtWidgets.QHBoxLayout()
            streams_w.setLayout(layout_streams)
            for i, encoder in enumerate(self._encoders):
                if i:
                    separador = QtWidgets.QFrame()
                    separador.setFrameShape(QtWidgets.QFrame.Shape.VLine)
                    layout_streams.addWidget(separador)
                layout_streams.addWidget(encoder)
            layout.addWidget(streams_w)

            self.init_next(layout)
            self.setLayout(layout)

            self.refresh()

    def export(self):
        """
        ** Complete the job or the next step in the main pipeline. **
        """
        self.accept()
        streams = self.app.tree().in_streams

        # conversion of supplied parameters
        filename = (
            pathlib.Path(self.app.export_settings["parent"]) / self.app.export_settings["stem"]
        )

        indexs = {}
        streams_settings = []
        for stream in streams:
            index = indexs.get(stream.type, -1) + 1
            indexs[stream.type] = index
            streams_settings.append({
                "encodec": self.app.export_settings["encoders"][stream.type][index],
                "options": self.app.export_settings["encoders_settings"][stream.type][index],
            })
            if streams_settings[-1]["encodec"] == "default":
                streams_settings[-1]["encodec"] = (
                    self.app.export_settings["codecs"][stream.type][index]
                )
            if stream.type == "audio":
                streams_settings[-1]["rate"] = self.app.export_settings["rates"]["audio"][index]
            elif stream.type == "video":
                streams_settings[-1]["rate"] = self.app.export_settings["rates"]["video"][index]
                streams_settings[-1]["shape"] = self.app.export_settings["shapes"][index]
            else:
                raise TypeError(f"not yet supported {stream.type}")

        container_settings = {
            "format": self.app.export_settings["muxer"],
            "container_options": self.app.export_settings["muxer_settings"],
        }

        # completes the missing parameters
        try:
            filename, streams_settings, container_settings = suggest_export_params(
                streams,
                filename=filename,
                streams_settings=streams_settings,
                container_settings=container_settings,
            )
        except IncompatibleSettings as err:
            QtWidgets.QMessageBox.warning(None, "Incompatible Parameters", str(err))

        # transmission of the information for next steps
        tree = ContainerOutputFFMPEG(
            streams,
            filename=filename,
            streams_settings=streams_settings,
            container_settings=container_settings,
        )
        self.main_window.output.put_nowait({
            "graph": tree_to_graph(tree),
            "optimize": self.app.export_settings["optimize"],
            "excecute": self.app.export_settings["excecute"],
            "filename": (
                pathlib.Path(self.app.export_settings["parent"]) / self.app.export_settings["stem"]
            )
        })

        # close
        self.main_window.close()

    def init_next(self, layout):
        """
        ** The button for the next stape. **
        """
        def set_optimize(state):
            self.app.export_settings["optimize"] = bool(state)
        def set_excecute(state):
            self.app.export_settings["excecute"] = bool(state)
        separador = QtWidgets.QFrame()
        separador.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        layout.addWidget(separador)
        optimize = QtWidgets.QCheckBox("Optimize the graph.")
        optimize.setChecked(self.app.export_settings["optimize"])
        optimize.stateChanged.connect(set_optimize)
        layout.addWidget(optimize)
        excecute = QtWidgets.QCheckBox("Excecute the generated code.")
        excecute.setChecked(self.app.export_settings["excecute"])
        excecute.stateChanged.connect(set_excecute)
        layout.addWidget(excecute)
        button = QtWidgets.QPushButton("Let's Go!")
        button.clicked.connect(self.export)
        layout.addWidget(button)

    def refresh(self):
        with WaitCursor(self):
            self._container_settings.refresh()
            for enc in self._encoders:
                enc.refresh()

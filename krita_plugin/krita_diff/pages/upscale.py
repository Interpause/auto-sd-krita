from krita import QPushButton, QVBoxLayout, QWidget

from ..script import script
from ..widgets import QCheckBox, QComboBoxLayout, QLabel


# TODO: Become SD Upscale tab.
class UpscaleTabWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(UpscaleTabWidget, self).__init__(*args, **kwargs)

        self.upscaler_layout = QComboBoxLayout(
            script.cfg, "upscaler_list", "upscale_upscaler_name", label="Upscaler:"
        )

        self.downscale_first = QCheckBox(
            script.cfg,
            "upscale_downscale_first",
            "Downscale image x0.5 before upscaling",
        )

        note = QLabel(
            """
NOTE:<br/>
 - txt2img & img2img will use the <em>Quick Config</em> Upscaler when needing to scale up.<br/>
 - Upscaling manually is only useful if the image was resized via Krita.<br/>
 - In the future, SD Upscaling will replace this tab! For now, use the WebUI.
            """
        )
        note.setWordWrap(True)

        self.btn = QPushButton("Start upscaling")

        layout = QVBoxLayout()
        layout.addWidget(note)
        layout.addLayout(self.upscaler_layout)
        layout.addWidget(self.downscale_first)
        layout.addStretch()
        layout.addWidget(self.btn)

        self.setLayout(layout)

    def cfg_init(self):
        self.upscaler_layout.cfg_init()
        self.downscale_first.cfg_init()

    def cfg_connect(self):
        self.upscaler_layout.cfg_connect()
        self.downscale_first.cfg_connect()
        self.btn.released.connect(lambda: script.action_simple_upscale())

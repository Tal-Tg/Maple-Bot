import time
import threading
import winsound
import keyboard as kb
from src.common import config, utils
from datetime import datetime

class Listener():
    DEFAULT_CONFIG = {
        'Start/stop': 'insert',
        'Reload routine': 'f6',
        'Record position': 'f7'
    }
    
    def _init(self):
        config.listener = self

        self.enabled = False
        self.ready = False
        self.block_time = 0
        self.thread = threading.Thread(target=self._main)
        self.thread.daemon = True
        
    def start(self):
        print('\n[~] Started keyboard listener')
        self.thread.start()

    def _main(self):
        self.ready = True
        while True:
            if kb.is_pressed('home'):
                Listener.toggle_enabled()


    @staticmethod
    def recalibrate_minimap():
        config.capture.calibrated = False
        while not config.capture.calibrated:
            time.sleep(0.01)
        
    @staticmethod
    def toggle_enabled():

        # config.bot.rune_active = False

        if not config.enabled:
            Listener.recalibrate_minimap()      # Recalibrate only when being enabled.

        config.enabled = not config.enabled
        utils.print_state()

        if config.enabled:
            winsound.Beep(784, 333)     # G5
        else:
            winsound.Beep(523, 333)     # C5
        time.sleep(0.267)

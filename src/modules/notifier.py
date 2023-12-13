from src.common import config, utils
import time
import os
import cv2
import pygame
import threading
import numpy as np
import keyboard as kb

RUNE_RANGES = (
    ((141, 148, 245), (146, 158, 255)),
)
rune_filtered = utils.filter_color(cv2.imread('assets/rune_template.png'), RUNE_RANGES)
RUNE_TEMPLATE = cv2.cvtColor(rune_filtered, cv2.COLOR_BGR2GRAY)


class Notifier:
    
    def __init__(self):
        
        pygame.mixer.init()
        self.mixer = pygame.mixer.music
        
        self.ready = False
        self.thread = threading.Thread(target=self._main)
        self.thread.daemon = True
        self.rune_alert_delay = 270
        
    def start(self):
        
        print('\n[~] Started notifier')
        self.thread.start()
    
    def _main(self):
        self.ready = True
        rune_start_time = time.time()
        print("notifier...")
        time.sleep(2)
        while True:
            
            frame = config.capture.frame
            height, width, _ = frame.shape
            minimap = config.capture.minimap['minimap']
            
            now = time.time()
            if not config.bot.rune_active:
                filtered = utils.filter_color(minimap, RUNE_RANGES)
                matches = utils.multi_match(filtered, RUNE_TEMPLATE, threshold=0.9)
                rune_start_time = now 
                if matches:
                    abs_rune_pos = (matches[0][0], matches[0][1])
                    config.bot.rune_pos = utils.convert_to_relative(abs_rune_pos, minimap)
                    print(config.bot.rune_pos)
                    config.bot.rune_active = True
            elif now - rune_start_time > self.rune_alert_delay:     # Alert if rune hasn't been solved
                config.bot.rune_active = False
                # self._alert('siren')
            time.sleep(0.01)
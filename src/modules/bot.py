import time
from src.modules.components import Move
from src.common.vkeys import press,key_down,key_up
from src.common import config,detection
import time
from random import random
import threading
import tensorflow as tf
import cv2

arrow_right_data = cv2.CascadeClassifier('cascade.xml')


class Bot():
    
    def __init__(self):
        
        config.bot = self
        self.ready = False
        self.thread = threading.Thread(target=self._main)
        self.thread.daemon = True
        self.command_book = None        
        self.rune_active = False
        self.rune_pos = (0, 0)
        
    def start(self):
        print('\n[~] Started main bot loop')
        self.thread.start()
   
        
    def makingRandomNumberFloat(self):
        numberRandom = random()
        float_version = float(numberRandom)
        return float_version 
    
    
    # def load_model():
    #     model_dir = f'assets/models/rune_model_rnn_filtered_cannied/saved_model'
    #     return tf.saved_model.load(model_dir)
    
    
    
    
    def _main(self):
        self.ready = True
        i=1
        
        # model = self.load_model()
        
        while True:
            # print("boting...")
            if self.rune_active:
                move = Move(config.bot.rune_pos[0],config.bot.rune_pos[1],25)
                move.main()
                time.sleep(2)
                self.solvingRun()
            time.sleep(0.01)
            
            
    def solvingRun(self):
        
        press('space', 2, down_time=0.1)    
        time.sleep(2)
        
        frame = config.capture.frame
        height, width, channels = frame.shape
        cropped = frame[120:height//2, width//4:3*width//4]
        grayscaled_img = cv2.cvtColor(cropped,cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f"2.jpg",grayscaled_img)
        print("solving rune...")
        for _ in range(15):
            try:
                search_arrow_right = arrow_right_data.detectMultiScale(grayscaled_img)
                if search_arrow_right:
                    for (x, y, w,  h) in search_arrow_right:
                        print("right")
                        self.rune_active = False
            except:
                print("An exception occurred")
                

            
            
            # solution = detection.merge_detection(model, frame)
            # if solution:
            #     print(', '.join(solution))
            #     if solution in inferences:
            #         print('Solution found, entering result')
            #         for arrow in solution:
            #             press(arrow, 1, down_time=0.1)
            #             time.sleep(1)
            #         self.rune_active = False
            #         break
            # if i < 3:
            #     move = Move(0.2,0.27,25)
            #     move.main()
            #     print(config.player_pos)
            #     press("alt",1,down_time=0.1)
            #     press("a",3,down_time=0.1)
            #     time.sleep(0.2)
            #     print(config.player_pos)
            #     press("alt",1,down_time=0.1)
            #     press("a",3,down_time=0.1)
            #     move = Move(0.4,0.27,25)
            #     move.main()
            #     print(config.player_pos)
            #     press("alt",1,down_time=0.1)
            #     press("a",3,down_time=0.1)
            #     time.sleep(0.2)
            #     print(config.player_pos)
            #     press("alt",1,down_time=0.1)
            #     press("a",3,down_time=0.1)
            #     move = Move(0.6,0.27,25)
            #     move.main()
            #     print(config.player_pos)
            #     press("alt",1,down_time=0.1)
            #     press("a",3,down_time=0.1)
            #     time.sleep(0.2)
            #     print(config.player_pos)
            #     press("a",3,down_time=0.1)
            #     move = Move(0.8,0.27,25)
            #     move.main()
            #     print(config.player_pos)
            #     time.sleep(0.2)
            #     print(config.player_pos)
            #     press("a",3,down_time=0.1)
            #     i+=1

        # while i<2:
        #     print(config.player_pos) 
        #     move = Move(0.2,0.07,15)
        #     move.main()
        #     config.enabled = False
        #     i+=1
        
        # while True:
        #     i = 1
        #     j = 1 
        #     press("delete", 1, down_time=0.1,up_time=0.1)
        #     time.sleep(0.2)
        #     press("end", 1, down_time=0.1,up_time=0.1)
        #     while i < 4:
        #         time.sleep(0.2)
        #         press("right", 1, down_time=0.2,up_time=0.1)
        #         time.sleep(0.1)
        #         press("alt", 2, down_time=0.1,up_time=0.1)
        #         time.sleep(0.1)
        #         press("a", 1, down_time=0.2,up_time=0.1)
        #         i+=1

                
        #     while j < 4:
        #         time.sleep(0.2)
        #         press("left", 1, down_time=0.2,up_time=0.1)
        #         time.sleep(0.1)
        #         press("alt", 2, down_time=0.1,up_time=0.1)
        #         time.sleep(0.1)
        #         press("a", 1, down_time=0.2,up_time=0.1)
        #         j+=1
                
            # press("right", 1, down_time=self.makingRandomNumberFloat()*2)
            # press("a", 1, down_time=0.1)
            
            # time.sleep(self.makingRandomNumberFloat())
            
            # press("right", 1, down_time=self.makingRandomNumberFloat()*2)
            # press("a", 1, down_time=0.1)
            
            # time.sleep(self.makingRandomNumberFloat())
            
            
            # # turn left for some reason
            # press("left", 1, down_time=0.5)
            # press("a", 1, down_time=0.1)
            
            # time.sleep(self.makingRandomNumberFloat())
            
            # press("x", 1, down_time=0.1)
            
            # time.sleep(self.makingRandomNumberFloat())
            
            # press("right", 1, down_time=self.makingRandomNumberFloat()*2)
            # press("a", 1, down_time=0.1)
            
            # time.sleep(self.makingRandomNumberFloat())
            
            # press("left", 1, down_time=self.makingRandomNumberFloat()*2)
            # press("a", 1, down_time=0.1)
            
            # time.sleep(self.makingRandomNumberFloat())
            
            # press("left", 1, down_time=self.makingRandomNumberFloat()*2)
            # press("a", 1, down_time=0.1)
            
            # time.sleep(self.makingRandomNumberFloat())
            
            # # turn right for some reason
            # press("right", 1, down_time=0.1)
            # press("a", 1, down_time=0.1)
            
            # time.sleep(self.makingRandomNumberFloat())
            
            # press("left", 1, down_time=self.makingRandomNumberFloat()*2)
            # press("a", 1, down_time=0.1)            
            
            
            # press("ctrl", 1, down_time=0.1)
            
            # time.sleep(self.makingRandomNumberFloat())

    


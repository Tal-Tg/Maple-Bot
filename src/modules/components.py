from src.common import utils,config,settings
from src.common.vkeys import key_down,key_up,press
import math
import time

class Move():
    
    def __init__(self,x,y,max_steps):
        self.target = (float(x),float(y))
        self.max_steps = int(max_steps)
        self.prev_direction = ''
        self.enabled = False
        
    def _new_direction(self, new):
        key_down(new)
        if self.prev_direction != new:
            key_up(self.prev_direction)
        self.prev_direction = new
        
    def main(self):
        self.enabled = True
        counter = self.max_steps
        self.prev_direction = ''
        toggle = True
        key = ''
        
        while counter > 1 :
            if toggle:
                d_x = float(self.target[0]) - config.player_pos[0]
                if abs(d_x) > 0.1 / math.sqrt(2):
                    if d_x < 0:
                        key = 'left'
                    else:
                        key = 'right'
                    self._new_direction(key)  
                    press(key,1,down_time=1)  
                counter -= 1                 
            else:
                d_y = float(self.target[1]) - config.player_pos[1]
                if abs(d_y) > settings.move_tolerance / math.sqrt(2):
                    if d_y < 0:
                        key = 'up'
                        key_down(key)
                        press('alt',2,down_time=0.1,up_time=0.1)
                        key_up(key)
                        press('left',1,down_time=0.5,up_time=0.1)
                    else:
                        key = 'down'
                        key_down(key)
                        press('alt',2,down_time=0.1,up_time=0.1)
                        key_up(key)
                        press('left',1,down_time=0.5,up_time=0.1) 
                    self._new_direction(key)
                counter -= 1 
            toggle = not toggle

            
            

            
            
            
        # while counter > 1 : 
        #     if toggle:  
        #         if config.player_pos[0] > float(self.target[0]+0.05) or config.player_pos[0] < float(self.target[0]-0.05) :
        #             d_x = float(self.target[0]) - config.player_pos[0]
        #             if d_x < 0 :
        #                 arrow = 'left'
        #             else:
        #                 arrow = 'right'
        #             self._new_direction(arrow)
        #             press(arrow,1,down_time=0.1)
        #             key_up(arrow)
        #     elif config.player_pos[1] > float(self.target[1]+0.02) or config.player_pos[1] < float(self.target[1]-0.02): 
        #         d_y = float(self.target[1]) - config.player_pos[1]
        #         if d_y < 0 :
        #             arrow = 'up'
        #             key_down(arrow)
        #             press('alt',2,down_time=0.1,up_time=0.1)
        #             key_up(arrow)
        #             press('left',1,down_time=0.1,up_time=0.1)
        #         else:
        #             arrow = 'down'
        #             key_down(arrow)
        #             press('alt',1,down_time=0.1,up_time=0.1)
        #             key_up(arrow)
        #             press('left',1,down_time=0.1,up_time=0.1)
        #         key_up(arrow)
        #     else:  
        #         break
        #     toggle = not toggle
            
                # self._new_direction(arrow)
                # counter-=1

            
            

            
            
            



       
            
            
        # while True :   
        #     if toggle:
        #         if config.player_pos[0] > float(self.target[0]+0.1) or config.player_pos[0] < float(self.target[0]-0.1) :
        #             d_x = float(self.target[0]) - config.player_pos[0]
        #             if d_x < 0 :
        #                 arrow = 'left'
        #             else:
        #                 arrow = 'right'
        #             self._new_direction(arrow)
        #             press(arrow,1,down_time=1,up_time=0.1)
        #             counter-=1
        #         elif config.player_pos[1] > float(self.target[1]+0.05) or config.player_pos[1] < float(self.target[1]-0.05): 
        #             d_y = float(self.target[1]) - config.player_pos[1]
        #             if d_y < 0 :
        #                 arrow = 'up'
        #                 key_down(arrow)
        #                 press('alt',2,down_time=0.1,up_time=0.1)
        #                 key_down(arrow)
        #                 press('left',1,down_time=0.3,up_time=0.1)
        #             else:
        #                 arrow = 'down'
        #                 key_down(arrow)
        #                 press('alt',1,down_time=0.1,up_time=0.1)
        #                 key_down(arrow)
        #                 press('left',1,down_time=0.3,up_time=0.1)
        #             counter-=1
        #             self._new_direction(arrow)
        #             key_down(arrow)
        #         toggle = not toggle
                    
                

                
            
            
            
            # the best one yet
            
            #  if config.player_pos[0] > float(self.target[0]+0.1) or config.player_pos[0] < float(self.target[0]-0.1) or config.player_pos[1] > float(self.target[1]+0.03) or config.player_pos[1] < float(self.target[1]-0.03):
            #     if toggle:
            #         d_x = float(self.target[0]) - config.player_pos[0]
            #         if d_x < 0 :
            #             arrow = 'left'
            #         else:
            #             arrow = 'right'
            #         self._new_direction(arrow)
            #         press(arrow,1,down_time=1,up_time=0.1)
            #         counter-=1
            #     else: 
            #         d_y = float(self.target[1]) - config.player_pos[1]
            #         if d_y < 0 :
            #             arrow = 'up'
            #             key_down(arrow)
            #             press('alt',2,down_time=0.1,up_time=0.1)
            #             key_down(arrow)
            #             press('right',1,down_time=0.1,up_time=0.1)
            #         else:
            #             arrow = 'down'
            #             key_down(arrow)
            #             press('alt',1,down_time=0.1,up_time=0.1)
            #             key_down(arrow)
            #             press('left',1,down_time=0.1,up_time=0.1)
            #         counter-=1
            #         self._new_direction(arrow)
            #         key_down(arrow)
            #     toggle = not toggle
            # else:
            #     break
            
            
            
            # if config.player_pos[0] > float(self.target[0]+0.1) or config.player_pos[0] < float(self.target[0]-0.1):
            #     if toggle:
            #         d_x = float(self.target[0]) - config.player_pos[0]
            #         if d_x < 0 :
            #             arrow = 'left'
            #         else:
            #             arrow = 'right'
            #         self._new_direction(arrow)
            #         press(arrow,1,down_time=1,up_time=0.1)
            #         counter-=1
            #     else: 
            #         d_y = float(self.target[1]) - config.player_pos[1]
            #         if d_y < 0:
            #             arrow = 'up'
            #             key_down(arrow)
            #             press('alt',2,down_time=0.1,up_time=0.1)
            #             key_down(arrow)
            #         else:
            #             arrow = 'down'
            #             key_down(arrow)
            #             press('alt',1,down_time=0.1,up_time=0.1)
            #             key_down(arrow)
            #         counter-=1
            #         self._new_direction(arrow)
            #     toggle = not toggle
            # else:
            #     break
            # if self.prev_direction:
            #     key_up(self.prev_direction)
            
            
        
        
        
        
        # x_error = utils.distance( config.player_pos , self.target)
        # y_error = utils.distance( config.player_pos , self.target)
        # single_x_error = float(config.player_pos[0]) - float(self.target[0])
        
        
            # if self.prev_direction:
            #     key_up(self.prev_direction)
            
         # print(single_x_error)
        # print(config.player_pos)
        
        
            # while self.max_steps < 1:
            #     press("right",1,down_time=0.1,up_time=0.1)
            #     self.max_steps-=1
            #     time.sleep(0.1)
                
        # if single_x_error > 0.1 :
        #     print("hello")
        
        
        
        
            # while self.max_steps < 1:   
            #     press("left",1,down_time=0.1,up_time=0.1)
            #     self.max_steps-=1
            #     time.sleep(0.1)
        
            # arrow = "left"
            # press(arrow,1,down_time=0.1,up_time=0.1)
            # counter-=1
            # time.sleep(0.01)
        
            

        
            


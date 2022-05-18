import math

class Melee:
    def __init__(self, mp = False,
            strike_count=2,
            damage=10,
            hostile = True,
            owner_object = None,
            strike_range=150):
        self.owner = owner_object
        self.mp=mp;
        self.arc=1*math.pi;
        self.strike_range = strike_range # what's a good melee range number? - lets see if we can't make this more adjustable  ## The attack distance for zombies is 100, so at least 150
        self.strikes_used=0;
        self.strikes=strike_count;
        self.damage = damage;


    def get_string(self):

        string = "MELEE:" + str(round(self.pos[0])) + "_" + str(round(self.pos[1])) + "_"+ str(round(self.target_pos[0])) + "_"+ str(round(self.target_pos[1]))
        return string


    def check_for_strike(self,r_click):
        if r_click == True and self.strikes_used < self.strikes: ##FIRE
            return True
        else:
            return False



    def tick(self,screen, r_click):

        pos = tuple(self.owner.get_pos())
        angle = self.owner.get_angle()

        if self.check_for_strike(r_click):
            melee_sound.stop()
            melee_sound.play()
            melee_list.append({"pos" : pos, "angle" : angle, "damage" : self.damage, "distance" : self.strike_distance, "arc" : self.arc})   #BULLET
            self.strikes_used += 1
        if self.strikes_used > 0:
            self.strikes_used -= 0.01
        else:
            self.strikes_used = 0




    def get_remaining_strikes(self):
        return self.__strikes-self._strikes_used


# https://blog.csdn.net/waitan2018/article/details/83930162
"""外星人入侵了宇宙飞船，我们的英雄需要通过各种房间组成的迷宫，打败遇到的外星人，
   这样才能通过救生船回到下面的行星去。这个游戏会跟《Zork》或者《Adventure》类似，
   会用文字输出各种搞笑的死法。游戏会用到一个引擎，带动一张充满房间和场景的地图。
   当玩家进入一个房间，这个房间会显示出自己的描述，告诉引擎下一步应该到哪个房间去。
"""
"""
游戏的内部逻辑
   * Map
      – next_scene
      – opening_scene
   * Engine
      – play
   * Scene
      –enter
      * Death
      * Central	Corridor
      * Laser Weapon Armory
      * The Bridge
      *	Escape Pod
"""
"""
    死亡（Death）：玩家死去的场景。
    中央走廊（Central Corridor）：这是游戏的起点，哥顿人已经在那儿把守着了，
    玩家需要讲一个笑话才能继续。
    激光武器库（Laser Weapon Armory）：在这里英雄会找到一个中子弹，
    在乘坐逃生舱离开飞船时用它把飞船炸掉。这个房间有个数字键盘，英雄需要猜密码组合。
    飞船主控舱（The Bridge）：另一个战斗场景，英雄需要在这里埋炸弹。
    逃生舱（Escape Pod）：英雄逃离的场景，但需要猜对哪艘是好的。
"""




from sys import exit
from random import randint
class Scene(object):
    def enter(self):
        print('This scene is not yet configured.---此场景尚未配置。')
        print('Subclass it and implement enter().---对它进行子类化并实现输入。')
        exit(1)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
        print("e1")

    def play(self):
        current_scene = self.scene_map.opening_scene()
        print("e2.1")
        last_scene = self.scene_map.next_scene('finished')
        print("e2.2")

        while current_scene != last_scene:
            print("e2.3")
            next_scene_name = current_scene.enter()
            print("e2.4")
            current_scene = self.scene_map.next_scene(next_scene_name)
            print("e2.5")

		# be sure to print out the last scene_map
        current_scene.enter()
        print("e2.6")


class Death(Scene):
    def enter(self):
        print("death")


class CentralCorridor(Scene):
    def enter(self):
        print("central_corridor")
        return 'laser_weapon_armory'


class LaserWeaponArmory(Scene):
    def enter(self):
        print("laser_weapon_armory")
        return 'the_bridge'


class TheBridge(Scene):
    def enter(self):
        print("the_bridge")
        return 'escape_pod'


class EscapePod(Scene):
    def enter(self):
        print("escape_pod")
        return 'finished'


class Finished(Scene):
    def enter(self):
        print("YOU WIN!")


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        print("map1")
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        print("map2")
        return val

    def opening_scene(self):
        print("map3")
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

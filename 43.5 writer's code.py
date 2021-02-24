from sys import exit
from random import randint
from textwrap import dedent
#为了写房间描述时使用三引号字符串，引入了dedent函数，它会把字符串开头的空白去掉，如果不用这个函数，使用三引号风格字符串就会失败，因为它们会砸屏幕上缩进，和在Python 代码中一样。


class Scene(object):   #场景

	def enter(self):
		print('This scene is not yet configured.---此场景尚未配置。')
		print('Subclass it and implement enter().---对它进行子类化并实现输入。')
		exit(1)


class Engine(object):   #引擎

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		#
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')

		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

		# be sure to print out the last scene_map
		current_scene.enter()


class Death(Scene):   #死亡

	quips = [
		"You died. You kinda suck at this.---你死了。你在这方面有点烂。",
		"You mom would be proud...if she were smarter.---你妈妈会感到骄傲的……如果她更聪明的话。",
		"Such a luser.---这样一个失败者。",
		"I have a small puppy that's better at this.---我有一只小狗，它更擅长这个。",
		"You're worse than your Dad's jokes.---你比你爸爸的笑话还烂。"
	]

	def enter(self):
		print(Death.quips[randint(0, len(self.quips)-1)])   #randint(0，x)函数，在0-x之间（包含）随机生成一个整数
		exit(1)


class CentralCorridor(Scene):  #中央走廊

	def enter(self):
		print(dedent("""
			The Gothons of planet Percal #25 haveinvaded your ship and desteoyed your entire crew.
			You are the last surviving member and your last mission is to get the neutron destruct bomb from the Weapons Armory,
			put it in the bridge, and blow the ship up afther getiing into an escape pod.
			You're running down the central corridor to the Weapons Armory when a Gothon jumps out ,
			red scaly skin, dark grimy filled body.
			He's blocking the door to the Armory and about topull a weapon blast you.
			---
			Percal25号星球上的哥顿人入侵了你的飞船，杀了你的全体船员。
			你是最后的幸存者，你最后的任务获得武器库里的中子毁灭炸弹，放在主控舱，然后把船炸成逃生舱。
			你沿着中央走廊跑去找武器军械库时，一只哥顿人跳出来，红色的鳞片皮肤，全身黑色的污垢。
			他挡住了军械库的门并用武器攻击你。
		"""))

		action = input('> ')

		if action == "shoot!":
			print(dedent("""
				Quick on the draw you yank out your blaster and fire it at the Gothon.
				His clown costume is flowing and moving around his body, which throws off you aim.
				This completely ruins his brand new costume but misses him entirely,
				which makes him fly into an insane rage and blast you repeatedly in the face untill you are dead.
				Then he eats you.
				---
				你迅速拔出你的爆破枪，向Gothon开火。
				他滑稽的服饰在他的身边流动，这使你无法瞄准。
				这完全破坏了他的全新服饰，但没有命中他，
				这使他勃然大怒，不断地朝你脸上猛烈攻击，直到你死去。
				然后他吃了你。
			"""))
			return 'death'

		elif action == 'dodge!':
			print(dedent("""
				Like a world class boxer you dodge, weave, slip and slide right as the Gothon's blaster cranks a laser past your head.
				In the middle of your artful dodge your foot slips and you bang your head on the metal wall and pass out.
				You wake up shortly after only to die as the Gothon stomps on your head and eats you.
				---
				就像一个世界级的拳击手，你躲避、迂回、滑动、向右滚动，Gothon的爆破枪发射的激光在你头上闪过。
				在巧妙闪避中你的脚滑了一下，你的头撞在了金属墙上之后晕倒了。
				你醒来后不久就死了，因为Gothon踩着你的头并吃掉了你。
			"""))
			return 'death'

		elif action == 'tell a joke!':
			print(dedent("""
				Lucky for you they made you learn Gothon insults in the academy.
				You tell the one Gothon joke you know:
				Lbhe zbgure vf fb sng , jura fur fvgf nebhaq gur ubhfr, jura fur fvgf nebhaq gur ubhfr.
				The Gothon stops, tries not to laugh, then busts out laughing and can't move.
				While he's laughing you run up and shoot him square in the head putting him down, then jump through the Weapon Armory door.
				---
				幸运的是，他们让你在学院里学会了Gothon侮辱性语言。
				你讲了一个你知道的Gothon笑话:
				Lbhe zbgure vf fb sng, jura fur fvgf nebhaq ubhfr, jura fur fvgf nebhaq ubhfr。
				Gothon停下来，试着不笑，然后突然大笑起来，动弹不得。
				当他在笑的时候，你跑上去朝他的头部开了一枪把他打倒，然后从武器室的门跳过去。
			"""))
			return 'laser_weapon_armory'  #激光武器库

		else:
			print('DOES NOT COMPUTE! --不算，重来--')
			return 'central_corridor'  #中央走廊


class LaserWeaponArmory(Scene):    #激光武器库

	def enter(self):
		print(dedent("""
			You do a dive roll into the Weapon Armory, crouch and scan the room for more Gothons that might be hiding.
			It's dead quiet, too quiet. You stand up and run to the far side of the room and find the neutron bomb in its container.
			There's a keypad lock on the box and you need the code to get the bomb out.
			If you get the code wrong 10 times then the lock closes forever and you can't get the bomb.
			The code is 3 digits.
			---
			你俯冲翻滚进武器库，蹲伏并扫描房间以寻找可能隐藏的更多Gothon。
			这里很安静，非常安静，你站起来跑到房间的另一边，在它的容器里找到了中子弹。
			盒子上有一个键盘锁，你需要密码才能把炸弹取出来。 如果你错了10次，锁就会永远关闭，你就得不到炸弹。
			密码是3位数。
		"""))

		code = f"{randint(8,9)}{randint(8,9)}{randint(8,9)}"
		guess = input("[keypad]> ")
		guesses = 0

		while guess != code and guesses < 10:
			print('BZZZZEDDD!')
			guesses += 1
			guess = input("[keypad]> ")

		if guess == code:
			print(dedent("""
				The container clicks open and the seal breaks, letting gas out.
				You grab the neutron bomb and run as fast as you can to he bridge where you must place it in the right spot.
				---
				容器咔嗒一声打开，密封破裂，让气体排出。
				你抓住中子弹并尽可能快地跑到主控舱，你必须将它放在正确的位置。
			"""))
			return 'the_bridge'   #主控舱

		else:
			print(dedent("""
				The lock buzzes one last time and then you hear a sickening melting sound as the mechanism is fused together.
				You decide to sit there, and you die .
				锁最后一次发出嗡嗡声，当装置融合在一起时你听到了令人作呕的融化声。
				你决定就坐在那里，你死了。
			"""))
			return 'death'


class TheBridge(Scene):   #主控舱

	def enter(self):
		print(dedent("""
			You burst onto the Bridge with the netron destruct bomb under your arm and surprise 5 Gothons who are trying to take control of the ship.
			Each of them has an even uglier clown costume than the last.
			They haven't pulled their weapons out yet,
			as they see the active bomb under your arm and don't want to set it off.
			---
			你胳膊挟着毁灭炸弹突然出现在主控舱，让试图控制这艘船的5个哥顿人大吃一惊。
			他们每个人都有比上一个更丑的滑稽服饰。
			他们没拿出武器，因为他们看到你胳膊下的炸弹，不想让它引爆。
		"""))

		action = input('> ')

		if action == 'throw the bomb':   #投掷炸弹
			print(dedent("""
				In a panic you throw the bomb at the group of Gothons and make a leap for the door.
				Right as you drop it a Gothon shoots you right in the back killing you.
				As you die you see another Gothon frantically try to disarm the bomb.
				You die knowing they will probably blow up when it goes off.
				---
				你惊慌失措地把炸弹扔向哥顿人，然后向门口跳去。
				就在你扔下它的时候，一只Gothon朝你的背部开枪杀死了你。
				当你死的时候，你会看到另一只Gothon疯狂地试图拆除炸弹。
				你死的时候知道它们可能会在拆弹的时候爆炸。
			"""))
			return 'death'

		elif action == 'slowly place the bomb':   #慢慢放置炸弹
			print(dedent("""
				You point your blaster at the bomb under your arm and the Gothons put their hands up and start to sweat .
				You inch backward to the door, open it ,and then carefully place the bomb on the floor, pointing your blaster at it.
				You then jump back through the door, punch the close button and blast the lock so the Gothon can't get out .
				Now that the bomb is placed you run to the escape pod to get off this tin can.
				---
				你用爆破枪指着你胳膊下的炸弹，哥顿人举起手开始冒汗。
				你慢慢的向门移动，打开门，然后小心地把炸弹放在地板上，用爆破枪指着它。
				然后你跳回门里，按下关闭按钮，破坏门锁，让Gothon跑不出去。
				既然炸弹已经放好了，你就跑到逃生舱去把这个“罐头”弄下来。
			"""))
			return 'escape_pod'   #逃生舱

		else:
			print('DOES NOT COMPUTE！--不算，重来--')
			return 'the_bridge'


class EscapePod(Scene):   #逃生舱

	def enter(self):
		print(dedent("""
			You rush through the ship desperately trying to make it to the escape pod before the whole ship explodes.
			It seems like hardly any Gothons are on the ship, so your run is clear of interference.
			You get to the chamber with the escape pods ,and now need to pick one to take.
			Some of them could be damage but you don't have time to look.
			There's 5 pods, which one do you take?
			---
			你拼命冲过飞船，试图在整个飞船爆炸前到达逃生舱。
			看来船上几乎没有哥顿人，所以你的奔跑没有干扰。
			你带着逃生舱来到了密室，现在需要选择一个逃生舱。
			其中一些可能会造成损害，但你没有时间去看。
			有5个逃生舱，你带哪一个?
		"""))

		good_pod = randint(1,2)
		guess = input('[pod #]> ')

		if int(guess) != good_pod:
			print(dedent(f"""
				You jump into pod {guess} and hit the eject button.
				The escapes pod  out into the void of space,
				then implodes as the hull ruptures, crushing your body into jam jelly.
				---
				进入{guess}#舱，然后点击弹出按钮。
				逃生舱飞出太空，
				然后在船体破裂时发生内爆，把你的身体压成果冻酱。
			"""))
			return 'death'

		else:
			print(dedent(f"""
				You jump into pod {guess} and hit the eject button.
				The pod easily slides out into space heading to the planet below.
				As it flies to the planet, you look back and see your ship implode then explode like a
				bright star, taking out the Gothon ship at the same time.
				You won!
				---
				进入{guess}#舱，然后点击弹出按钮。
				逃生舱很容易的飞出太空，，飞向下面的行星。
				当它飞向地球时，你回头看，你的飞船爆炸了，然后像一颗明亮的星，同时把Gothon飞船干掉了。
				你赢了！
			"""))
			return 'finished'


class Finished(Scene):   #游戏结束

	def enter(self):
		print("You won! Good job.")
		return 'finished'


class Map(object):   #地图

	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death': Death(),
		'finished': Finished(),
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

import pgzrun
from pygame import Rect
WIDTH, HEIGHT, TILE = 1280, 640, 32
TITLE = "The Little Green Hero"
blocks = []
game_state = "menu"
music_on = True
lives = 3
level = [
    "........................................",
    "........................................",
    ".....................U..................",
    "............S..T..QWWE..............S.F.",
    ".....C......T............T..........QWWE",
    "....QWWWE...............................",
    "...T............................C.......",
    ".............................QWWWE......",
    "........................................",
    "T.......................................",
    "........................................",
    "......U..............UU.T...............",
    ".QWWWWWE....T...QWWWWWE.....SS..........",
    "............................QWWWE.......",
    ".....................................C..",
    "...................................OBBBP",
    "...................................GHHHJ",
    ".S.....C...QWWWWWE.................GHHHJ",
    "BBBBBBBBPKKKKKKKKKKKOBBPKKKKOBBBBBBHHHHJ",
    "HHHHHHHHJLLLLLLLLLLLGHHJLLLLGHHHHHHHHHHH"
]
tiles = {
    "B":"block","W":"blockfly_center","Q":"blockfly_left","E":"blockfly_right",
    "G":"ground_left","J":"ground_right","H":"ground_center","K":"lava",
    "O":"blocksl","P":"blocksr","T":"ground_fly","L":"lava_in","F":"flag_green_a",
    "C":"cactus", "U":"bush", "S":"grass"
}
life_display = [
    Actor("hero_logo", (20, 20)),
    Actor("0", (52, 20)),
    Actor("3", (84, 20))
]
def update_life_display():
    life_str = f"{lives:02d}"
    life_display[1].image = life_str[0]
    life_display[2].image = life_str[1]
def block_hitbox(b):
    return Rect(b.left, b.top, b.width, b.height)
class Hero(Actor):
    def __init__(self, pos):
        super().__init__("hero_idle", pos) 
        self.vy, self.face_right, self.on_ground = 0, True, False
        self.run_r, self.run_l = ["hero_run1", "hero_run2"], ["hero_run1l", "hero_run2l"]
        self.jump_r, self.jump_l = ["hero_jump1", "hero_jump2"], ["hero_jump1l", "hero_jump2l"]
        self.idle_r, self.idle_l = "hero_idle", "hero_idlel"
        self.idle_special_frames = ["hero", "hero_idle", "hero_idlel"]
        self.frame, self.idle_timer, self.idle_anim_frame_index = 0.0, 0, 0.0
    def get_hitbox(self):
        return Rect(self.x - 17, self.y - 24, 34, 48)
    def get_feet_probe(self):
        hb = self.get_hitbox(); return Rect(hb.x + 6, hb.bottom, hb.width - 12, 4)
    def check_on_ground(self, blocks):
        probe = self.get_feet_probe()
        for b in blocks:
            if b.image in ("lava", "lava_in", "flag_green_a", "flag_green_b", "laval", "cactus", "bush", "grass"): continue
            if probe.colliderect(block_hitbox(b)): return True
        return False
    def reset_position(self):
        self.x, self.y, self.vy = 32, HEIGHT - 64, 0
        self.image, self.face_right = self.idle_r, True
        self.frame, self.idle_timer, self.idle_anim_frame_index = 0.0, 0, 0.0
        if music_on: sounds.death.play()
    def update(self, blocks):
        dx = 0
        if keyboard.left: dx -= 3; self.face_right = False
        if keyboard.right: dx += 3; self.face_right = True
        self.x += dx
        hb = self.get_hitbox()
        for b in blocks:
            if b.image in ("lava", "lava_in", "laval", "cactus", "bush", "grass") or b.image.startswith("flag_green_"): continue
            bb = block_hitbox(b)
            if hb.colliderect(bb):
                if dx > 0: self.x = bb.left - (hb.width // 2)
                elif dx < 0: self.x = bb.right + (hb.width // 2)
                hb.x = self.x - hb.width // 2
        self.on_ground = self.check_on_ground(blocks)
        if keyboard.space and self.on_ground:
            self.vy = -11
            if music_on: sounds.jump.play()
        self.vy += 0.5
        self.y += self.vy
        hb = self.get_hitbox()
        probe = self.get_feet_probe()
        lava_below, solid_below = False, False
        for b in blocks:
            bb = block_hitbox(b)
            if b.image.startswith("flag_green_") and hb.colliderect(bb): return "win"
            if b.image == "lava_in" and hb.colliderect(bb): return "reset" 
            if (b.image == "lava" or b.image == "laval") and probe.colliderect(bb): lava_below = True 
            if b.image not in ("lava", "lava_in", "flag_green_a", "flag_green_b", "laval", "cactus", "bush", "grass") and probe.colliderect(bb): solid_below = True
            if b.image in ("lava", "lava_in", "flag_green_a", "flag_green_b", "laval", "cactus", "bush", "grass"): continue
            if hb.colliderect(bb):
                if self.vy > 0 and hb.bottom > bb.top and hb.top < bb.top:
                    self.y = bb.top - (hb.height // 2)
                    self.vy = 0
                elif self.vy < 0 and hb.top < bb.bottom and hb.bottom > bb.bottom:
                    self.y = bb.bottom + (hb.height // 2)
                    self.vy = 0
                hb = self.get_hitbox()
        if lava_below and not solid_below: return "reset"
        if not self.on_ground:
            if self.face_right: self.image = self.jump_r[0] if self.vy < 0 else self.jump_r[1]
            else: self.image = self.jump_l[0] if self.vy < 0 else self.jump_l[1]
            self.frame, self.idle_timer, self.idle_anim_frame_index = 0.0, 0, 0.0
        elif dx != 0:
            self.frame = (self.frame + 0.18) % 2
            self.image = (self.run_r if self.face_right else self.run_l)[int(self.frame)]
            self.idle_timer, self.idle_anim_frame_index = 0, 0.0
        else:
            self.idle_timer += 1
            seconds_idle = self.idle_timer / 60.0
            if seconds_idle < 3.0:
                self.image = self.idle_r if self.face_right else self.idle_l
                self.frame, self.idle_anim_frame_index = 0.0, 0.0
            else:
                self.idle_anim_frame_index = (self.idle_anim_frame_index + 0.08) % len(self.idle_special_frames)
                self.image = self.idle_special_frames[int(self.idle_anim_frame_index)]
        if self.left < 0: self.left = 0
        if self.right > WIDTH: self.right = WIDTH
        if self.top < 0: self.top = 0
        if self.bottom > HEIGHT:
            self.bottom = HEIGHT
            self.vy = 0
        return "play"
class Enemy(Actor):
    def __init__(self, img, x, y, vx, minx, maxx, vy=0, miny=0, maxy=0, frames=None):
        super().__init__(img, (x, y)); self.vx, self.min_x, self.max_x = vx, minx, maxx; self.vy, self.min_y, self.max_y = vy, miny, maxy; self.base_frames = frames if frames else [img]; self.frame_index = 0.0
    def get_hitbox(self):
        return Rect(self.x - 14, self.y - 28, 28, 56)
    def update(self):
        self.x += self.vx;
        if self.x < self.min_x or self.x > self.max_x: self.vx *= -1
        self.y += self.vy;
        if self.y < self.min_y or self.y > self.max_y: self.vy *= -1
        self.update_animation()
    def update_animation(self):
        frames_to_use = self.base_frames
        if self.base_frames[0] == "bee":
            if self.vx > 0: frames_to_use = ["beel", "bee2l"]
            elif self.vx < 0: frames_to_use = ["bee", "bee2"]
        self.frame_index = (self.frame_index + 0.12) % len(frames_to_use)
        self.image = frames_to_use[int(self.frame_index)]
def build_level(level_data, tile_map):
    level_blocks = []
    for y, row in enumerate(level_data):
        for x, col in enumerate(row):
            if col in tile_map:
                level_blocks.append(Actor(tile_map[col], (x * TILE + TILE // 2, y * TILE + TILE // 2)))
    return level_blocks
def lose_life():
    global lives, game_state
    lives -= 1
    update_life_display()
    if lives <= 0:
        game_state = "game_over"
        music.stop()
    else:
        hero.reset_position()
def full_reset_game():
    global lives, game_state
    lives = 3
    game_state = "play"
    hero.x, hero.y, hero.vy = 32, HEIGHT - 64, 0
    hero.image, hero.face_right = hero.idle_r, True
    update_life_display()
    if music_on and not music.is_playing('music.mp3'): 
        music.play("music.mp3")
        music.set_volume(0.3)
blocks = build_level(level, tiles)
hero = Hero((32, HEIGHT - 64))
enemy_data = [
    ("worm", 150, HEIGHT - 73, 0.7, 150, 260, 0, 0, 0, ["worm", "worm2"]),
    ("worm", 150, HEIGHT - 490, 1.0, 150, 260, 0, 0, 0, ["worm", "worm2"]),
    ("worm", 650, HEIGHT - 73, 0.5, 650, 750, 0, 0, 0, ["worm", "worm2"]),
    ("bee", 850, 250, 0, 0, 0, 4, 50, 530, ["bee", "bee2"]),
    ("bee", 210, 360, 2.5, 210, 550, 0, 0, 0, ["bee", "bee2"])
]
enemies = [Enemy(*d) for d in enemy_data]
menu_buttons = {
    "play": (Rect(0, 0, 220, 50), "Play"),
    "sound": (Rect(0, 0, 220, 50), "Sound: On"),
    "exit": (Rect(0, 0, 220, 50), "Exit")
}
menu_buttons["play"][0].center = (WIDTH // 2, HEIGHT // 2 - 40)
menu_buttons["sound"][0].center = (WIDTH // 2, HEIGHT // 2 + 20)
menu_buttons["exit"][0].center = (WIDTH // 2, HEIGHT // 2 + 80)
def draw():
    if game_state == "menu":
        screen.blit("background_menu", (0, 0))
        screen.draw.text(TITLE, center=(WIDTH // 2, HEIGHT // 2 - 140), fontsize=60, color="white")
        for key in menu_buttons:
            rect, text = menu_buttons[key]
            screen.draw.filled_rect(rect, (0, 80, 120))
            screen.draw.textbox(text, rect, color="white", align="center")
        instructions_rect = Rect(0, 0, 700, 150)
        instructions_rect.center = (WIDTH // 2, HEIGHT // 2 + 190)
        instructions_text = "Welcome to the game!\n\nUse Arrow Keys to move and Spacebar to jump. Avoid all creatures and lava. You have 3 lives. Good luck!\n(Press ESC to quit at any time)"
        screen.draw.text(instructions_text, topleft=instructions_rect.topleft, width=instructions_rect.width, color="white", fontsize=28, align="center")
        return
    if game_state == "win":
        screen.blit("background_win", (0, 0))
        screen.draw.text("Congratulations! You Win!", center=(WIDTH // 2, HEIGHT // 2), fontsize=60, color="yellow")
        for actor in life_display: actor.draw()
        return
    if game_state == "game_over":
        screen.blit("background_death", (0, 0))
        screen.draw.text("GAME OVER", center=(WIDTH // 2, HEIGHT // 2 - 20), fontsize=60, color="red")
        screen.draw.text("Click to return to menu", center=(WIDTH // 2, HEIGHT // 2 + 40), fontsize=40, color="white")
        return
    
    screen.blit("background", (0, 0))
    for b in blocks:
        if b.image.startswith("flag_green_"): b.draw()
        elif b.image not in ("lava", "laval"): b.draw() 
    for e in enemies: e.draw()
    hero.draw()
    for b in blocks:
        if b.image == "lava" or b.image == "laval": b.draw()
    for actor in life_display: actor.draw()
def update():
    global game_state
    if game_state != "play": return
    hero_status = hero.update(blocks) 
    if hero_status == "win":
        game_state = "win"
        music.stop()
        if music_on: sounds.win.play()
        return
    if hero_status == "reset":
        lose_life()
        return
    for e in enemies:
        e.update()
        if hero.get_hitbox().colliderect(e.get_hitbox()):
            lose_life()
            return
    for b in blocks:
        if b.image.startswith("flag_green_"):
            if not hasattr(b, "flag_timer"): b.flag_timer = 0
            b.flag_timer += 1
            if b.flag_timer % 15 == 0:
                b.image = "flag_green_b" if b.image == "flag_green_a" else "flag_green_a"
        elif b.image == "lava" or b.image == "laval":
            if not hasattr(b, "lava_timer"): b.lava_timer = 0
            b.lava_timer += 1
            if b.lava_timer % 20 == 0:
                b.image = "laval" if b.image == "lava" else "lava"
def on_mouse_down(pos):
    global game_state, music_on
    if game_state == "game_over":
        game_state = "menu"
        if music_on: music.play("music.mp3")
        return
    if game_state == "menu":
        if menu_buttons["play"][0].collidepoint(pos):
            full_reset_game()
        if menu_buttons["sound"][0].collidepoint(pos):
            music_on = not music_on
            if music_on: music.unpause()
            else: music.pause()
            menu_buttons["sound"] = (menu_buttons["sound"][0], f"Sound: {'On' if music_on else 'Off'}")
        if menu_buttons["exit"][0].collidepoint(pos):
            quit()
            
def on_key_down(key):
    if key == keys.ESCAPE:
        quit()
        
music.play("music.mp3")
music.set_volume(0.3)
pgzrun.go()


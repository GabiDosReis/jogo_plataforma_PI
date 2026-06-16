import os
import pygame as pg
import random

class TreasureHunters:

    def __init__(self):
        
        pg.init()
        self.BASE_DIR = os.path.dirname(__file__)
        self.white        = (255, 255, 255)
        self.black        = (  0,   0,   0)
        self.purple_dark  = (181, 181, 255)
        self.purple_light = (230, 230, 255)
        self.green        = (  0, 255,   0)
        self.green_light  = (180, 255, 180)
        self.blue         = (  0,   0, 255)

        self.window = pg.display.set_mode((1280, 768))

        pg.font.init()
        self.font = pg.font.SysFont("Courier New", 50, bold=True)

        self.clock = pg.time.Clock()

        self.map = [
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M','M',' ',' ',' ',' ',' ',' ',' '],

        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],

        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],

        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],

        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ','M',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ','1','2','3',' ',' ',' ',' ',' ',' ',' ',' ',' '],

        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','2','3',' ',' ','7','8','9',' ',' ',' ',' ',' ',' ',' ',' ',' '],

        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ',' ','1','2','3',' ',' ','7','8','9',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],

        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','M',' ',' ','1','3',' ','1','2','3',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','2','3',' ',' ','7','8','9',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],

        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','2','3',' ','7','9',' ','4','5','6',' ',' ',' ','1','2','3',' ',' ',' ','1','2','3',' ',' ',' ','1','2','3',' ',' ',' ','1','2','3',' ',' ',' ',' ',' ',' ',' ',' ','1','2','3',' ',' ','7','8','9',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],

        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','7','8','9',' ',' ',' ',' ','4','5','6',' ',' ',' ','7','8','9',' ',' ',' ','7','8','9',' ',' ',' ','7','8','9',' ',' ',' ','7','8','9',' ',' ',' ','1','2','3',' ',' ','7','8','9',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','F',' ',' ',' '],

        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','4','5','6',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','7','8','9',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','2','2','2','3',' '],

        ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','5','5','6',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','7','8','8','8','9',' ']
        ]

        #gravidade
        self.gravity = 1

        #nuvens
        self.big_clouds_pos = 0
        self.small_cloud_1_pos = 0
        self.small_cloud_2_pos = 0
        self.small_cloud_3_pos = 0
        
        #jogador
        self.player_animation = 0
        self.player_animation_frame = 0
        self.player_pos = [300, 600]
        self.player_jump_force = -22
        self.player_vertical_speed = 0
        self.player_box_colider = [46, 54]

        #moedas
        self.coins = 0

        #bombas
        self.bomb_warnings = []
        self.warning_timer = 0
        self.warning_interval = 45  # 0,75 segundos em 60 FPS
        self.warning_time = 0
        self.bomb_speed = 25

        self.warning_duration = 30   # 0,50s
        self.warning_delay = 180     # 3,5s

        self.warning_active = False

        self.bombs = []

        #piso
        self.on_ground = False

        #camera
        self.camera_x = 0
        self.camera_y = 0

        #vitoria/gameover
        self.win = False
        self.game_over = False

        # Mouse variables
        self.last_click_status = (False, False, False)

        # Captain Clown Nose (Idle)
        player_idle_1_img = self.load_image(
            'Sprites',
            'Captain Clown Nose',
            'Captain Clown Nose without Sword',
            '01-Idle',
            'Idle 01.png'
        )
        self.player_idle_1 = pg.transform.scale(player_idle_1_img, (128, 80))
        player_idle_2_img = self.load_image(
            'Sprites',
            'Captain Clown Nose',
            'Captain Clown Nose without Sword',
            '01-Idle',
            'Idle 02.png'
        )
        self.player_idle_2 = pg.transform.scale(player_idle_2_img, (128, 80))
        player_idle_3_img = self.load_image(
            'Sprites',
            'Captain Clown Nose',
            'Captain Clown Nose without Sword',
            '01-Idle',
            'Idle 03.png'
        )
        self.player_idle_3 = pg.transform.scale(player_idle_3_img, (128, 80))
        player_idle_4_img = self.load_image(
            'Sprites',
            'Captain Clown Nose',
            'Captain Clown Nose without Sword',
            '01-Idle',
            'Idle 04.png'
        )
        self.player_idle_4 = pg.transform.scale(player_idle_4_img, (128, 80))
        player_idle_5_img = self.load_image(
            'Sprites',
            'Captain Clown Nose',
            'Captain Clown Nose without Sword',
            '01-Idle',
            'Idle 05.png'
        )
        self.player_idle_5 = pg.transform.scale(player_idle_5_img, (128, 80))
        # Captain Clown Nose (Idle left)
        player_idle_left_1_img = self.load_image(
            'Sprites',
            'Captain Clown Nose',
            'Captain Clown Nose without Sword',
            '01-Idle',
            'Idle 01.png'
        )
        self.player_idle_left_1 = pg.transform.scale(player_idle_left_1_img, (128, 80))
        player_idle_left_2_img = self.load_image(
            'Sprites',
            'Captain Clown Nose',
            'Captain Clown Nose without Sword',
            '01-Idle',
            'Idle 02.png'
        )
        self.player_idle_left_2 = pg.transform.scale(player_idle_left_2_img, (128, 80))
        player_idle_left_3_img = self.load_image(
            'Sprites',
            'Captain Clown Nose',
            'Captain Clown Nose without Sword',
            '01-Idle',
            'Idle 03.png'
        )
        self.player_idle_left_3 = pg.transform.scale(player_idle_left_3_img, (128, 80))
        player_idle_left_4_img = self.load_image(
            'Sprites',
            'Captain Clown Nose',
            'Captain Clown Nose without Sword',
            '01-Idle',
            'Idle 04.png'
        )
        self.player_idle_left_4 = pg.transform.scale(player_idle_left_4_img, (128, 80))
        player_idle_left_5_img = self.load_image(
            'Sprites',
            'Captain Clown Nose',
            'Captain Clown Nose without Sword',
            '01-Idle',
            'Idle 05.png'
        )
        self.player_idle_left_5 = pg.transform.scale(player_idle_left_5_img, (128, 80))
        # Captain Clown Nose (Run right)
        player_right_1_img = self.load_image(
            'Sprites',
            'Captain Clown Nose',
            'Captain Clown Nose without Sword',
            '02-Run',
            'Run 01.png'
        )
        self.player_right_1 = pg.transform.scale(player_right_1_img, (128, 80))
        player_right_2_img = self.load_image(
            'Sprites',
            'Captain Clown Nose',
            'Captain Clown Nose without Sword',
            '02-Run',
            'Run 02.png'
        )
        self.player_right_2 = pg.transform.scale(player_right_2_img, (128, 80))
        player_right_3_img = self.load_image(
            'Sprites',
            'Captain Clown Nose',
            'Captain Clown Nose without Sword',
            '02-Run',
            'Run 03.png'
        )
        self.player_right_3 = pg.transform.scale(player_right_3_img, (128, 80))
        player_right_4_img = self.load_image(
            'Sprites',
            'Captain Clown Nose',
            'Captain Clown Nose without Sword',
            '02-Run',
            'Run 04.png'
        )
        self.player_right_4 = pg.transform.scale(player_right_4_img, (128, 80))
        player_right_5_img = self.load_image(
            'Sprites',
            'Captain Clown Nose',
            'Captain Clown Nose without Sword',
            '02-Run',
            'Run 05.png'
        )
        self.player_right_5 = pg.transform.scale(player_right_5_img, (128, 80))
        player_right_6_img = self.load_image(
            'Sprites',
            'Captain Clown Nose',
            'Captain Clown Nose without Sword',
            '02-Run',
            'Run 06.png'
        )
        self.player_right_6 = pg.transform.scale(player_right_6_img, (128, 80))
        # Captain Clown Nose (Run left)
        player_left_1_img = self.load_image(
            'Sprites',
            'Captain Clown Nose',
            'Captain Clown Nose without Sword',
            '02-Run',
            'Run 01.png'
        )
        player_left_1_img = pg.transform.flip(player_left_1_img, True, False)
        self.player_left_1 = pg.transform.scale(player_left_1_img, (128, 80))
        player_left_2_img = self.load_image(
            'Sprites',
            'Captain Clown Nose',
            'Captain Clown Nose without Sword',
            '02-Run',
            'Run 02.png'
        )
        player_left_2_img = pg.transform.flip(player_left_2_img, True, False)
        self.player_left_2 = pg.transform.scale(player_left_2_img, (128, 80))
        player_left_3_img = self.load_image(
            'Sprites',
            'Captain Clown Nose',
            'Captain Clown Nose without Sword',
            '02-Run',
            'Run 03.png'
        )
        player_left_3_img = pg.transform.flip(player_left_3_img, True, False)
        self.player_left_3 = pg.transform.scale(player_left_3_img, (128, 80))
        player_left_4_img = self.load_image(
            'Sprites',
            'Captain Clown Nose',
            'Captain Clown Nose without Sword',
            '02-Run',
            'Run 04.png'
        )
        player_left_4_img = pg.transform.flip(player_left_4_img, True, False)
        self.player_left_4 = pg.transform.scale(player_left_4_img, (128, 80))
        player_left_5_img = self.load_image(
            'Sprites',
            'Captain Clown Nose',
            'Captain Clown Nose without Sword',
            '02-Run',
            'Run 05.png'
        )
        player_left_5_img = pg.transform.flip(player_left_5_img, True, False)
        self.player_left_5 = pg.transform.scale(player_left_5_img, (128, 80))
        player_left_6_img = self.load_image(
            'Sprites',
            'Captain Clown Nose',
            'Captain Clown Nose without Sword',
            '02-Run',
            'Run 06.png'
        )
        player_left_6_img = pg.transform.flip(player_left_6_img, True, False)
        self.player_left_6 = pg.transform.scale(player_left_6_img, (128, 80))
        # Background
        background_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Background',
            'BG Image.png'
        )
        self.background = pg.transform.scale(background_img, (1280, 768))
        big_clouds_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Background',
            'Big Clouds.png'
        )
        self.big_clouds = pg.transform.scale(big_clouds_img, (896, 202))
        # Clouds
        small_cloud_1_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Background',
            'Small Cloud 1.png'
        )
        self.small_cloud_1 = pg.transform.scale(small_cloud_1_img, (148, 48))
        small_cloud_2_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Background',
            'Small Cloud 2.png'
        )
        self.small_cloud_2 = pg.transform.scale(small_cloud_2_img, (266, 70))
        small_cloud_3_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Background',
            'Small Cloud 3.png'
        )
        self.small_cloud_3 = pg.transform.scale(small_cloud_3_img, (280, 78))
        # Water (Big)
        self.big_water_animation_frame = 0
        big_water_1_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Background',
            'Water Reflect Big 01.png'
        )
        self.big_water_1 = pg.transform.scale(big_water_1_img, (340, 20))
        big_water_2_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Background',
            'Water Reflect Big 02.png'
        )
        self.big_water_2 = pg.transform.scale(big_water_2_img, (340, 20))
        big_water_3_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Background',
            'Water Reflect Big 03.png'
        )
        self.big_water_3 = pg.transform.scale(big_water_3_img, (340, 20))
        big_water_4_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Background',
            'Water Reflect Big 04.png'
        )
        self.big_water_4 = pg.transform.scale(big_water_4_img, (340, 20))
        # Water (Medium)
        self.medium_water_animation_frame = 0
        medium_water_1_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Background',
            'Water Reflect Medium 01.png'
        )
        self.medium_water_1 = pg.transform.scale(medium_water_1_img, (106, 6))
        medium_water_2_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Background',
            'Water Reflect Medium 02.png'
        )
        self.medium_water_2 = pg.transform.scale(medium_water_2_img, (106, 6))
        medium_water_3_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Background',
            'Water Reflect Medium 03.png'
        )
        self.medium_water_3 = pg.transform.scale(medium_water_3_img, (106, 6))
        medium_water_4_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Background',
            'Water Reflect Medium 04.png'
        )
        self.medium_water_4 = pg.transform.scale(medium_water_4_img, (106, 6))
        # Water (Small)
        self.small_water_animation_frame = 0
        small_water_1_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Background',
            'Water Reflect Small 01.png'
        )
        self.small_water_1 = pg.transform.scale(small_water_1_img, (70, 6))
        small_water_2_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Background',
            'Water Reflect Small 02.png'
        )
        self.small_water_2 = pg.transform.scale(small_water_2_img, (70, 6))
        small_water_3_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Background',
            'Water Reflect Small 03.png'
        )
        self.small_water_3 = pg.transform.scale(small_water_3_img, (70, 6))
        small_water_4_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Background',
            'Water Reflect Small 04.png'
        )
        self.small_water_4 = pg.transform.scale(small_water_4_img, (70, 6))
        # Terrain
        ground_1_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Terrain',
            'ground_1.png'
        )
        self.ground_1 = pg.transform.scale(ground_1_img, (64, 64))
        ground_2_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Terrain',
            'ground_2.png'
        )
        self.ground_2 = pg.transform.scale(ground_2_img, (64, 64))
        ground_3_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Terrain',
            'ground_3.png'
        )
        self.ground_3 = pg.transform.scale(ground_3_img, (64, 64))
        ground_4_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Terrain',
            'ground_4.png'
        )
        self.ground_4 = pg.transform.scale(ground_4_img, (64, 64))
        ground_5_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Terrain',
            'ground_5.png'
        )
        self.ground_5 = pg.transform.scale(ground_5_img, (64, 64))
        ground_6_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Terrain',
            'ground_6.png'
        )
        self.ground_6 = pg.transform.scale(ground_6_img, (64, 64))
        ground_7_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Terrain',
            'ground_7.png'
        )
        self.ground_7 = pg.transform.scale(ground_7_img, (64, 64))
        ground_8_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Terrain',
            'ground_8.png'
        )
        self.ground_8 = pg.transform.scale(ground_8_img, (64, 64))
        ground_9_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Terrain',
            'ground_9.png'
        )
        self.ground_9 = pg.transform.scale(ground_9_img, (64, 64))

        coin_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Objetos',
            'moeda.png'
        )

        self.coin = pg.transform.scale(coin_img, (64, 64))

        flag_img = self.load_image(
            'Sprites',
            'Palm Tree Island',
            'Objetos',
            'Bandeira_final.png'
        )
        self.flag = pg.transform.scale(flag_img, (64, 64))


    def load_image(self, *path):
        return pg.image.load(os.path.join(self.BASE_DIR, *path))


    def mouse_has_clicked(self, input):
            if self.last_click_status == input:
                return (False, False, False)
            else:
                left_button = False
                center_button = False
                right_button = False
                if self.last_click_status[0] == False and input[0] == True:
                    left_button = True
                if self.last_click_status[1] == False and input[1] == True:
                    center_button = True
                if self.last_click_status[2] == False and input[2] == True:
                    right_button = True

                return (left_button, center_button, right_button)

    def background_imgs(self):
        # Background
        self.window.blit(self.background, (0, 0))
        # Big Clouds
        if self.big_clouds_pos > -896:
            self.big_clouds_pos -= 0.05
        else:
            self.big_clouds_pos = 0
        self.window.blit(self.big_clouds, (self.big_clouds_pos, 315))
        self.window.blit(self.big_clouds, (self.big_clouds_pos + 896, 315))
        self.window.blit(self.big_clouds, (self.big_clouds_pos + (896 * 2), 315))
        # Small Cloud 1
        if self.small_cloud_1_pos > -1500:
            self.small_cloud_1_pos -= 0.3
        else:
            self.small_cloud_1_pos = 0
        self.window.blit(self.small_cloud_1, (120 + self.small_cloud_1_pos, 100))
        self.window.blit(self.small_cloud_1, (120 + self.small_cloud_1_pos + 1500, 100))
        self.window.blit(self.small_cloud_1, (900 + self.small_cloud_1_pos, 50))
        self.window.blit(self.small_cloud_1, (900 + self.small_cloud_1_pos + 1500, 50))
        # Small Cloud 2
        if self.small_cloud_2_pos > -1500:
            self.small_cloud_2_pos -= 0.2
        else:
            self.small_cloud_2_pos = 0
        self.window.blit(self.small_cloud_2, (250 + self.small_cloud_2_pos, 200))
        self.window.blit(self.small_cloud_2, (250 + self.small_cloud_2_pos + 1500, 200))
        self.window.blit(self.small_cloud_2, (1000 + self.small_cloud_2_pos, 150))
        self.window.blit(self.small_cloud_2, (1000 + self.small_cloud_2_pos + 1500, 150))
        # Small Cloud 3
        if self.small_cloud_2_pos > -1500:
            self.small_cloud_3_pos -= 0.2
        else:
            self.small_cloud_3_pos = 0
        self.window.blit(self.small_cloud_3, (650 + self.small_cloud_3_pos, 250))
        self.window.blit(self.small_cloud_3, (650 + self.small_cloud_3_pos + 1500, 250))
        # Big water effect
        if self.big_water_animation_frame <= 12:
            self.window.blit(self.big_water_1, (300, 550))
        if self.big_water_animation_frame <= 24:
            self.window.blit(self.big_water_2, (300, 550))
        if self.big_water_animation_frame <= 36:
            self.window.blit(self.big_water_3, (300, 550))
        if self.big_water_animation_frame <= 48:
            self.window.blit(self.big_water_4, (300, 550))
        self.big_water_animation_frame += 1
        if self.big_water_animation_frame > 48:
            self.big_water_animation_frame = 0
        # Medium water effect
        if self.medium_water_animation_frame <= 12:
            self.window.blit(self.medium_water_1, (250, 600))
            self.window.blit(self.medium_water_1, (500, 625))
        if self.big_water_animation_frame <= 24:
            self.window.blit(self.medium_water_2, (250, 600))
            self.window.blit(self.medium_water_2, (500, 625))
        if self.big_water_animation_frame <= 36:
            self.window.blit(self.medium_water_3, (250, 600))
            self.window.blit(self.medium_water_3, (500, 625))
        if self.big_water_animation_frame <= 48:
            self.window.blit(self.medium_water_4, (250, 600))
            self.window.blit(self.medium_water_4, (500, 625))
        self.medium_water_animation_frame += 1
        if self.medium_water_animation_frame > 48:
            self.medium_water_animation_frame = 0
        # Small water effect
        if self.small_water_animation_frame <= 12:
            self.window.blit(self.small_water_1, (1000, 600))
            self.window.blit(self.small_water_1, (900, 625))
        if self.small_water_animation_frame <= 24:
            self.window.blit(self.small_water_2, (1000, 600))
            self.window.blit(self.small_water_3, (900, 625))
        if self.small_water_animation_frame <= 36:
            self.window.blit(self.small_water_3, (1000, 600))
            self.window.blit(self.small_water_3, (900, 625))
        if self.small_water_animation_frame <= 48:
            self.window.blit(self.small_water_4, (1000, 600))
            self.window.blit(self.small_water_4, (900, 625))
        self.small_water_animation_frame += 1
        if self.small_water_animation_frame > 48:
            self.small_water_animation_frame = 0

    def tiles(self):
        range_y = len(self.map)
        range_x = len(self.map[0])
        for y in range(range_y):
            for x in range(range_x):
                if self.map[y][x] != ' ':
                    if self.map[y][x] == '1':
                        self.window.blit(
                            self.ground_1,
                            (
                                x * 64 - self.camera_x,
                                y * 64 - self.camera_y
                            )
                        )
                    elif self.map[y][x] == '2':
                        self.window.blit(
                            self.ground_2,
                            (
                                x * 64 - self.camera_x,
                                y * 64 - self.camera_y
                            )
                        )
                    elif self.map[y][x] == '3':
                        self.window.blit(
                            self.ground_3,
                            (
                                x * 64 - self.camera_x,
                                y * 64 - self.camera_y
                            )
                        )
                    elif self.map[y][x] == '4':
                        self.window.blit(
                            self.ground_4,
                            (
                                x * 64 - self.camera_x,
                                y * 64 - self.camera_y
                            )
                        )
                    elif self.map[y][x] == '5':
                        self.window.blit(
                            self.ground_5,
                            (
                                x * 64 - self.camera_x,
                                y * 64 - self.camera_y
                            )
                        )
                    elif self.map[y][x] == '6':
                        self.window.blit(
                            self.ground_6,
                            (
                                x * 64 - self.camera_x,
                                y * 64 - self.camera_y
                            )
                        )
                    elif self.map[y][x] == '7':
                        self.window.blit(
                            self.ground_7,
                            (
                                x * 64 - self.camera_x,
                                y * 64 - self.camera_y
                            )
                        )
                    elif self.map[y][x] == '8':
                        self.window.blit(
                            self.ground_8,
                            (
                                x * 64 - self.camera_x,
                                y * 64 - self.camera_y
                            )
                        )
                    elif self.map[y][x] == '9':
                        self.window.blit(
                            self.ground_9,
                            (
                                x * 64 - self.camera_x,
                                y * 64 - self.camera_y
                            )
                        )
                            
                    elif self.map[y][x] == 'F':
                        self.window.blit(
                            self.flag,
                            (
                                x * 64 - self.camera_x,
                                y * 64 - self.camera_y
                            )
                        )

                    elif self.map[y][x] == 'M':
                        self.window.blit(
                            self.coin,
                            (
                                x * 64 - self.camera_x,
                                y * 64 - self.camera_y
                            )
                        )
                        
    def collect_coins(self):

        player_rect = pg.Rect(
            self.player_pos[0] + 40,
            self.player_pos[1] + 8,
            self.player_box_colider[0],
            self.player_box_colider[1]
        )

        for y in range(len(self.map)):
            for x in range(len(self.map[0])):

                if self.map[y][x] == 'M':

                    coin_rect = pg.Rect(
                        x * 64,
                        y * 64,
                        64,
                        64
                    )

                    if player_rect.colliderect(coin_rect):

                        self.map[y][x] = ' '
                        self.coins += 1
    
    def draw_coins(self):

        text = self.font.render(
            f"MOEDAS: {self.coins}",
            True,
            (255,255,255)
        )

        self.window.blit(text, (20, 20))

    def draw_bomb_warnings(self):

        if not self.warning_active:
            return

        if self.warning_time % 20 < 10:

            for warning in self.bomb_warnings:

                pg.draw.line(
                    self.window,
                    (255,0,0),
                    (warning["x"] - self.camera_x, 0),
                    (warning["x"] - self.camera_x, 768),
                    4
                )

    def create_warnings(self):

        self.bomb_warnings.clear()

        distancia_minima = 150

        tentativas = 0

        while len(self.bomb_warnings) < 5 and tentativas < 100:

            tentativas += 1

            x = random.randint(
                self.camera_x,
                self.camera_x + 1280
            )

            valido = True

            for warning in self.bomb_warnings:

                if abs(x - warning["x"]) < distancia_minima:

                    valido = False
                    break

            if valido:

                self.bomb_warnings.append({
                    "x": x
                })

    def bomb_manager(self):

        self.warning_time += 1

        if not self.warning_active:

            if self.warning_time >= self.warning_delay:

                self.create_warnings()

                self.warning_active = True

                self.warning_time = 0

        else:

            if self.warning_time >= self.warning_duration:

                for warning in self.bomb_warnings:

                    self.bombs.append({
                        "x": warning["x"],
                        "y": -100,
                        "speed": self.bomb_speed
                    })

                self.bomb_warnings.clear()

                self.warning_active = False

                self.warning_time = 0

    def draw_bombs(self):

        for bomb in self.bombs:

            pg.draw.circle(
                self.window,
                (0,0,0),
                (
                    int(bomb["x"] - self.camera_x),
                    int(bomb["y"] - self.camera_y)
                ),
                20
            )

    def update_bombs(self):

        bombs_to_remove = []

        player_rect = pg.Rect(
            self.player_pos[0] + 40,
            self.player_pos[1] + 8,
            self.player_box_colider[0],
            self.player_box_colider[1]
        )

        for bomb in self.bombs:

            bomb["y"] += bomb["speed"]

            bomb_rect = pg.Rect(
                bomb["x"] - 20,
                bomb["y"] - 20,
                40,
                40
            )
            if bomb_rect.colliderect(player_rect):

                self.game_over = True
                bombs_to_remove.append(bomb)
                continue

            tile_x = int(bomb["x"] // 64)
            tile_y = int(bomb["y"] // 64)

            if (
                0 <= tile_y < len(self.map)
                and
                0 <= tile_x < len(self.map[0])
            ):
                
                tile = self.map[tile_y][tile_x]

                if tile in ['1','2','3','4','5','6','7','8','9']:
                    bombs_to_remove.append(bomb)
                    continue

            if bomb["y"] > len(self.map) * 64 + 200:
                bombs_to_remove.append(bomb)
        
        for bomb in bombs_to_remove:

            if bomb in self.bombs:
                self.bombs.remove(bomb)
    
    def check_win(self):
        player_rect = pg.Rect(
            self.player_pos[0] + 40,
            self.player_pos[1] + 8,
            self.player_box_colider[0],
            self.player_box_colider[1]
        )

        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                if self.map[y][x] == 'F':
                    flag_rect = pg.Rect(x * 64, y * 64, 64, 64)

                    if player_rect.colliderect(flag_rect):
                        self.win = True

    def draw_win(self):
        dark = pg.Surface((1280, 768))
        dark.set_alpha(180)
        dark.fill((0, 0, 0))

        self.window.blit(dark, (0, 0))

        win_text = self.font.render(
            'VOCE VENCEU!',
            True,
            (255, 255, 255)
        )

        restart_text = self.font.render(
            'APERTE "R" PARA REINICIAR',
            True,
            (255, 255, 255)
        )

        self.window.blit(win_text, (400, 250))
        self.window.blit(restart_text, (250, 350))

    def player_idle(self):
        if self.player_animation_frame <= 7:
            self.window.blit(
                self.player_idle_1,
                (
                    self.player_pos[0] - self.camera_x,
                    self.player_pos[1] - self.camera_y
                )
            )
        elif self.player_animation_frame <= 14:
            self.window.blit(
                self.player_idle_2,
                (
                    self.player_pos[0] - self.camera_x,
                    self.player_pos[1] - self.camera_y
                )
            )
        elif self.player_animation_frame <= 21:
            self.window.blit(
                self.player_idle_3,
                (
                    self.player_pos[0] - self.camera_x,
                    self.player_pos[1] - self.camera_y
                )
            )
        elif self.player_animation_frame <= 28:
            self.window.blit(
                self.player_idle_4,
                (
                    self.player_pos[0] - self.camera_x,
                    self.player_pos[1] - self.camera_y
                )
            )
        elif self.player_animation_frame <= 35:
            self.window.blit(
                self.player_idle_5,
                (
                    self.player_pos[0] - self.camera_x,
                    self.player_pos[1] - self.camera_y
                )
            )
        self.player_animation_frame += 1
        if self.player_animation_frame > 35:
            self.player_animation_frame = 0

    def player_idle_left(self):
        if self.player_animation_frame <= 7:
            self.window.blit(self.player_idle_left_1, (
            self.player_pos[0] - self.camera_x,
            self.player_pos[1] - self.camera_y
        ))
        elif self.player_animation_frame <= 14:
            self.window.blit(self.player_idle_left_2, (
            self.player_pos[0] - self.camera_x,
            self.player_pos[1] - self.camera_y
        ))
        elif self.player_animation_frame <= 21:
            self.window.blit(self.player_idle_left_3, (
            self.player_pos[0] - self.camera_x,
            self.player_pos[1] - self.camera_y
        ))
        elif self.player_animation_frame <= 28:
            self.window.blit(self.player_idle_left_4, (
            self.player_pos[0] - self.camera_x,
            self.player_pos[1] - self.camera_y
        ))
        elif self.player_animation_frame <= 35:
            self.window.blit(self.player_idle_left_5, (
            self.player_pos[0] - self.camera_x,
            self.player_pos[1] - self.camera_y
        ))
        self.player_animation_frame += 1
        if self.player_animation_frame > 35:
            self.player_animation_frame = 0

    def player_right(self):
        if self.player_animation_frame <= 7:
            self.window.blit(self.player_right_1, (
            self.player_pos[0] - self.camera_x,
            self.player_pos[1] - self.camera_y
        ))
        elif self.player_animation_frame <= 14:
            self.window.blit(self.player_right_2, (
            self.player_pos[0] - self.camera_x,
            self.player_pos[1] - self.camera_y
        ))
        elif self.player_animation_frame <= 21:
            self.window.blit(self.player_right_3, (
            self.player_pos[0] - self.camera_x,
            self.player_pos[1] - self.camera_y
        ))
        elif self.player_animation_frame <= 28:
            self.window.blit(self.player_right_4, (
            self.player_pos[0] - self.camera_x,
            self.player_pos[1] - self.camera_y
        ))
        elif self.player_animation_frame <= 35:
            self.window.blit(self.player_right_5, (
            self.player_pos[0] - self.camera_x,
            self.player_pos[1] - self.camera_y
        ))
        elif self.player_animation_frame <= 42:
            self.window.blit(self.player_right_6, (
            self.player_pos[0] - self.camera_x,
            self.player_pos[1] - self.camera_y
        ))
        self.player_animation_frame += 1
        if self.player_animation_frame > 42:
            self.player_animation_frame = 0

    def player_left(self):
        if self.player_animation_frame <= 7:
            self.window.blit(self.player_left_1, (
            self.player_pos[0] - self.camera_x,
            self.player_pos[1] - self.camera_y
        ))
        elif self.player_animation_frame <= 14:
            self.window.blit(self.player_left_2, (
            self.player_pos[0] - self.camera_x,
            self.player_pos[1] - self.camera_y
        ))
        elif self.player_animation_frame <= 21:
            self.window.blit(self.player_left_3, (
            self.player_pos[0] - self.camera_x,
            self.player_pos[1] - self.camera_y
        ))
        elif self.player_animation_frame <= 28:
            self.window.blit(self.player_left_4, (
            self.player_pos[0] - self.camera_x,
            self.player_pos[1] - self.camera_y
        ))
        elif self.player_animation_frame <= 35:
            self.window.blit(self.player_left_5, (
            self.player_pos[0] - self.camera_x,
            self.player_pos[1] - self.camera_y
        ))
        elif self.player_animation_frame <= 42:
            self.window.blit(self.player_left_6, (
            self.player_pos[0] - self.camera_x,
            self.player_pos[1] - self.camera_y
        ))
        self.player_animation_frame += 1
        if self.player_animation_frame > 42:
            self.player_animation_frame = 0

    def player_collider(self):
        pos_x = self.player_pos[0] + 40
        pos_y = self.player_pos[1] + 8
        box = [[pos_x, pos_y],
                [pos_x + self.player_box_colider[0], pos_y],
                [pos_x, pos_y + self.player_box_colider[1]],
                [pos_x + self.player_box_colider[0], pos_y + self.player_box_colider[1]]]
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                if self.map[y][x] in ['1','2','3','4','5','6','7','8','9']:
                    for i in range(len(box)):
                        if x * 64 <= box[i][0] and y * 64 <= box[i][1] and (x * 64) + 64 >= box[i][0] and (y * 64) + 64 >= box[i][1]:
                            return True
        return False

    def player(self):
        self.player_vertical_speed += self.gravity
        self.player_pos[1] += self.player_vertical_speed
        if self.player_pos[1] > len(self.map) * 64 + 300:
            self.game_over = True
        if self.player_collider():
            self.player_pos[1] -= self.player_vertical_speed
            self.player_vertical_speed = 0
            self.on_ground = True
        else:
            self.on_ground = False
        if self.player_animation == 0:
            self.player_idle()
        if self.player_animation == 1:
            self.player_idle_left()
        if self.player_animation == 2:
            self.player_right()
        if self.player_animation == 3:
            self.player_left()

    def camera(self):
        map_width = len(self.map[0]) * 64
        map_height = len(self.map) * 64

        self.camera_x = self.player_pos[0] - 640
        self.camera_y = self.player_pos[1] - 384

        if self.camera_x < 0:
            self.camera_x = 0

        if self.camera_y < 0:
            self.camera_y = 0

        if self.camera_x > map_width - 1280:
            self.camera_x = map_width - 1280

        if self.camera_y > map_height - 768:
            self.camera_y = map_height - 768

    def move(self, array, key):

        if self.game_over or self.win:
            return
        
        buttom_press = False

        # Right
        if array[100] == True:
            self.player_pos[0] += 5
            if self.player_collider():
                self.player_pos[0] -= 5
            else:
                self.player_animation = 2
                buttom_press = True

        # Left
        if array[97] == True:
            self.player_pos[0] -= 5
            if self.player_collider():
                self.player_pos[0] += 5
            else:
                self.player_animation = 3
                buttom_press = True

        if buttom_press == False and self.player_animation == 2:
            self.player_animation = 0
        elif buttom_press == False and self.player_animation == 3:
            self.player_animation = 1

        map_width = len(self.map[0]) * 64
        map_height = len(self.map) * 64

        if self.player_pos[0] < 0:
            self.player_pos[0] = 0

        if self.player_pos[0] > map_width - 128:
            self.player_pos[0] = map_width - 128

        if self.player_pos[1] < 0:
            self.player_pos[1] = 0

        if key == 'space' and self.on_ground:
            self.player_vertical_speed = self.player_jump_force
            
    def draw_game_over(self):

        dark = pg.Surface((1280, 768))
        dark.set_alpha(180)
        dark.fill((0, 0, 0))

        self.window.blit(dark, (0, 0))

        game_over_text = self.font.render(
            'GAME OVER',
            True,
            (255, 255, 255)
        )

        restart_text = self.font.render(
            'APERTE "R" PARA REINICIAR',
            True,
            (255, 255, 255)
        )

        self.window.blit(game_over_text, (430, 250))
        self.window.blit(restart_text, (250, 350))
        


jogo = TreasureHunters()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            if (jogo.game_over or jogo.win) and pg.key.name(event.key) == 'r':
                jogo = TreasureHunters()
            jogo.move(pg.key.get_pressed(), pg.key.name(event.key))
            if pg.key.name(event.key) == 'escape':
                pg.quit()
                quit()

    # Mouse info
    mouse_position  = pg.mouse.get_pos()
    mouse_input = pg.mouse.get_pressed()
    mouse_click = jogo.mouse_has_clicked(mouse_input)
    mouse = (mouse_position, mouse_input, mouse_click)

    # Game
    jogo.clock.tick(60)
    jogo.move(pg.key.get_pressed(), '')
    jogo.camera()
    jogo.background_imgs()
    jogo.tiles()
    jogo.bomb_manager()
    jogo.draw_bomb_warnings()
    jogo.update_bombs()
    jogo.draw_bombs()
    jogo.draw_coins()

    if not jogo.game_over and not jogo.win:
        jogo.player()
        jogo.collect_coins()
        jogo.check_win()

    if jogo.game_over:
        jogo.draw_game_over()

    if jogo.win:
        jogo.draw_win()

    jogo.last_click_status = mouse_input

    pg.display.update()
import pygame
import os
import time
from shutil import copyfile
from PIL import Image  


# pygame.init()
# screen = pygame.display.set_mode([500, 500])

app_path = os.path.dirname(os.path.realpath(__file__))

# dir_path = os.path.dirname(os.path.realpath(__file__))
window_h = 700
window_w = 1200
# dir_path = "/media/kuba-ubuntu/E46216A86216800A/Zdjęcia"
folder = "out"
dir_path = "E:\Conv_Zdjęcia"
conv_param = 5

def convert_photo(folder):
    images_path = dir_path + "/" + folder
    files_list = os.listdir(images_path)
    for img_name in files_list:
        path_to_image = os.path.join(images_path, img_name)
        image = Image.open(path_to_image)  
        width, height = image.size  
        newsize = (int(width/conv_param), int(height/conv_param))
        image = image.resize(newsize)
        print(width, height) 
        print(newsize)
        path_to_out = f"E:\Conv_Zdjęcia\{folder}"
        path_to_out = os.path.join(path_to_out, img_name)
        image.save(path_to_out, "JPEG")


class App:
    def __init__(self, window_w, window_h):
        self.running = True
        self.window_h = window_h
        self.window_w = window_w
        self.window = None
        self.position = 0
        self.picture_number = 0
        self.img = None
        self.path_to_image = None

    def on_init(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.window_w, self.window_h), pygame.HWSURFACE)
        pygame.display.set_caption("The Picture")
        self.running = True
        self.get_files()

    def get_files(self):
        previous_img_folder = folder
        images_path = dir_path + "/" + previous_img_folder
        files_list = os.listdir(images_path)
        self.picture_number = len(files_list)
        picture_name = files_list[self.position]
        self.path_to_image = os.path.join(images_path, picture_name)
        self.img = pygame.image.load(self.path_to_image)
        self.window.fill((255, 255, 255))
        self.window.blit(self.img, (0, 0))
        pygame.display.flip()
        # new_picture_name = previous_img_folder + "_" + picture_name
        new_picture_name = picture_name
        dst_directory = dir_path + "\\" + "album"
        self.path_to_out = os.path.join(dst_directory, new_picture_name)

    def on_execute(self):
        self.on_init()

        if not self.on_init:
            self.running = False

        while self.running:
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if keys[pygame.K_RIGHT]:
                if self.position + 1 < self.picture_number:
                    self.position += 1
                time.sleep(0.1)
                # print(self.position)
            if keys[pygame.K_LEFT]:
                if self.position - 1 >= 0:
                    self.position -= 1
                time.sleep(0.1)

            if keys[pygame.K_TAB]:
                copyfile(self.path_to_image, self.path_to_out)
                # font_path = app_path + "\\" + "AGENCYR.TTF"
                # myfont = pygame.font.SysFont(pygame.font.get_default_font(), 50)
                # textsurface = myfont.render('Copied !', True, (240, 255, 255))
                # self.window.blit(textsurface,(50,50))
                # pygame.display.flip()

                time.sleep(0.1)

            if (keys[pygame.K_ESCAPE]):
                self.running = False

            if self.picture_number > self.position >= 0:
                self.get_files()


if __name__ == "__main__":
    theApp = App(window_w, window_h)
    theApp.on_execute()

    # folders = os.listdir(dir_path)
    # for folder in folders:
    #     convert_photo(folder)

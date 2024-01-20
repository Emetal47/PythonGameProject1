import pygame as pg


class Camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def apply(self, target):
        return target.rect.move(self.width // 2, self.height // 2)

    def update(self, target):
        # Adjust the camera to follow the target (player)
        camera_x = -target.rect.x + self.width // 2
        camera_y = -target.rect.y + self.height // 2

        # Clamp camera position to prevent it from going beyond the game boundaries
        camera_x = min(0, camera_x)
        camera_y = min(0, camera_y)

        # You can add additional logic here based on your game's requirements

        self.camera = (camera_x, camera_y)

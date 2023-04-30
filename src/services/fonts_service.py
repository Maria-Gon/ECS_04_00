import pygame


class FontsService:
    def __init__ (self) -> None:
        self._font = {}

    def get(self, path: str, size: int) -> pygame.font.Font:
        if path not in self._font:
            self._font[path] = pygame.font.Font(path, size)
        return self._font[path]

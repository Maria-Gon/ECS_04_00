import pygame
import esper
from src.create.prefab_creator import create_text_special
from src.ecs.components.c_surface import CSurface
from src.ecs.components.tags.c_tag_score import CTagScore
from src.engine.service_locator import ServiceLocator


def system_loading_bar(world: esper.World, num: int, text_info: dict, path: str):
    components = world.get_components(CSurface, CTagScore)
    font = ServiceLocator.fonts_service.get(path, text_info["size"])
    for score_entity, (c_s, c_) in components:
        color = (text_info["color"]["r"],text_info["color"]["g"],text_info["color"]["b"])
        if num != 100:
            color = (255,0,0)
        surf =font.render(str(num)+"%", True, pygame.Color(color))
        c_s.surf = surf
        c_s.area = surf.get_rect()
    


    
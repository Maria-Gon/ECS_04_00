
import pygame
import esper
from src.create.prefab_creator import create_bullet_special
from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_tag_bullet import CTagBullet


def system_bullet_special(world: esper.World, bullet_info: dict):
    components_bullet = world.get_components(CTransform, CTagBullet)

    for bullet_entity, (c_b_t, b_t) in components_bullet:
        if (b_t.bullet_type == "Basic"):
            create_bullet_special(world, c_b_t.pos, pygame.Vector2(-100,-100), bullet_info)
            create_bullet_special(world, c_b_t.pos, pygame.Vector2(100,100), bullet_info)
            create_bullet_special(world, c_b_t.pos, pygame.Vector2(-100,100), bullet_info)
            create_bullet_special(world, c_b_t.pos, pygame.Vector2(100,-100), bullet_info)
            world.delete_entity(bullet_entity)
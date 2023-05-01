import pygame
import esper
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.tags.c_tag_bullet import CTagBullet


def system_kill_special(world: esper.World):
    components = world.get_components( CTagBullet)
    for bullet_entity, ( b_t) in components:
        world.delete_entity(bullet_entity)
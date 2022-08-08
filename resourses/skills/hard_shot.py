from resourses.skills.base_skill import BaseSkill


class HardShot(BaseSkill):
    """Concrate skill instace"""
    name = "Сильный удар"
    stamina_required = 3.0
    damage = 3.0

    def skill_effect(self) -> str:
        self.user.stamina_points_ -= self.stamina_required
        self.target.health_points_ -= self.damage
        return f"{self.user.name} применил умение {self.name} и нанес {self.damage} урона по {self.target.name}"

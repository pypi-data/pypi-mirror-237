import random

from autonomous import log

from dmtoolkit.models.ttrpgobject import TTRPGObject


class Encounter(TTRPGObject):
    LOOT_MULTIPLIER = 3
    attributes = TTRPGObject.attributes | {
        "difficulty": "",
        "enemies": [],
        "loot": [],
    }
    difficulty_list = [
        "trivial",
        "easy",
        "medium",
        "hard",
        "deadly",
    ]
    loot_types = [
        "currency",
        "valuables",
        "trinkets",
        "junk",
        "weapon",
        "armor",
    ]
    funcobj = {
        "name": "generate_encounter",
        "description": "Generate an Encounter object",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The title of the encounter",
                },
                "backstory": {
                    "type": "string",
                    "description": "The backstory of the encounter",
                },
                "desc": {
                    "type": "string",
                    "description": "A physical description of the scene the characters come upon to start the encounter",
                },
                "loot": {
                    "type": "array",
                    "description": "Loot gained from the encounter",
                    "items": {"type": "string"},
                },
                "enemies": {
                    "type": "array",
                    "description": "A list of enemies faced in the encounter",
                    "items": {"type": "string"},
                },
            },
        },
    }

    def get_image_prompt(self):
        description = self.desc or "shadowy figures"
        return f"A full color illustrated image of fictional characters preparing for battle. Additional details:  {description}"

    @classmethod
    def generate(cls, world, num_players=5, level=1):
        primer = f"""
        You are a {world.genre} TTRPG Encounter generator that creates level appropriate random encounters and specific loot rewards.
        """
        difficulty = random.choice(list(enumerate(cls.difficulty_list)))
        loot_type = random.choices(
            cls.loot_types,
            weights=[10, 5, 3, 30, 10, 10],
            k=(difficulty[0] * cls.LOOT_MULTIPLIER) + 1,
        )
        prompt = f"""Generate an {world.genre} TTRPG encounter for the following:
        - Occurs in a world with the following description:{world.desc}
        - a party of {num_players} at level {level} 
        - Difficulty: {difficulty[1]} 
        - Type of loot items: {loot_type} 
        """
        encounter = super().generate(primer, prompt)
        encounter |= {"difficulty": difficulty[1], "world": world}
        encounter = Encounter(**encounter)
        encounter.save()
        return encounter

    def page_data(self, root_path="ttrpg"):
        return {
            "Details": [
                f"difficulty: {self.difficulty}",
                {
                    "enemies": [
                        f"[{r.name}]({r.page_path(root_path)})" for r in self.enemies
                    ]
                },
                {"loot": self.loot},
            ],
        }

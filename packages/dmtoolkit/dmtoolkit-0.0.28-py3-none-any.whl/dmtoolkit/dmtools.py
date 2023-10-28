from autonomous import log
from autonomous.apis.wikijs import WikiJS
from autonomous.auth.user import AutoUser

from dmtoolkit.models.world import World


def generator(world):
    log(world)
    pk = world.save()
    log(pk)
    world.generate(region=1, location=3, city=2, faction=2)
    pk = world.save()
    log(pk, world)
    res = world.canonize(root_path="ttrpg/swn")
    log(res)


if __name__ == "__main__":
    ws = World(
        genre="sci-fi",
        user=AutoUser(),
        desc="A small sector of the galaxy under the tenuous rule of the the militaristic Red Sun Dominion",
        name="Red Sun Dominion",
        backstory="150 years after Humanity rediscovers interstellar travel following a great cataclysm that decimated human civilization across the entire galaxy, the Red Sun Dominion has gained a tenuous hold over a small sector of the galaxy.",
    )
    ws.save()
    generator(ws)

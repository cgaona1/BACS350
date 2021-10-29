from .models import Hero

# CREATE
def add_hero(name, description):
    return Hero.objects.create(hero_name=name, hero_description=description)

# READ - list
def list_heroes():
    return Hero.objects.all()

# READ - Get
def get_hero(pk):
    return Hero.objects.get(pk=pk)


def get_hero_name(pk):
    name = get_hero(pk).hero_name
    return name


def get_hero_description(pk):
    description = get_hero(pk).hero_description
    return description

# UPDATE
def set_hero_name(pk, name):
    hero = get_hero(pk)
    hero.hero_name = name
    hero.save()

# DELETE
def delete_hero(pk):
    Hero.objects.get(pk=pk).delete()

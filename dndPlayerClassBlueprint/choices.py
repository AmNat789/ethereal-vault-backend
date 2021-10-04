from django.db import models
from enum import Enum, auto


class Choices(Enum):
    @classmethod
    def get_tuple(cls):
        return tuple((i.name, i.value) for i in cls)


class Attribute(Choices):
    STR = "Strength"
    DEX = "Dexterity"
    CON = "Constitution"
    INT = "Intelligence"
    WIS = "Wisdom"
    CHA = "Charisma"


class MagicType(Choices):
    SPELL = "Spell"
    CANTRIP = "Cantrip"


class SchoolOfMagic(Choices):
    CONJURATION = "Conjuration"
    NECROMANCY = "Necromancy"
    EVOCATION = "Evocation"
    ABJURATION = "Abjuration"
    TRANSMUTATION = "Transmutation"
    DIVINATION = "Divination"
    ENCHANTMENT = "Enchantment"
    ILLUSION = "Illusion"


class DamageType(Choices):
    ACID = "Acid"
    BLUDGEONING = "Bludgeoning"
    COLD = "Cold"
    FIRE = "Fire"
    FORCE = "Force"
    LIGHTNING = "Lightning"
    NECROTIC = "Necrotic"
    PIERCING = "Piercing"
    POISON = "Poison"
    RADIANT = "Radiant"
    SLASHING = "Slashing"
    THUNDER = "Thunder"

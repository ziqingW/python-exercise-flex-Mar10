class Aura:
    def __init__(self, name, end):
        self.name = name
        self.begin = 0
        self.end = end
        
auraNormal = Aura("normal", 0)
auraSlowed = Aura("slowed", 2)
auraBlessed = Aura("blessed", 10)
auraEnraged = Aura("enraged", 2)
auraCorrupted = Aura("corrupted", 2)
auraSwapped = Aura("swapped", 1)
auraParalyzed = Aura("paralyzed", 2)
auraProtected = Aura("protected", 3)
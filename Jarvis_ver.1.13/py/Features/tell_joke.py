import pyjokes
from talk import talk

joke = (pyjokes.get_joke())
print("\n\n" + joke)
talk("OK." + joke)
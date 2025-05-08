import sys

def attr_demo():
    class Obj:
        def __init__(self):
            self.val = 10
    o = Obj()
    return o.val

attr_demo()
print("\nSpecialization stats (may require Python 3.11+):")
try:
    print(sys._get_specialization_stats())
except AttributeError:
    print("Specialization stats not available (needs Python 3.11+)")

# =====================================
# 7. When Frame Knowledge Helps or Hurts
# =====================================
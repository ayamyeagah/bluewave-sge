import random

def power():
    kWh = round(random.uniform(8,12), 2)
    kVAR = round(random.uniform(8,12), 2)
    Hz = round(random.uniform(50,60), 2)

    return [kWh, kVAR, Hz]
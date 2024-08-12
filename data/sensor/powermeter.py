import random

def power():
    kWh = round(random.uniform(12,24), 2)
    kVAR = round(random.uniform(12,24), 2)
    Hz = round(random.uniform(12,24), 2)

    return [kWh, kVAR, Hz]
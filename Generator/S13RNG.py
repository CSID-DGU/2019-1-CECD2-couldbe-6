import hashlib
import time

Dmodular = 2147483647    # Default modular
Dseed = 0    # Default seed

# S13RNG class
class S13RNG(object):
    def __init__(self, rng_modular = Dmodular, rng_seed = Dseed):
        self.rng_modular = Dmodular
        self.rng_seed = Dseed

# Return Current Seed
    def current_seed(self):
        return self.rng_seed

# Return Current Modular
    def current_modular(self):
        return self.rng_modular

# Set Seed
    def seed(self, new_seed):
        self.rng_seed = new_seed

# Set Modular
    def modular(self, new_modular):
        self.rng_modular = new_modular

# Run Random and Generate Random Number
    def random(self):
        input = str(self.rng_seed)
        sha = hashlib.new('sha1')
        sha.update(input.encode())
        exec = sha.hexdigest()
        execa = exec + exec[:20]
        sha.update(execa.encode())
        exec1 = sha.hexdigest()
        execi = int(exec1, 16)
        execb = exec1 + exec[20:40]
        sha.update(execb.encode())
        exec2 = sha.hexdigest()
        execi = int(exec2, 16)
        self.rng_seed = self.rng_seed + 1
        return execi % self.rng_modular
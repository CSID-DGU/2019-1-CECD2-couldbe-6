import hashlib
import time

Dmodular = 2147483647    # Default modular
Dcounter = 0    # Default counter

class S13RNG(object):
    def __init__(self, rng_modular = Dmodular, rng_counter = Dcounter):
        self.rng_modular = Dmodular
        self.rng_counter = Dcounter

    def current_counter(self):
        return self.rng_counter

    def counter(self, new_counter):
        self.rng_counter = new_counter

    def modular(self, new_modular):
        self.rng_modular = new_modular

    def random(self):
        input = str(self.rng_counter)
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
        self.rng_counter = self.rng_counter + 1
        return execi % self.rng_modular
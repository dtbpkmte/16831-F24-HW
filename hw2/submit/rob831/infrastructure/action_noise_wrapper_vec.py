import numpy as np
from gym.vector import VectorEnvWrapper


class ActionNoiseWrapperVec(VectorEnvWrapper):
    def __init__(self, env, seed, std):
        super().__init__(env)
        self.rng = np.random.default_rng(seed)
        self.std = std

    def step_async(self, actions):
        noisy_actions = actions + self.rng.normal(0, self.std, actions.shape)
        self.env.step_async(noisy_actions)

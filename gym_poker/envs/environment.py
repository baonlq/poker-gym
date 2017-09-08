from io import StringIO
import sys
import time

import gym
from gym import error, spaces, utils
from gym.utils import seeding

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import numpy as np


class PokerEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(PokerEnv, self).__init__()
        self._action_space = spaces.Discrete(98)
        self.driver = webdriver.Chrome()

    def _reset(self):
        self.driver.get("http://103.68.82.34/p/")

    def _close(self):
        self.driver.close()
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
        self.driver = webdriver.Chrome()

    def _step(self, action):
        pass

    def _reset(self):
        self.driver.get("http://103.68.82.34/p/")

    def _render(self, mode='human', close=False):
        pass

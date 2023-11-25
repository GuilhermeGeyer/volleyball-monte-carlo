# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 19:58:54 2023

@author: user
"""

from random import random


class Player():
    def __init__(self, success_chance, score, name):
        self.success_chance = success_chance
        self.score = score
        self.name = name
        self.starting_score = score

    def reset(self):
        self.score = self.starting_score


class Match():
    def __init__(self, player_1, player_2, current_player):
        self.player_1 = player_1
        self.player_2 = player_2
        self.current_player = current_player

    def change_player(self):
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1

    def new_point(self):
        if random() < self.current_player.success_chance:
            self.current_player.score += 1
        else:
            self.change_player()
            self.current_player.score += 1

    def print_score(self):
        print('Score:')
        print(f'{self.player_1.name} {self.player_1.score} x ' +
              f'{self.player_2.score} {self.player_2.name}')

    def is_ongoing(self):
        if self.player_1.score > 24:
            if self.player_2.score < 24:
                return False
            if abs(self.player_1.score - self.player_2.score) < 2:
                return True
            return False
        if self.player_2.score > 24:
            if abs(self.player_1.score - self.player_2.score) < 2:
                return True
            return False
        return True

    def reset(self):
        self.player_1.reset()
        self.player_2.reset()


class Series():
    def __init__(self, match):
        self.match = match
        self.total_matches = 0
        self.score_1 = 0
        self.score_2 = 0

    def print_score(self):
        if self.total_matches == 0:
            print('None')
        else:
            print(f'{round(100 * self.score_1 / self.total_matches,2)} % x ' +
                  f'{round(100 * self.score_2 / self.total_matches,2)} %')
            print(f'{match.player_1.name} x {match.player_2.name}')

    def match_ended(self):
        if self.match.player_1.score > self.match.player_2.score:
            self.score_1 += 1
        else:
            self.score_2 += 1
        self.total_matches += 1
        match.reset()


current_score = [int(i) for i in '23 20'.split(' ')]

p1 = Player(0.5, current_score[0], 'p1')
p2 = Player(0.5, current_score[1], 'p2')
match = Match(p1, p2, p1)
series = Series(match)

while series.total_matches < 100000:
    while match.is_ongoing():
        match.new_point()
    series.match_ended()
series.print_score()

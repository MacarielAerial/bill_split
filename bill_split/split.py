'''
This script triggers computations on individual bill amount based on informatiton from data.py within the same directory
'''

import os
from pathlib import Path
from fractions import Fraction

class Split():
        def __init__(self, ppl_dish, dish_p, output_f_name = 'Output.txt'):
            # Store input variables locally
            self.ppl_dish, self.dish_p = ppl_dish, dish_p
            self.output_f_name = output_f_name
            # Initiate an empty dictionary to store final output amounts
            self.output_amount = dict(zip(list(self.ppl_dish.keys()), [0] * len(list(self.ppl_dish.keys()))))
            # Calculate everyone's payment amount
            self.calculate()
            # Clean previous application output if any
            self.clean_previous_output()

        def calculate(self):
            '''
            Calculate everyone's calculated final payment amount
            '''
            for person in self.ppl_dish:
                for dish in self.ppl_dish[person]:
                    self.output_amount[person] = self.output_amount[person] + self.dish_p[dish] * self.ppl_dish[person][dish]

        def display_final(self):
            '''
            Display everyone's calculated final payment amount
            '''
            with open(Path.cwd().joinpath(self.output_f_name), 'a+') as f:
                print('Here\'s everyone\'s final amount:', file = f)
                for person in self.output_amount:
                    print(person + ': ' + str(
                                             round(
                                                  self.output_amount[person], 2)
                                                  ),
                                             file = f
                                             )
                print('\n', end = '', file = f)

        def display_individual(self):
            '''
            Display individual dishes ordered by persons
            '''
            with open(Path.cwd().joinpath(self.output_f_name), 'a+') as f:
                print('Here\'s dishes that each person ordered:', file = f)
                for person in self.ppl_dish:
                    print(person + ':', file = f)
                    for dish in self.ppl_dish[person]:
                        print(str(Fraction(self.ppl_dish[person][dish]).limit_denominator()) + ' ' + dish, file = f)
                    print('\n', end = '', file = f)

        def clean_previous_output(self):
            if os.path.exists(Path.cwd().joinpath(self.output_f_name)):
                os.remove(Path.cwd().joinpath(self.output_f_name))

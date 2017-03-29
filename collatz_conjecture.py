#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 15:33:25 2017

@author: lucfrachon
"""
import numpy as np
import matplotlib.pyplot as plt

def collatz(num):
    
    
    if num % 2 == 0:
        num /= 2
    else:
        num *= 3
        num += 1
    return num
    
    
def run_collatz(start):
    numbers = [start]
    num = start
    it = 0
    
    while num > 1:
        num = collatz(num)
        numbers.append(num)
        it += 1
    return numbers

if __name__ == '__main__':    

    highest_number = int(input('Highest number to sample from: '))
    num_sample = int(input('How many numbers do you want to try? '))
    sample = np.random.randint(1, highest_number, size = num_sample)          
    lines = []

    for num in sample:
        print("Trying ", num)
        numbers = run_collatz(num)
        plt.plot(numbers, label = str(num), alpha = .3)
    plt.yscale('log')
    plt.title("Collatz Conjecture")
    plt.legend(loc = 'upper right', fontsize = 'xx-small')
    

    
        

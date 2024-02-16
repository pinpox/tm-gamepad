#!/usr/bin/env nix-shell
#!nix-shell -I nixpkgs=channel:nixpkgs-unstable -i python3 -p "python3.withPackages (ps: with ps; [ matplotlib numpy ])"


import numpy as np
import matplotlib.pyplot as plt

def read_values_from_file(file_path):
    values = np.loadtxt(file_path)
    return values

def plot_values(values):
    plt.plot(values, marker='o', linestyle='-', color='b')
    plt.title('Values from Text File')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    file_path = "values.csv"  # Replace with the path to your text file
    values = read_values_from_file(file_path)
    plot_values(values)

import matplotlib.pyplot as plt

def collatz_conjecture(n):
    sequence = [n]

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)

    return sequence

def plot_collatz_sequence(sequence):
    x = range(len(sequence))

    plt.plot(x, sequence, marker='o', linestyle='-')
    plt.title('Collatz Conjecture Sequence')
    plt.xlabel('Step')
    plt.ylabel('Value')
    plt.grid(True)
    plt.show()
import matplotlib.pyplot as plt
import numpy as np
import seaborn

if __name__ == '__main__':

    csvfile = '../log/large_3072.csv'

    plt.clf()
    #plt.style.use('ggplot')
    plt.xlabel('Epoch', fontsize=15)
    plt.ylabel('Accuracy', fontsize=15)
    plt.rcParams['xtick.labelsize'] = 18
    plt.rcParams['ytick.labelsize'] = 18

    accs = np.genfromtxt(csvfile, delimiter=',')
    accs = np.delete(accs, 0, 0)

    epoch = accs[:, 0]
    accuracy = accs[:, 3]

    plt.xlim([0, 850])

    plt.plot(epoch, accuracy, color='black')

    plt.savefig("graph_7_emos_accuracy.png", dpi=500, bbox_inches="tight")


from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc('font', size=18)
machines = ['MLP', 'RBM', 'SAE', 'DAE']
accuracy = [80.2741, 80.2608, 79.1519, 76.9251]
width = 0.4
ind = np.arange(len(machines))

fig, ax = plt.subplots()
rects = ax.bar(ind, accuracy, width, color='b')
ax.set_ylabel('Accuracy(%)')
ax.set_xlabel('Classifiers')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(machines)
ax.set_xlim([-0.5, len(machines)])
ax.set_ylim([70, 82])
plt.grid()


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.005*height,
                '%.2f' % height, ha='center', va='bottom')

autolabel(rects)
plt.tight_layout()
plt.savefig('comp_accuracy.pdf', fmt='pdf')
plt.show()

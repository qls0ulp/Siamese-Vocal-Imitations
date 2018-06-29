import os
import time

import matplotlib.pyplot as plt
import numpy as np


def mrr_per_epoch(train_mrrs, val_mrrs, train_var=None, val_var=None, title="MRR vs. Epoch"):
    plt.errorbar(np.arange(len(train_mrrs)), train_mrrs, yerr=train_var, color='blue', label='train', capsize=5, errorevery=3)
    plt.errorbar(np.arange(len(val_mrrs)), val_mrrs, yerr=val_var, color='orange', label='validation', capsize=5, errorevery=3)
    plt.legend()
    plt.ylabel('MRR')
    plt.xlabel('epoch')
    plt.title(title)
    title = title_to_filename(title)
    plt.savefig(title)
    plt.close()


def loss_per_epoch(losses, var, title="Loss vs. Epoch"):
    plt.plot(losses, color='blue', label='train')
    plt.errorbar(np.arange(len(losses)), losses, yerr=var, capsize=5, errorevery=5)
    plt.legend()
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.title(title)
    title = title_to_filename(title)
    plt.savefig(title)
    plt.close()


def title_to_filename(title):
    title = title.replace(' ', '_')
    title = title.replace('.', '')
    title += '_{0}.png'.format(time.time())
    title = title.lower()
    return os.path.join('./graphs', title)
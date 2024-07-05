import numpy as np
import awkward as ak
import hist
from matplotlib import pyplot as plt
import mplhep as hep

from samples import samples, d_samples
from vars import vars, d_vars

hep.style.use(hep.style.ROOT)

def determine_bins(data) -> tuple[int, int]:
    '''Determine the binning for a given data set.
    '''

    x_min = min([ak.min(a) for a in data])
    x_max = max([ak.max(a) for a in data])

    # Can add outlier finding here...

    return x_min, x_max

def make_plot(inputs: dict, name: str, n_bins=25, xlabel: str = '', ylabel: str = 'Events', logy: bool = False):
    plt.clf()
    processes = [s.process for s in samples]
    
    x_min, x_max = determine_bins(inputs.values())

    if x_min == x_max:
        print('Skipping', name, 'because either empty or constant', len(inputs.values()))
        return

    c_ax = hist.axis.StrCategory(processes, name='cat', label='Process')    
    ax = hist.axis.Regular(n_bins, x_min, x_max, flow=False, name='x', label=d_vars[name].title)
    cat_hists = hist.Hist(ax, c_ax)
    for label, data in inputs.items():
        cat_hists.fill(x=data, cat=d_samples[label].process)

    stack = cat_hists.stack('cat')
    stack[::-1].plot(stack=True, histtype='fill')
    plt.legend()
    # plt.show()
    plt.savefig(f'plots/{name}.png')



if __name__ == '__main__':
    distributions = np.load('distributions.npz', allow_pickle=True)['arr_0'].item()
    for label in distributions[samples[0].name].keys():
        make_plot({k: v[label] for k, v in distributions.items()}, label, n_bins=25, xlabel=label)

    

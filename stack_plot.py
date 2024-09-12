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

def make_plot(inputs: dict, name: str, n_bins=25, xlabel: str = '', ylabel: str = 'Events', logy: bool = False, lumi: float = 1.0):
    plt.clf()
    processes = list(set([s.process for s in samples]))
    
    x_min, x_max = determine_bins(inputs.values())

    if x_min == x_max:
        print('Skipping', name, 'because either empty', len(inputs.values()), 'or constant', x_min, x_max)
        return

    c_ax = hist.axis.StrCategory(processes, name='cat', label='Process')    
    ax = hist.axis.Regular(n_bins, x_min, x_max, flow=False, name='x', label=d_vars[name].title)
    cat_hists = hist.Hist(ax, c_ax)
    data_hist = hist.Hist(ax)
    for label, events in inputs.items():
        if 'data' in d_samples[label].name:
            data_hist.fill(x=events)
            continue
        weight = lumi*d_samples[label].xsec/d_samples[label].n_ev_produced*ak.ones_like(events)
        cat_hists.fill(x=events, cat=d_samples[label].process, weight=weight)

    stack = cat_hists.stack('cat')
    stack[::-1].plot(stack=True, histtype='fill')
    # data_hist.plot(histtype='errorbar')
    plt.legend()
    # plt.show()
    plt.savefig(f'plots/{name}.png')



if __name__ == '__main__':
    in_dir = '/Users/jan/cernbox/snd_plot/'
    distributions = {d.name: np.load(f'{in_dir}distributions_{d.name}.npz', allow_pickle=True)['arr_0'].item() for d in samples}
    for label in distributions[samples[0].name].keys():
        make_plot({k: v[label] for k, v in distributions.items()}, label, n_bins=25, xlabel=label)

    

import numpy as np
import awkward as ak
import hist
from matplotlib import pyplot as plt
import mplhep as hep

from samples import samples, d_samples

hep.style.use(hep.style.ROOT)


x_label_dict = {
    'n_hits_total':'Number of total hits',
    'n_hits_scifi':'Number of scifi hits',
    'n_hits_us':'Number of us hits',
    'n_hits_ds':'Number of ds hits',
    'n_hits_veto':'Number of veto hits',
    'n_hits_veto_0':'Number of veto_0 hits',
    'n_hits_veto_1':'Number of veto_1 hits',
    'n_hits_scifi_1':'Number of scifi_1 hits',
    'n_hits_scifi_2':'Number of scifi_2 hits',
    'n_hits_scifi_3':'Number of scifi_3 hits',
    'n_hits_scifi_4':'Number of scifi_4 hits',
    'n_hits_scifi_5':'Number of scifi_5 hits',
    'n_scifi_layers':'Number of SciFi layers hits',
    'n_hits_scifi_vertical':'Number of vertical SciFi hits',
    'n_hits_us_vertical':'Number of vertical US hits',
    'n_hits_ds_vertical':'Number of vertical DS hits',
    'n_hits_scifi_horizontal':'Number of horizontal SciFi hits',
    'n_hits_us_horizontal':'Number of horizontal US hits',
    'n_hits_ds_horizontal':'Number of horizontal DS hits',
}

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
    ax = hist.axis.Regular(n_bins, x_min, x_max, flow=False, name='x', label=x_label_dict[name])
    cat_hists = hist.Hist(ax, c_ax)
    for label, data in inputs.items():
        cat_hists.fill(x=data, cat=d_samples[label].process)

    stack = cat_hists.stack('cat')
    stack[::-1].plot(stack=True, histtype='fill')
    plt.legend()
    # plt.show()
    plt.savefig(f'plots/{name}.png')



if __name__ == '__main__':
    distributions = np.load('distributions.npy', allow_pickle=True).item()
    for label in distributions[samples[0].name].keys():
        make_plot({k: v[label] for k, v in distributions.items()}, label, n_bins=25, xlabel=label)

    

import numpy as np
import awkward as ak
import hist
from matplotlib import pyplot as plt
import mplhep as hep

from samples import samples

hep.style.use(hep.style.ROOT)

def load_sample(sample, replace='targets'):
    arrays = []
    for file in sample.get_files():
        hits = ak.from_parquet(file)
        if sample.class_select >= 0:
            targets = ak.from_parquet(file.replace('hits', replace))
            hits = hits[targets.pdg == sample.class_select]
            del targets
        arrays.append(hits)

    return ak.concatenate(arrays)

def calculate_input_vars(data) -> dict:
    '''Produces various distributions for a given sample.
    '''

    vars = {}

    # Per-event variables
    vars['n_hits_total'] = ak.count(hits.det, axis=1)
    vars['n_hits_scifi'] = ak.count(hits.det[hits.det == 1], axis=1)
    vars['n_hits_us'] = ak.count(hits.det[hits.det == 2], axis=1)
    vars['n_hits_ds'] = ak.count(hits.det[hits.det == 3], axis=1)

    vars['n_hits_veto'] = ak.count(hits.det[(hits.det == 1) & (hits.strip_z < 290.)], axis=1)

    vars['n_hits_veto_0'] = ak.count(hits.det[(hits.det == 1) & (hits.strip_z < 285.)], axis=1)
    vars['n_hits_veto_1'] = ak.count(hits.det[(hits.det == 1) & (hits.strip_z > 285.) & (hits.strip_z < 290.)], axis=1)

    vars['n_hits_scifi_1'] = ak.count(hits.det[(hits.det == 1) & (hits.strip_z > 295.) & (hits.strip_z < 305.)], axis=1)
    vars['n_hits_scifi_2'] = ak.count(hits.det[(hits.det == 1) & (hits.strip_z > 310.) & (hits.strip_z < 320.)], axis=1)
    vars['n_hits_scifi_3'] = ak.count(hits.det[(hits.det == 1) & (hits.strip_z > 320.) & (hits.strip_z < 330.)], axis=1)
    vars['n_hits_scifi_4'] = ak.count(hits.det[(hits.det == 1) & (hits.strip_z > 335.) & (hits.strip_z < 345.)], axis=1)
    vars['n_hits_scifi_5'] = ak.count(hits.det[(hits.det == 1) & (hits.strip_z > 350.) & (hits.strip_z < 360.)], axis=1)

    vars['n_scifi_layers'] = np.int32(vars['n_hits_scifi_1']) + vars['n_hits_scifi_2'] + vars['n_hits_scifi_3'] + vars['n_hits_scifi_4'] + vars['n_hits_scifi_5']


    vars['n_hits_scifi_vertical'] = ak.count(hits.det[(hits.det == 1) & (hits.vertical == 1)], axis=1)
    vars['n_hits_us_vertical'] = ak.count(hits.det[(hits.det == 2) & (hits.vertical == 1)], axis=1)
    vars['n_hits_ds_vertical'] = ak.count(hits.det[(hits.det == 3) & (hits.vertical == 1)], axis=1)
    vars['n_hits_scifi_horizontal'] = ak.count(hits.det[(hits.det == 1) & (hits.vertical == 0)], axis=1)
    vars['n_hits_us_horizontal'] = ak.count(hits.det[(hits.det == 2) & (hits.vertical == 0)], axis=1)
    vars['n_hits_ds_horizontal'] = ak.count(hits.det[(hits.det == 3) & (hits.vertical == 0)], axis=1)
    
    return vars

label_dict = {
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
    labels = inputs.keys()
    x_min, x_max = determine_bins(inputs.values())

    if x_min == x_max:
        print('Skipping', name, 'because either empty or constant', len(inputs.values()))
        return

    c_ax = hist.axis.StrCategory(labels, name='cat', label='Process')    
    ax = hist.axis.Regular(n_bins, x_min, x_max, flow=False, name='x', label=label_dict[name])
    cat_hists = hist.Hist(ax, c_ax)
    for label, data in inputs.items():
        cat_hists.fill(x=data, cat=label)

    stack = cat_hists.stack('cat')
    stack[::-1].plot(stack=True, histtype='fill')
    plt.legend()
    # plt.show()
    plt.savefig(f'{name}.png')



if __name__ == '__main__':
    distributions = {}
    for sample in samples:
        print(f'Loading {sample.name}')
        hits = load_sample(sample)
        print(f'Loaded {len(hits)} events')

        distributions[sample.name] = calculate_input_vars(hits)
        del hits

    for label in distributions[samples[0].name].keys():
        make_plot({k: v[label] for k, v in distributions.items()}, label, n_bins=25, xlabel=label)

    

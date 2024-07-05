import numpy as np
import awkward as ak

from samples import samples, d_samples


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


if __name__ == '__main__':
    distributions = {}
    for sample in samples:
        print(f'Loading {sample.name}')
        hits = load_sample(sample)
        print(f'Loaded {len(hits)} events')

        distributions[sample.name] = calculate_input_vars(hits)
        del hits

    np.save('distributions.npy', distributions)

from glob import glob
from dataclasses import dataclass

import awkward as ak

@dataclass
class Sample:
    name: str
    files: list
    xsec: float = 1.
    class_select: int = -1

    def get_files(self) -> list:
        files = sum([glob(file) for file in self.files], [])
        return files

samples = [
    Sample('nu_e', ['/Users/jan/cernbox/snd_ak/hits*.pt'], 1.0, 0),
    # Sample('nu_mu', ['/Users/jan/cernbox/snd_ak/hits*.pt'], 1.0, 1),
    # Sample('nu_tau', ['/Users/jan/cernbox/snd_ak/hits*.pt'], 1.0, 2),
    # Sample('nc', ['/Users/jan/cernbox/snd_ak/hits*.pt'], 1.0, 4),
    # Sample('neu_80_90', ['/Users/jan/cernbox/snd_ak/neu_80_90_hits0.pt'], 1.0),
    # Sample('neu_20_30', ['/Users/jan/cernbox/snd_ak/neu_20_30_hits1.pt'], 1.0),
    # Sample('neu_50_60', ['/Users/jan/cernbox/snd_ak/neu_50_60_hits2.pt'], 1.0),
    # Sample('neu_90_100', ['/Users/jan/cernbox/snd_ak/neu_90_100_hits3.pt'], 1.0),
    # Sample('neu_60_70', ['/Users/jan/cernbox/snd_ak/neu_60_70_hits4.pt'], 1.0),
    # Sample('neu_30_40', ['/Users/jan/cernbox/snd_ak/neu_30_40_hits5.pt'], 1.0),
    # Sample('neu_40_50', ['/Users/jan/cernbox/snd_ak/neu_40_50_hits0.pt'], 1.0),
    # Sample('neu_70_80', ['/Users/jan/cernbox/snd_ak/neu_70_80_hits0.pt'], 1.0),
]

def load_sample(sample, replace='hits'):
    return ak.concatenate([ak.from_parquet(file.replace('hits', replace)) for file in sample.get_files()])

def calculate_input_vars(data) -> dict:
    '''Produces various distributions for a given sample.
    '''

    vars = {}

    # Per-event variables
    vars['n_hits_total'] = ak.count(hits.det, axis=1)
    vars['n_hits_scifi'] = ak.count(hits.det[hits.det == 1], axis=1)
    vars['n_hits_us'] = ak.count(hits.det[hits.det == 2], axis=1)
    vars['n_hits_ds'] = ak.count(hits.det[hits.det == 3], axis=1)

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
        if sample.class_select >= 0:
            targets = load_sample(sample, replace='targets')
            hits = hits[targets.pdg == sample.class_select]
        
        print(f'Loaded {len(hits)} events')

        distributions[sample] = calculate_input_vars(hits)

    

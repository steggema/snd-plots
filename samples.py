import os

from Sample import Sample

base_dir = '/afs/cern.ch/user/s/steggema/work/snd_lx9/data'

samples = [
    Sample('nu_e', [os.path.join(base_dir, 'neutrino/*hits.pt')], 'electron neutrino', 1.0, 0),
    Sample('nu_mu', [os.path.join(base_dir, 'neutrino/*hits.pt')], 'muon neutrino', 1.0, 1),
    Sample('nu_tau', [os.path.join(base_dir, 'neutrino/*hits.pt')], 'tau neutrino', 1.0, 2),
    Sample('nc', [os.path.join(base_dir, 'neutrino/*hits.pt')], 'neutral current', 1.0, 4),
    Sample('neu_5_10', [os.path.join(base_dir, 'neu_5_10/*hits.pt')], 'neutron', 1.0),
    Sample('neu_10_20', [os.path.join(base_dir, 'neu_20_30/*hits.pt')], 'neutron', 1.0),
    Sample('neu_20_30', [os.path.join(base_dir, 'neu_20_30/*hits.pt')], 'neutron', 1.0),
    Sample('neu_30_40', [os.path.join(base_dir, 'neu_30_40/*hits.pt')], 'neutron', 1.0),
    Sample('neu_40_50', [os.path.join(base_dir, 'neu_40_50/*hits.pt')], 'neutron', 1.0),
    Sample('neu_50_60', [os.path.join(base_dir, 'neu_50_60/*hits.pt')], 'neutron', 1.0),
    Sample('neu_60_70', [os.path.join(base_dir, 'neu_60_70/*hits.pt')], 'neutron', 1.0),
    Sample('neu_70_80', [os.path.join(base_dir, 'neu_70_80/*hits.pt')], 'neutron', 1.0),
    Sample('neu_80_90', [os.path.join(base_dir, 'neu_80_90/*hits.pt')], 'neutron', 1.0),
    Sample('neu_90_100', [os.path.join(base_dir, 'neu_90_100/*hits.pt')], 'neutron', 1.0),
    Sample('data_2023', [os.path.join(base_dir, 'data_2023/*hits.pt')], 'data', 1.0),
]

d_samples = {sample.name: sample for sample in samples}

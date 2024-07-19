import os
from glob import glob

from Sample import Sample

base_dir = '/afs/cern.ch/user/s/steggema/work/snd_lx9/data'
base_dir_plot = '/Users/jan/cernbox/snd_plot/'

samples = []

# for i, f in enumerate(glob(os.path.join(base_dir, f'data_2023/*_hits.pt'))):
#     samples.append(Sample(f'data_2023_{i}', [f], 'data', 1.0))

samples += [
    Sample('nu_e', [os.path.join(base_dir, 'neutrino/*hits.pt')], 'electron neutrino', 7.5, 318547, 0), # approximate cross section from p8 of https://indico.cern.ch/event/1309399/contributions/5596455/attachments/2727389/4740233/cv_sndlhc_nuselectionupdate_20231004.pdf
    Sample('nu_mu', [os.path.join(base_dir, 'neutrino/*hits.pt')], 'muon neutrino', 7.5, 318547, 1),
    Sample('nu_tau', [os.path.join(base_dir, 'neutrino/*hits.pt')], 'tau neutrino', 7.5, 318547, 2),
    Sample('nc', [os.path.join(base_dir, 'neutrino/*hits.pt')], 'neutral current', 7.5, 318547, 4),
    # Cross sections per 1 fb-1 from https://cds.cern.ch/record/2862767/files/Observation_of_neutrino_interactions_at_SND_LHC.pdf table 4
    Sample('neu_5_10', [os.path.join(base_dir, 'neu_5_10/*hits.pt')], 'neutron', 1.0, 1998000), # 14525000 high_stat
    Sample('neu_10_20', [os.path.join(base_dir, 'neu_20_30/*hits.pt')], 'neutron', 575.5 + 273.2, 1994000),
    Sample('neu_20_30', [os.path.join(base_dir, 'neu_20_30/*hits.pt')], 'neutron', 160.7 + 102., 997000),
    Sample('neu_30_40', [os.path.join(base_dir, 'neu_30_40/*hits.pt')], 'neutron', 65.1 + 55.7, 983000),
    Sample('neu_40_50', [os.path.join(base_dir, 'neu_40_50/*hits.pt')], 'neutron', 23.6 + 38.5, 989000),
    Sample('neu_50_60', [os.path.join(base_dir, 'neu_50_60/*hits.pt')], 'neutron', 40, 491893), # starting from here numbers very approximate
    Sample('neu_60_70', [os.path.join(base_dir, 'neu_60_70/*hits.pt')], 'neutron', 25, 490000),
    Sample('neu_70_80', [os.path.join(base_dir, 'neu_70_80/*hits.pt')], 'neutron', 15, 493000),
    Sample('neu_80_90', [os.path.join(base_dir, 'neu_80_90/*hits.pt')], 'neutron', 10, 495000),
    Sample('neu_90_100', [os.path.join(base_dir, 'neu_90_100/*hits.pt')], 'neutron', 8, 494408),

    Sample('K_5_10', [os.path.join(base_dir, 'K_5_10/*hits.pt')], 'kaon', 1.0, 1986000), # 14800000 high_stat
    Sample('K_10_20', [os.path.join(base_dir, 'K_20_30/*hits.pt')], 'kaon', 685.2 + 27.8, 1986000),
    Sample('K_20_30', [os.path.join(base_dir, 'K_20_30/*hits.pt')], 'kaon', 217.8 + 27.9, 995000),
    Sample('K_30_40', [os.path.join(base_dir, 'K_30_40/*hits.pt')], 'kaon', 90.7 + 21.3, 996000),
    Sample('K_40_50', [os.path.join(base_dir, 'K_40_50/*hits.pt')], 'kaon', 70.2 + 10.3, 997000),
    Sample('K_50_60', [os.path.join(base_dir, 'K_50_60/*hits.pt')], 'kaon', 80, 490000), # starting from here numbers very approximate
    Sample('K_60_70', [os.path.join(base_dir, 'K_60_70/*hits.pt')], 'kaon', 65, 437000),
    Sample('K_70_80', [os.path.join(base_dir, 'K_70_80/*hits.pt')], 'kaon', 50, 358341),
    Sample('K_80_90', [os.path.join(base_dir, 'K_80_90/*hits.pt')], 'kaon', 35, 403000),
    Sample('K_90_100', [os.path.join(base_dir, 'K_90_100/*hits.pt')], 'kaon', 20, 372428),
    Sample('data_2023', [], 'neutron', 1.0),

]

d_samples = {sample.name: sample for sample in samples}

from Sample import Sample

samples = [
    Sample('nu_e', ['/Users/jan/cernbox/snd_ak/hits*.pt'], 'electron neutrino', 1.0, 0),
    Sample('nu_mu', ['/Users/jan/cernbox/snd_ak/hits*.pt'], 'muon neutrino', 1.0, 1),
    Sample('nu_tau', ['/Users/jan/cernbox/snd_ak/hits*.pt'], 'tau neutrino', 1.0, 2),
    Sample('nc', ['/Users/jan/cernbox/snd_ak/hits*.pt'], 'neutral current', 1.0, 4),
    Sample('neu_80_90', ['/Users/jan/cernbox/snd_ak/neu_80_90_hits0.pt'], 'neutron', 1.0),
    Sample('neu_20_30', ['/Users/jan/cernbox/snd_ak/neu_20_30_hits1.pt'], 'neutron', 1.0),
    Sample('neu_50_60', ['/Users/jan/cernbox/snd_ak/neu_50_60_hits2.pt'], 'neutron', 1.0),
    Sample('neu_90_100', ['/Users/jan/cernbox/snd_ak/neu_90_100_hits3.pt'], 'neutron', 1.0),
    Sample('neu_60_70', ['/Users/jan/cernbox/snd_ak/neu_60_70_hits4.pt'], 'neutron', 1.0),
    Sample('neu_30_40', ['/Users/jan/cernbox/snd_ak/neu_30_40_hits5.pt'], 'neutron', 1.0),
    Sample('neu_40_50', ['/Users/jan/cernbox/snd_ak/neu_40_50_hits0.pt'], 'neutron', 1.0),
    Sample('neu_70_80', ['/Users/jan/cernbox/snd_ak/neu_70_80_hits0.pt'], 'neutron', 1.0),
]

d_samples = {sample.name: sample for sample in samples}

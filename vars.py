import numpy as np
import awkward as ak
from Var import Var

vars = [
    Var('n_hits_total', lambda h: ak.count(h.det, axis=1), 'Number of total hits'),
    Var('n_hits_scifi', lambda h: ak.count(h.det[h.det == 4], axis=1), 'Number of scifi hits'),
    Var('n_hits_us', lambda h: ak.count(h.det[h.det == 2], axis=1), 'Number of us hits'),
    Var('n_hits_ds', lambda h: ak.count(h.det[h.det == 3], axis=1), 'Number of ds hits'),
    Var('n_hits_veto', lambda h: ak.count(h.det[(h.det == 1)], axis=1), 'Number of veto hits'),
    Var('n_hits_veto_0', lambda h: ak.count(h.det[(h.det == 1) & (h.strip_z < 285.)], axis=1), 'Number of veto_0 hits'),
    Var('n_hits_veto_1', lambda h: ak.count(h.det[(h.det == 1) & (h.strip_z > 285.) & (h.strip_z < 290.)], axis=1), 'Number of veto_1 hits'),
    Var('n_hits_scifi_1', lambda h: ak.count(h.det[(h.det == 4) & (h.strip_z > 295.) & (h.strip_z < 305.)], axis=1), 'Number of scifi_1 hits'),
    Var('n_hits_scifi_2', lambda h: ak.count(h.det[(h.det == 4) & (h.strip_z > 310.) & (h.strip_z < 320.)], axis=1), 'Number of scifi_2 hits'),
    Var('n_hits_scifi_3', lambda h: ak.count(h.det[(h.det == 4) & (h.strip_z > 320.) & (h.strip_z < 330.)], axis=1), 'Number of scifi_3 hits'),
    Var('n_hits_scifi_4', lambda h: ak.count(h.det[(h.det == 4) & (h.strip_z > 335.) & (h.strip_z < 345.)], axis=1), 'Number of scifi_4 hits'),
    Var('n_hits_scifi_5', lambda h: ak.count(h.det[(h.det == 4) & (h.strip_z > 350.) & (h.strip_z < 360.)], axis=1), 'Number of scifi_5 hits'),
    #Var('n_scifi_layers', lambda h: np.int32(vars['n_hits_scifi_1']) + vars['n_hits_scifi_2'] + vars['n_hits_scifi_3'] + vars['n_hits_scifi_4'] + vars['n_hits_scifi_5'], 'Number of SciFi layers hits'),
    Var('n_hits_scifi_vertical', lambda h: ak.count(h.det[(h.det == 4) & (h.vertical == 1)], axis=1), 'Number of vertical SciFi hits'),
    Var('n_hits_us_vertical', lambda h: ak.count(h.det[(h.det == 2) & (h.vertical == 1)], axis=1), 'Number of vertical US hits'),
    Var('n_hits_ds_vertical', lambda h: ak.count(h.det[(h.det == 3) & (h.vertical == 1)], axis=1), 'Number of vertical DS hits'),
    Var('n_hits_scifi_horizontal', lambda h: ak.count(h.det[(h.det == 4) & (h.vertical == 0)], axis=1), 'Number of horizontal SciFi hits'),
    Var('n_hits_us_horizontal', lambda h: ak.count(h.det[(h.det == 2) & (h.vertical == 0)], axis=1), 'Number of horizontal US hits'),
    Var('n_hits_ds_horizontal', lambda h: ak.count(h.det[(h.det == 3) & (h.vertical == 0)], axis=1), 'Number of horizontal DS hits'),
]

d_vars = {v.name: v for v in vars}
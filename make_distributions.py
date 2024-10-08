import gc

import numpy as np
import awkward as ak
from tqdm import tqdm

from samples import samples, d_samples
from vars import vars, d_vars


def process_sample(sample, replace='targets.') -> dict:
    out = {}

    for file in tqdm(sample.get_files()):
        hits = ak.from_parquet(file)
        if sample.class_select >= 0:
            targets = ak.from_parquet(file.replace('hits.', replace), columns=['pdg'])
            hits = hits[targets.pdg == sample.class_select]
            del targets
        
        for var in vars:
            if var.name not in out:
                out[var.name] = ak.values_astype(var.func(hits), var.type)
            else:
                out[var.name] = ak.concatenate([out[var.name], ak.values_astype(var.func(hits), var.type)], axis=0)
        
        del hits
        gc.collect()
    return out


if __name__ == '__main__':
    for sample in samples:
        print(f'Processing {sample.name}')
        distributions = process_sample(sample)
        np.savez_compressed(f'distributions_{sample.name}.npz', distributions)

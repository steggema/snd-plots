'''Concatenates dictionaries of numpy arrays from the distributed
production for data events'''
import numpy as np
from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('files', nargs='+', help='Files to concatenate')
    parser.add_argument('-o', '--output', help='Output file name', default='distributions.npz')
    args = parser.parse_args()

    import numpy as np

    all_ds = [np.load(f, allow_pickle=True)['arr_0'].item() for f in args.files]

    d_out = {}
    for key in all_ds[0].keys():
        d_out[key] = np.concatenate([ds[key] for ds in all_ds], axis=0)

    np.savez_compressed(args.output, d_out)

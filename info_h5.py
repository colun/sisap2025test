import sys
import h5py

assert len(sys.argv) == 2

h5 = h5py.File(sys.argv[1])
def func(path):
    data = h5
    for name in path:
        data = data[name]
    if isinstance(data, h5py.Group):
        for name in data:
            func(path + [name])
    elif isinstance(data, h5py.Dataset):
        print(data.name, data.shape, data.dtype)
func([])

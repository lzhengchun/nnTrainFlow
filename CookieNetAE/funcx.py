
def funcX_simulation(wdir, cmde):
    cmd_aug = cmde.split('#')
    import subprocess, os
    os.chdir(wdir) 
    
    fns = os.listdir('out/')
    for item in fns:
        if item.endswith(".h5"):
            os.remove(os.path.join('out', item))    

    result = subprocess.run(cmd_aug, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

# simu_uuid = fxc.register_function(funcX_simulation)
# print(f'funcX ID for simu: {simu_uuid}')

def funcX_simu_data_proc_for_CookieNetAE(ddir, tfn, vfn):
    import glob, h5py, os
    import numpy as np
    
    odir = '/'.join(tfn.split('/')[:-1])
    for item in os.listdir(odir):
        os.remove(os.path.join(odir, item))    
    
    raw_fns = glob.glob(f'{ddir}/*.h5')
    
    if len(raw_fns)==0:
        return f"no data found in {ddir}"
    
    tmp2sz = raw_fns[0]
    with h5py.File(tmp2sz, 'r') as fp:
        _k = list(fp.keys())[0]
        h, w = fp[_k]['Ximg'].shape
    
    h5_train = h5py.File(tfn, 'w')
    ds_train_x = h5_train.create_dataset(name='Ximg', shape=(0, h, w), maxshape=(None, h, w), dtype='uint8',)
    ds_train_y = h5_train.create_dataset(name='Ypdf', shape=(0, h, w), maxshape=(None, h, w), dtype='f4',)

    h5_valid = h5py.File(vfn, 'w')
    ds_valid_x = h5_valid.create_dataset(name='Ximg', shape=(0, h, w), maxshape=(None, h, w), dtype='uint8',)
    ds_valid_y = h5_valid.create_dataset(name='Ypdf', shape=(0, h, w), maxshape=(None, h, w), dtype='f4',)
    
    for _fn in raw_fns:
        h5_src = h5py.File(_fn, 'r')
        _xtrain, _ytrain = [], []
        _xvalid, _yvalid = [], []
        for _k in list(h5_src.keys()):
            if h5_src[_k].attrs['Train']:
                _xtrain.append(h5_src[_k]['Ximg'][:])
                _ytrain.append(h5_src[_k]['Ypdf'][:])
            else:
                _xvalid.append(h5_src[_k]['Ximg'][:])
                _yvalid.append(h5_src[_k]['Ypdf'][:])

        n_train = len(_xtrain)
        n_valid = len(_xvalid)

        ds_train_x.resize(ds_train_x.shape[0]+n_train, axis=0)
        ds_train_x[-n_train:] = np.array(_xtrain)

        ds_train_y.resize(ds_train_y.shape[0]+n_train, axis=0)
        ds_train_y[-n_train:] = np.array(_ytrain)

        ds_valid_x.resize(ds_valid_x.shape[0]+n_valid, axis=0)
        ds_valid_x[-n_valid:] = np.array(_xvalid)

        ds_valid_y.resize(ds_valid_y.shape[0]+n_valid, axis=0)
        ds_valid_y[-n_valid:] = np.array(_yvalid)

        h5_src.close()
        print("%s has been processed, there are %d and %d samples for training and validation seperately" % (_fn, n_train, n_valid))

    h5_train.close()
    h5_valid.close()

    return tfn, vfn

# curation_uuid = fxc.register_function(funcX_simu_data_proc_for_CookieNetAE)
# print(f'funcX ID for simu dataCure: {curation_uuid}')

def funcX_mdl_train(wdir, cmde):
    cmd_aug = cmde.split('#')
    import subprocess, os
    os.chdir(wdir) 
    result = subprocess.run(cmd_aug, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')
    
# train_uuid = fxc.register_function(funcX_mdl_train)
# print(f'funcX ID for simu dataCure: {train_uuid}')

from gladier import GladierBaseTool, generate_flow_definition

def model_train(train_wdir, train_cmde, **data):
    cmd_aug = train_cmde.split('#')
    import subprocess, os
    os.chdir(train_wdir) 
    os.environ['MKL_THREADING_LAYER'] = 'GNU'
    result = subprocess.run(cmd_aug, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')

@generate_flow_definition(modifiers={
    model_train: {'endpoint': 'fx_ep_train'}
})
class ModelTrain(GladierBaseTool):
    funcx_functions = [model_train]
    required_input = [
        'train_wdir',
        'train_cmde', 
        'fx_ep_train'
        ]



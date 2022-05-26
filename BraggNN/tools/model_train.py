from gladier import GladierBaseTool, generate_flow_definition

def model_train(wdir, cmde, **data):
    import subprocess, os

    os.chdir(wdir) 

    cmd = cmde.split('#')

    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return str(res.stdout), str(res.stderr)

@generate_flow_definition
class ModelTrain(GladierBaseTool):
    funcx_functions = [model_train]
    required_input = [
        'wdir',
        'cmde', 
        'funcx_endpoint_compute'
        ]



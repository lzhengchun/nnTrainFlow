from gladier import GladierBaseTool, generate_flow_definition

def run_simulation(simu_wdir, simu_cmde, **data):
    import subprocess, os

    os.chdir(simu_wdir) 
    fns = os.listdir('out/')
    for item in fns:
        if item.endswith(".h5"):
            os.remove(os.path.join('out', item))    
            
    cmd = simu_cmde.split('#')

    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return str(res.stdout), str(res.stderr)

@generate_flow_definition(modifiers={
    run_simulation: {'endpoint': 'fx_ep_simu'}
})
class RunSimu(GladierBaseTool):
    funcx_functions = [run_simulation]
    required_input = [
        'simu_wdir',
        'simu_cmde', 
        'fx_ep_simu'
        ]



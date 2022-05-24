
def trun_mdl_train(wdir, cmde):
    cmd_aug = cmde.split('#')
    import subprocess, os
    os.chdir(wdir) 
    result = subprocess.run(cmd_aug, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')
    
# shell_function = fxc.register_function(trun_mdl_train)
# shell_function

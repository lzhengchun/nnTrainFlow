from globus_automate_client import create_flows_client
import yaml, time
from dateutil import parser

class DNNTrainFlow:
    def __init__(self, cfg, label=None):
        wf_cfg = yaml.load(open(cfg, 'r'), Loader=yaml.CLoader)
        if label is not None:
            self.label = label
        else:
            self.label = wf_cfg['wf_name']
            
        self.flow_args = {
            "input": {
                "fx_ep_simu": wf_cfg['simulation_func']['EUUID'],
                "fx_id_simu": wf_cfg['simulation_func']['FUUID'],
                "params_simu":{'wdir': wf_cfg['simulation_func']['args_wdir'],
                               'cmde': wf_cfg['simulation_func']['args_cmde']},
                
                "fx_ep_cure": wf_cfg['curation_func']['EUUID'],
                "fx_id_cure": wf_cfg['curation_func']['FUUID'],
                "params_cure":{'ddir':wf_cfg['curation_func']['args_ddir'],
                               'tfn':wf_cfg['curation_func']['args_tfn'],
                               'vfn':wf_cfg['curation_func']['args_vfn']},
                
                "data_endpoint": wf_cfg['src_data']['UUID'],
                "data_path":wf_cfg['src_data']['PATH'],
                
                "aisys_endpoint": wf_cfg['dst_data']['UUID'],
                "aisys_path":wf_cfg['dst_data']['PATH'],
                
                "fx_ep_train": wf_cfg['training_func']['EUUID'],
                "fx_id_train": wf_cfg['training_func']['FUUID'],
                "params_train":{'wdir':wf_cfg['training_func']['args_wdir'],
                                'cmde':wf_cfg['training_func']['args_cmde']},
                
                "aisys_endpoint": wf_cfg['src_model']['UUID'],
                "aisys_mdl_path":wf_cfg['src_model']['PATH'],
                
                "dest_endpoint": wf_cfg['dst_model']['UUID'],
                "dest_path":wf_cfg['dst_model']['PATH'],
            }
        }
        self.flow_id = wf_cfg['workflow']['FLOWID']
        self.flow_scope = wf_cfg['workflow']['SCOPE']
        # self.flow_scope = f"https://auth.globus.org/scopes/{self.flow_id}/flow_{self.flow_id.replace('-','_')}_user"
        self.flows_client = create_flows_client()

    def run(self, ):        
        run_resp = self.flows_client.run_flow(flow_id=self.flow_id,\
                                            flow_scope=self.flow_scope, \
                                            flow_input=self.flow_args, \
                                            label=f"{self.label}")
        self.action_id   = run_resp['action_id']
        self.flow_action = run_resp
        self.start_ts    = time.time()
        return run_resp
    
    def status(self,):
        action = self.flows_client.flow_action_status(self.flow_id, \
                                                      self.flow_scope, \
                                                      self.action_id)
        self.flow_action = action
        return action
    
    def progress(self, ):
        flow_action = self.status()
        flow_status = flow_action['status']
        if flow_status == 'ACTIVE':
            try:
                state_name = flow_action['details']['action_statuses'][-1]['state_name']
            except:
                state_name = 'UNKNOWN'
            flow_elapsed = time.time() - self.start_ts
            msg = f'Flow State: {state_name}; total elapsed time: {flow_elapsed:.1f} seconds.'
        else:
            msg = f"Flow is not Active. It's {flow_status}!"
        return msg, flow_status == 'ACTIVE'
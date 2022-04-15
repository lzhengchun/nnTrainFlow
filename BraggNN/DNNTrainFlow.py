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
                "data_endpoint": wf_cfg['src_data_fabric']['UUID'],
                "data_path": wf_cfg['src_data_fabric']['PATH'],
                "comp_endpoint":wf_cfg['dst_data_fabric']['UUID'],
                "comp_path":wf_cfg['dst_data_fabric']['PATH'],
                "mdl_path":wf_cfg['src_model_fabric']['PATH'],
                "dest_endpoint": wf_cfg['dst_model_fabric']['UUID'],
                "dest_path": wf_cfg['dst_model_fabric']['PATH'],
                "fx_ep": wf_cfg['computing_fabric']['EUUID'],
                "fx_id": wf_cfg['computing_fabric']['TrFUUID'],
                "params": {'wdir': wf_cfg['computing_fabric']['WDIR'],
                           'cmde': wf_cfg['computing_fabric']['TrCMD']}
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
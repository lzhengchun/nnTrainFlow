
import argparse
import yaml

from gladier import GladierBaseClient, generate_flow_definition

##Import tools that will be used on the flow definition
from tools.transfer_data import TransferData
from tools.model_train import ModelTrain
from tools.transfer_model import TransferModel
from tools.run_simu import RunSimu
from tools.cure_date import CureData

##Generate flow based on the collection of `gladier_tools` 
@generate_flow_definition
class CookieNetAE_Train_Client(GladierBaseClient):
    globus_group = '0bbe98ef-de8f-11eb-9e93-3db9c47b68ba'
    gladier_tools = [
        RunSimu,
        CureData,
        TransferData,
        ModelTrain,
        TransferModel,
    ]

def create_input_cfg(cfg):
    wf_cfg = yaml.load(open(cfg, 'r'), Loader=yaml.CLoader)
        
    flow_args = {
        "input": {
            "fx_ep_simu": wf_cfg['simulation_func']['EUUID'],
            "simu_wdir" : wf_cfg['simulation_func']['args_wdir'],
            "simu_cmde" : wf_cfg['simulation_func']['args_cmde'],
            
            "fx_ep_cure": wf_cfg['curation_func']['EUUID'],
            "cure_ddir" : wf_cfg['curation_func']['args_ddir'],
            "cure_tfn"  : wf_cfg['curation_func']['args_tfn'],
            "cure_vfn"  : wf_cfg['curation_func']['args_vfn'],

            "data_endpoint": wf_cfg['src_data']['UUID'],
            "data_path"    : wf_cfg['src_data']['PATH'],
            
            "aisys_endpoint": wf_cfg['dst_data']['UUID'],
            "aisys_path"    : wf_cfg['dst_data']['PATH'],
            
            "fx_ep_train": wf_cfg['training_func']['EUUID'],
            "train_wdir" : wf_cfg['training_func']['args_wdir'],
            "train_cmde" : wf_cfg['training_func']['args_cmde'],
            
            "aisys_endpoint": wf_cfg['src_model']['UUID'],
            "aisys_mdl_path": wf_cfg['src_model']['PATH'],
            
            "dest_endpoint": wf_cfg['dst_model']['UUID'],
            "dest_path"    : wf_cfg['dst_model']['PATH'],
        }
    }
    return flow_args, wf_cfg['wf_name']

def train_with_flow(cfg):
   ##The first step Client instance
    trainClient = CookieNetAE_Train_Client()

    flow_input, wf_label = create_input_cfg(cfg)

    flow_run = trainClient.run_flow(flow_input=flow_input, label=wf_label)

    print('Run started with ID: ' + flow_run['action_id'])

##  Arguments for the execution of this file as a stand-alone client
def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', help='YAML config File', required=True)
    return parser.parse_args()

## Main execution of this "file" as a Standalone client
if __name__ == '__main__':

    args = arg_parse()
    train_with_flow(args.config)
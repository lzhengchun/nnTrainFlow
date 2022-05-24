flow4CookieNetAE = {
  "Comment": "A workflow to RUN simulation for data, train a DL model with the data and transfer trained model back",
  "StartAt": "runSimulation",
  "States": {
    "runSimulation": {
      "Comment": "Run CookieSimSlim to Generate datasets",
      "Type": "Action",
      "ActionUrl": "https://automate.funcx.org",
      "ActionScope": "https://auth.globus.org/scopes/b3db7e59-a6f1-4947-95c2-59d6b7a70f8c/action_all",
      "Parameters": {
          "tasks": [{
            "endpoint.$": "$.input.fx_ep_simu",
            "function.$": "$.input.fx_id_simu",
            "payload.$": "$.input.params_simu"
        }]
      },
      "ResultPath": "$.runSimulationRes",
      "WaitTime": 3600,
      "Next": "cureData"
    },
    "cureData": {
      "Comment": "Run the funcX function to curate simulation data",
      "Type": "Action",
      "ActionUrl": "https://automate.funcx.org",
      "ActionScope": "https://auth.globus.org/scopes/b3db7e59-a6f1-4947-95c2-59d6b7a70f8c/action_all",
      "Parameters": {
          "tasks": [{
            "endpoint.$": "$.input.fx_ep_cure",
            "function.$": "$.input.fx_id_cure",
            "payload.$": "$.input.params_cure"
        }]
      },
      "ResultPath": "$.cureDataRes",
      "WaitTime": 1800,
      "Next": "transferData"
    },
    "transferData": {
      "Comment": "Return transfer to move trained CookieNetAE and traces back",
      "Type": "Action",
      "ActionUrl": "https://actions.automate.globus.org/transfer/transfer",
      "ActionScope": "https://auth.globus.org/scopes/actions.globus.org/transfer/transfer",
      "Parameters": {
        "source_endpoint_id.$": "$.input.data_endpoint", 
        "destination_endpoint_id.$": "$.input.aisys_endpoint",
        "encrypt_data": False,
        "transfer_items": [
          {
            "source_path.$": "$.input.data_path",
            "destination_path.$": "$.input.aisys_path",
            "recursive": True 
          }
        ]
      },
      "ResultPath": "$.trainModelRes",
      "WaitTime": 3600,
      "Next": "trainModel"
    },
    "trainModel": {
      "Comment": "Run the funcX function to train CookieNetAE",
      "Type": "Action",
      "ActionUrl": "https://automate.funcx.org",
      "ActionScope": "https://auth.globus.org/scopes/b3db7e59-a6f1-4947-95c2-59d6b7a70f8c/action_all",
      "Parameters": {
          "tasks": [{
            "endpoint.$": "$.input.fx_ep_train",
            "function.$": "$.input.fx_id_train",
            "payload.$": "$.input.params_train"
        }]
      },
      "ResultPath": "$.trainModelRes",
      "WaitTime": 1800,
      "Next": "transferModel"
    },
    "transferModel": {
      "Comment": "Return transfer to move trained CookieNetAE and traces back",
      "Type": "Action",
      "ActionUrl": "https://actions.automate.globus.org/transfer/transfer",
      "ActionScope": "https://auth.globus.org/scopes/actions.globus.org/transfer/transfer",
      "Parameters": {
        "source_endpoint_id.$": "$.input.aisys_endpoint", 
        "destination_endpoint_id.$": "$.input.dest_endpoint",
        "encrypt_data": False,
        "transfer_items": [
          {
            "source_path.$": "$.input.aisys_mdl_path",
            "destination_path.$": "$.input.dest_path",
            "recursive": True 
          }
        ]
      },
      "ResultPath": "$.transferModelRes",
      "WaitTime": 600,
      "End": True
    },
  }
}
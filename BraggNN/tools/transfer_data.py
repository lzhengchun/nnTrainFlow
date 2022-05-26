from gladier import GladierBaseTool


class TransferData(GladierBaseTool):

    flow_definition = {
        'Comment': 'Transfer a file or directory in Globus',
        'StartAt': 'TransferData',
        'States': {
            'TransferData': {
                'Comment': 'Transfer a file or directory in Globus',
                'Type': 'Action',
                'ActionUrl': 'https://actions.automate.globus.org/transfer/transfer',
                'Parameters': {
                    'source_endpoint_id.$': '$.input.data_endpoint',
                    'destination_endpoint_id.$': '$.input.comp_endpoint',
                    'transfer_items': [
                        {
                            'source_path.$': '$.input.data_path',
                            'destination_path.$': '$.input.comp_path',
                            'recursive': True,
                        }
                    ]
                },
                'ResultPath': '$.TransferData',
                'WaitTime': 600,
                'End': True
            },
        }
    }

    flow_input = {}
    required_input = [
        'data_endpoint',
        'data_path',
        'comp_endpoint',
        'comp_path',
    ]

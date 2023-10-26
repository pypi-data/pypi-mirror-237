import os, json

def load_credential(channel = None, credential_path = None):
    """
    Loads the credentials for a specified channel from a JSON file.

    Args:
        channel (str): The channel to load credentials for. Should be either "ibm_quantum" or "ibm_cloud".
        credential_path (str): The path to the JSON file containing the credentials. If None, the default path is used.

    Returns:
        dict: A dictionary containing the credentials for the specified channel.
    """
    if not channel:
        channel = "ibm_quantum"
    if channel not in ["ibm_quantum", "ibm_cloud"]:
        raise ValueError("`channel` should be either 'ibm_quantum' or 'ibm_cloud'")
    
    if not credential_path:
        credential_path = os.path.join(os.path.dirname(__file__), "provider_credential.json")
    
    with open(credential_path, "r") as f:
        credential = json.load(f)[channel]
    
    return credential



def load_provider(channel = None, credential_path = None):
    """
    Loads a provider for a specified channel.

    Args:
        channel (str): The channel to load the provider for. Should be either "ibm_quantum" or "ibm_cloud".
        credential_path (str): The path to the JSON file containing the credentials. If None, the default path is used.

    Returns:
        BaseProvider: A provider object for the specified channel.
    """
    if not channel:
        channel = "ibm_quantum"
    if channel not in ["ibm_quantum", "ibm_cloud"]:
        raise ValueError("`channel` should be either 'ibm_quantum' or 'ibm_cloud'")
    
    if not credential_path:
        credential_path = os.path.join(os.path.dirname(__file__), "provider_credential.json")
    
    credential = load_credential(channel, credential_path)

    if channel == "ibm_quantum":
        from qiskit import IBMQ
        IBMQ.load_account()
        return IBMQ.get_provider(hub = credential["hub"], group = credential["group"], project = credential["project"])
    elif channel == "ibm_cloud":
        from qiskit_ibm_runtime import QiskitRuntimeService
        service = QiskitRuntimeService(instance = credential["crn"])
        return service

import sys
import os
import asamp.config as config
from asamp.disassembly import Assembly
sys.stdout = open(os.path.join(config.src_fldr, "ghpython_log.txt"), 'w') # Change to 'a' for append

import numpy as np

import tempfile
import atexit
import time
from datetime import datetime


load_time = datetime.now()
dt_string = load_time.strftime("%d/%m/%Y %H:%M:%S")
print("Logfile time: ", dt_string)


# Example usage in Grasshopper:
# import rhinoscriptsyntax as rs
# from compas.rpc import Proxy

# with Proxy('asamp.ghpython', python='C:\Users\Sam\Anaconda3\envs\project\python.exe') as proxy:
#     proxy.run_test()

# ## Or, without context managers
# proxy = Proxy('asamp.ghpython', python='C:\Users\Sam\Anaconda3\envs\project\python.exe')
# proxy.run_test()
# proxy.stop_server()


@atexit.register
def clean_stdout():
    # Ensure we clean up the logfile when the module is unloaded
    print("Closing logfile...")
    sys.stdout.close()    

@atexit.register
def clean_temp():
    try:
        if config.tmp:
            config.tmp.cleanup()
            if os.path.exists(config.tmp.name):
                import shutil
                shutil.rmtree(config.tmp.name)
            del config.tmp
    except:
        pass
    #config.tmp.close()

def run_test():
    import sys
    print("Test", file=sys.stdout)

def get_disassembly(n = 0, rebuild_tree=False, depth_mult=5):
    print("Calling from disassembly module")
    from asamp.disassembly import Assembly
    test = Assembly()
    if rebuild_tree:
        test.disassembly_tree(time_limit=60*5, depth_mult=depth_mult)

    tree = test.load_tree()
    #elements, directions = test.disassemble_loosest()

    sorted_tree = sorted(tree, key=lambda x: x.cum_freedom, reverse=True)

    first = sorted_tree[n]
    
    elements, directions = test.reconstruct_from_tree_node(first)

    return elements,directions


def reachmap():
    import pickle
    with open(config.reachmap, "rb") as handle:
        data = pickle.load(handle, encoding='latin1')
    return data

Assembly = Assembly

# if __name__ == '__main__':
#     print(get_disassembly())
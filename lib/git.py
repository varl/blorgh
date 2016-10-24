'''
TODO: Hard dependency on the Git binary at `/usr/bin/git`
'''

import subprocess

def clone(url, target):
  subprocess.call(['/usr/bin/git', 'clone', url, target])
  

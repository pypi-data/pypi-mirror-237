from subprocess import run as sprun
from hak.directory.make import f as mkdir
from hak.directory.remove import f as rmdir
from hak.system.git.init import f as git_init
from hak.file.save import f as save
from hak.system.git.commit.run import f as git_commit

_root = '../temp_git_log_oneline'

def up():
  mkdir(_root)
  git_init(_root)
  save(_root+'/foo.py', 'foo')
  git_commit(do_pull=False, cwd=_root, do_push=False)

def dn(): rmdir(_root)

args = ['git', 'log', '--oneline']

f = lambda cwd: sprun(cwd=cwd, capture_output=True, args=args)

def t():
  up()
  z = f(_root)
  dn()
  return all([
    z.args==args,
    z.returncode==0,
    'Added foo.py' in z.stdout.decode('utf-8'),
    not z.stderr.decode('utf-8')
  ])

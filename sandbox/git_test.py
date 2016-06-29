from git import Repo
from git.refs.tag import  TagReference
from git.objects.commit import  Commit
repo = Repo(path=r"c:\Work\RedCat\riverbeas")

tree = repo.heads.master.commit.tree
fifty_first_commits = list(repo.iter_commits('master', max_count=50))
print(fifty_first_commits)
first_commit = fifty_first_commits[0]


with repo.git.custom_environment(GIT_SSH='c:/Programs/babun/.babun/cygwin/bin/ssh.exe'):
    repo.remotes.origin.fetch()

tag = repo.tags[0]

commit = Commit(repo)

import shutil,errno,os,subprocess

user_input = input('Please enter your project name. (Default is app) \r\n') or 'app'
folder = input('Please enter where you want to create your project. (Default : ~/$PROJECT) \r\n') or '$HOME'

if folder[0] == '~' and not folder == None:
    folder = os.path.join( os.environ['HOME'] , folder[2::])

if folder == '$HOME' :
    new_folder = os.path.join( os.environ['HOME'] , user_input)
else:
    if folder[-1:] == '/':
        pass 
    else:
        folder = folder + '/'
    new_folder = folder + user_input

if user_input == 'app':
    user_project = 'app'
else:
    user_project = '%s_app' % user_input

try:
    shutil.copytree('./mu_sanic_src', new_folder)
except OSError as e:
    raise e

old_app = new_folder+'/app'
new_app = new_folder+'/%s' % user_project
os.rename(old_app,new_app)
subprocess.call("echo 'your_app=\"" + user_project + "\"' >> " + new_folder + '/mu_sanic/config.py',shell=True)
print('Your mu_sanic project create in %s' % new_folder )
print('Your mu_sanic project app create in %s' % new_app )
print('Your mu_sanic project config create in %s/mu_sanic/config.py' % new_folder )


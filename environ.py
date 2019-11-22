import os
import re

#for env in os.environ:
#	print(env)

print("--------------------------")
#print(os.environ.get("PWD"))
#print(os.environ.get("USER"))


wo = "${USER}"
m = re.match(r'^\$\{(.*)\}', wo)
if m.group(1) == "USER":
	print(os.environ.get(m.group(1)))


def get_env(string,env_var):
	mm = re.match(r'^\$\{(.*)\}',string)
	if mm.group(1) == env_var:
		return os.environ.get(mm.group(1))

print(get_env(wo,"USER"))


#print(m.group(1))


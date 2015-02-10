import os,sys

def main(project_name):
	print('Creating folders and files for the project %s' % project_name)
	try:
	    project_path  = '%s/%s' % (os.getcwd(), project_name)
	except Exception, ex:
	    print(' Error - %s; usage: python flaskafolding.py <project_name>' % ex)
	    
	if not os.path.exists(project_path): 
		make_folders(project_path)
		make_modules(project_path)
		generate_requirements(project_path)
		os.system("pip install -r %s/requirements.txt" % project_path)
		generate_main_file(project_path)
	print('Done! Enjoy your project!')



def generate_requirements(project_path):
	req = open('%s/requirements.txt' % project_path,'w')
	req.write('flask\n')
	req.write('pyDAL\n')
	req.flush()
	req.close()
		


def generate_main_file(project_path):
	main_file = open('%s/main.py' % project_path,'w')
	main_file.write('from flask import Flask\n')
	main_file.write('app = Flask(__name__, static_folder="static")\n\n')
	main_file.write('@app.route("/")\n')
	main_file.write('def hello():\n')
	main_file.write('	return "Hello World!"\n\n\n')
	main_file.write('if __name__ == "__main__":\n')
	main_file.write('	app.run()\n')
	main_file.flush()
	main_file.close()


def make_modules(project_path):
	open('%s/models/__init__.py' % project_path,'w').close()
	open('%s/controllers/__init__.py' % project_path,'w').close()
	open('%s/__init__.py' % project_path,'w').close()


def make_folders(project_path):
	os.makedirs(project_path)
	os.makedirs('%s/models' % project_path)
	os.makedirs('%s/views' % project_path)
	os.makedirs('%s/controllers' % project_path)
	os.makedirs('%s/static' % project_path)


if __name__ == "__main__":
	main(sys.argv[1])
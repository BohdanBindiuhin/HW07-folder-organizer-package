from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.1',
    license='MIT', 
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:process_folder']})
   
   

        
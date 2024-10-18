cd [..path_to_dir..]/mySearchEngine &&
source ../mySearchEngineVEnv/bin/activate &&
python3 manage.py refreshOnSaleList >> ~/mySearchEngineLog &&
deactivate

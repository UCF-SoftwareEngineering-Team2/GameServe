# Django GameServe 
-------------------



## Python Environment Specification
-------------------

1. You should use **virtualenv** to keep your python binary in your home directory (no more sudo). Run following from terminal  
`virtualenv ~/.python`  
`echo VIRTUAL_ENV_DISABLE_PROMPT=1 >> ~/.bash_profile`  
`echo source $HOME/.python/bin/activate >> ~/.bash_profile`  
`source ~/.bash_profile`  

2. You should then use pip to install **django-extensions** so you can run custom scripts to fill db  
`./manage.py runscript addDB`  
`pip install django-extensions`  
    - `runscript` allows python files located in scripts/ to run. Useful for scripts to add to DB etc  


## Notes
-------------------

1. Default Admin User account
    - Username: admin
    - Password: admin  

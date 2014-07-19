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


## DB Query
-------------------  
- All courts  
  `/api/v1/court/` 

- Next scheduled events after 7-18-2014 2:44AM  
  `/api/v1/event/?dateTime__gte=2014-7-18% 2:44`  

- Next schedules events on court id 1    
  `/api/v1/event/?dateTime__gte=2014-7-18 2:44&court=1`




## Notes
-------------------

1. Default Admin User account
    - Username: admin
    - Password: admin





## Querying the DB

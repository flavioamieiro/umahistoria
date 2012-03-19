# Este contem facilidades para o shell e é importado pelo postactivate

PROJECT_ROOT="$VIRTUAL_ENV/src"

alias manage="python $PROJECT_ROOT/manage.py"
alias cdsrc="cd $PROJECT_ROOT"
alias cddjango="cd `virtualenvwrapper_get_site_packages_dir`/django"
alias rmpyc="find . -iname '*.pyc' -exec rm {} \;"

# Jindo Client Python Library

## Installation
### Through pip install directly
<b>From local directory for development</b>
Clone the repo locally
```
conda activate <desired_env> # optional. to ensure the library is installed for the desired Python env

pip install -e ./
```

<b>From Github</b>

SSH
```
pip install git+ssh://git@github.com/jindogroup/jindo-aws-py.git

```

HTTPS
```
pip install git+https://github.com/jindogroup/jindo-aws-py.git

```

### Through setup.py/requirements.txt
```
jindo-aws-py @ git+ssh://git@github.com/jindogroup/jindo-aws-py.git
```

or through HTTP
```
jindo-aws-py @ git+https://github.com/jindogroup/jindo-aws-py.git
```

## Update library
```
pip install --upgrade --force-reinstall git+ssh://git@github.com/jindogroup/jindo-aws-py.git
```


### Specify a particular version (commit)

```
jindo-aws-py @ git+ssh://git@github.com/jindogroup/jindo-aws-py.git@<commit_hash>
```
ex: `jindo-aws-py @ git+ssh://git@github.com/jindogroup/jindo-aws-py.git@fcc447827a23e0021ea50096c5cf97f78ec96735`

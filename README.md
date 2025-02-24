# Plateforme demo projet

## Setup

### Install dependencies

```bash
uv sync
```

### Setup the server

```bash
uv run plateforme build
```

### Start the server

```bash
uv run plateforme start --reload
```

### Run the shell and interact with the server

It launches a shell with the server application loaded and the namespace variables:

- `app`: the loaded application
- `plateforme`: the plateforme module

```bash
uv run plateforme shell

>>> app
Plateforme('plateforme-demo-application')

>>> from packages.users import User
>>> with app.session() as session:
...     user = User(username='john', email='john@ex.com', password='123')
...     session.add(user)
...     session.commit()

>>> with app.session() as session:
...     session.query(User).all()
[User(id=1, username='john', email='john@ex.com', password=SecretStr('**********'))]

>>> plateforme
<module 'plateforme' from '...'>

>>> plateforme.runtime.resources
{'packages.users.users.User': <class 'packages.users.users.User'>, ...}

>>> plateforme.framework.VERSION
'0.1.0-a1'
```

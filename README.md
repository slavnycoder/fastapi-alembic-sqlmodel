To generate new migration run from "project" dir
```
alembic revision --autogenerate -m "Migrations name"
```

To apply migration run 
```
alembic upgrade head
```

it's already in `run/fstapi.sh` script

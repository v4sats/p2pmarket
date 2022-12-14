from environs import Env
import logging
import logging.config
from pathlib import Path


app_path = Path(__file__).parent.parent
root_path = app_path.parent
static_path = root_path/"static"
env = Env(expand_vars=True)
env.read_env(app_path/"main.env")

with env.prefixed('P2PMARKET_'):
    run_path = Path(env('RUN_PATH', root_path/"run"))
# configure logging
logs = run_path/'logs'
logs.mkdir(parents=True, exist_ok=True)
logging.config.fileConfig(
        Path(__file__).parent/'logging.conf',
        defaults={'logpath': logs},
        disable_existing_loggers=False
)

# database config
with env.prefixed('P2PMARKET_'):
    db_path = Path(env('PATH', run_path)).joinpath(env('DB_NAME', 'database.db'))
    db_debug = env.bool('DB_DEBUG', False)
db_url = f"sqlite:///{db_path}"



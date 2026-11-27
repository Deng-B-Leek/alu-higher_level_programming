# Python - Object-relational mapping

Scripts using MySQLdb and SQLAlchemy to query MySQL databases.

- `0-select_states.py` - lists all states from `hbtn_0e_0_usa`
- `1-filter_states.py` - lists states starting with `N`
- `2-my_filter_states.py` - lists states matching an argument (uses `format`)
- `3-my_safe_filter_states.py` - same, safe from SQL injection
- `4-cities_by_state.py` - lists all cities with their state name
- `5-filter_cities.py` - lists cities of a given state
- `model_state.py` - `State` model, `Base = declarative_base()`
- `7-model_state_fetch_all.py` - lists all `State` objects
- `8-model_state_fetch_first.py` - prints first `State` object
- `9-model_state_filter_a.py` - lists `State` objects containing `a`
- `10-model_state_my_get.py` - prints `State` with given name
- `11-model_state_insert.py` - adds `Louisiana`
- `12-model_state_update_id_2.py` - renames id 2 to `New Mexico`
- `13-model_state_delete_a.py` - deletes `State` objects containing `a`
- `model_city.py` - `City` model
- `14-model_city_fetch_by_state.py` - lists all `City` objects by state

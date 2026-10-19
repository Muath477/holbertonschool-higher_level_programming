# Python - Object-relational mapping

Scripts that connect Python to a MySQL database. The first part uses the `MySQLdb` module with SQL queries. The second
part uses the `SQLAlchemy` ORM, so the scripts work with Python objects and no SQL.

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- MySQL 8.0 running on localhost, port 3306
- `mysqlclient` 2.0.x (the `MySQLdb` module) and `SQLAlchemy` 1.4.x
- Code style checked with `pycodestyle` 2.7.*

## Files

| File | Description |
| --- | --- |
| `0-select_states.py` | Lists all the states of a database, sorted by id. |
| `1-filter_states.py` | Lists the states whose name starts with an upper case N. |
| `2-my_filter_states.py` | Lists the states matching a name given as argument (query built with `format`). |
| `3-my_safe_filter_states.py` | Same as the previous one, safe from SQL injection. |
| `4-cities_by_state.py` | Lists all the cities with the name of their state. |
| `5-filter_cities.py` | Lists the cities of a state given as argument on one line. |
| `model_state.py` | The `State` class and the `Base`, mapped to the `states` table. |
| `7-model_state_fetch_all.py` | Lists all the `State` objects. |
| `8-model_state_fetch_first.py` | Prints the first `State` object, or `Nothing`. |
| `9-model_state_filter_a.py` | Lists the `State` objects containing the letter a. |
| `10-model_state_my_get.py` | Prints the id of the `State` matching a name, or `Not found`. |
| `11-model_state_insert.py` | Adds the state Louisiana and prints its id. |
| `12-model_state_update_id_2.py` | Changes the name of the state with id 2 to New Mexico. |
| `13-model_state_delete_a.py` | Deletes the states containing the letter a. |
| `model_city.py` | The `City` class, mapped to the `cities` table, linked to `states`. |
| `14-model_city_fetch_by_state.py` | Lists all the `City` objects with their state. |

## Usage

Every script takes the MySQL user, the password and the database name, in that order. Scripts 2, 3, 5 and 10 take a state
name as a fourth argument.

```
$ ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas
Dallas, Houston, Austin
$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
```

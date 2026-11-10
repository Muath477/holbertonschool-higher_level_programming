# Python - Server-Side Rendering

Pages built on the server with Flask and Jinja, then sent to the browser as
finished HTML. The data comes from JSON, CSV and SQLite.

## Files

| File | Description |
| --- | --- |
| `task_00_intro.py` | `generate_invitations(template, attendees)`: fills `template.txt` for each attendee and writes `output_1.txt`, `output_2.txt`, ... Missing values become `N/A`; bad or empty input writes nothing |
| `task_01_jinja.py` | `/`, `/about` and `/contact`, all sharing `header.html` and `footer.html` through `{% include %}` |
| `task_02_logic.py` | Adds `/items`, which lists `items.json` with a Jinja loop, or shows `No items found` |
| `task_03_files.py` | Adds `/products?source=json\|csv&id=N` using `products.json` or `products.csv` |
| `task_04_db.py` | Same route with `source=sql` reading the `Products` table of `products.db` |
| `create_database.py` | Creates `products.db` with the two sample products |
| `templates/` | `index`, `about`, `contact`, `items`, `product_display`, `header` and `footer` |

## Usage

```
$ pip install Flask
$ ./create_database.py
$ ./task_04_db.py
```

Then open `http://127.0.0.1:5000/products?source=sql&id=1`.

| Request | Result |
| --- | --- |
| `source` missing or unknown | `Wrong source` |
| `id` not in the data | `Product not found` |
| `products.db` missing or broken | `Database error` |

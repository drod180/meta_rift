# Meta-Rift Backend

### Running the server

Eventually, the backend will be entirely on AWS and will use environmental variables. In the meantime, the API can be set up and tested according to the following instructions.

#### Step 1: Editing Local Database Information

First, edit the files `src/controllers/champions.py`, `src/db/seeds.py`, and
 `test/model.py` according to the commented instructions in each file.

#### Step 2: Seed the Database with Champions

In `server/src/db`, run `python seeds.py`. (Instructions for updating
  columns coming soon).

#### Step 3: Starting the Server

In the `server` directory, run `gunicorn app`. This will start the server, and calls may be made to the API according to the routes as labeled in `app.py`

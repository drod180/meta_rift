# Meta-Rift Backend

### Running the server

Eventually, the backend will be entirely on AWS and will use environmental variables. In the meantime, the API can be set up and tested according to the following instructions.

#### Step 0: Local Database

Create a local Postgres database named 'metariftdevelopment'

#### Step 1: Setting up environment variables

The following environment variables are used:  
`api_key` - Riot API key to fetch data with.

Setting environment variables:  
**Windows**  
From the command line run as admin:  
`setx api_key "[KEY]"`
`setx metarift_user "[USERNAME]"`
`setx metarift_pwd "[PASSWORD]"`

Replace [KEY] with your Riot API key and replace [USERNAME] and [PASSWORD] with the credentials of a Postgres user with access to 'metariftdevelopment'.
Be sure to restart Powershell after using setx, as it won't take effect in your current session.

**Ubuntu**  
From the command line run:  
`export api_key=[KEY]`
`export metarift_user=[USERNAME]`
`export metarift_pwd=[PASSWORD]`

Replace [KEY] with your Riot API key and replace [USERNAME] and [PASSWORD] with the credentials of a Postgres user with access to 'metariftdevelopment'.  
This needs to be run on each restart/session, to keep it set add the above lines in your profile, e.g. .bash_profile, .zshrc, .bashrc, etc.


#### Step 2: Setup Test Files (optional)

Edit `test/model.py` according to the commented instructions.

#### Step 3: Seed the Database with Champions

In `server/src/db`, run `python seeds.py`. (Instructions for updating
  columns coming soon).

#### Step 4: Starting the Server

In the `server` directory, run `gunicorn app`. This will start the server, and calls may be made to the API according to the routes as labeled in `app.py`

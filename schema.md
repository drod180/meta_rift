# Schema Outline


#DB 1 (raw)

## Champions_in_matches
column name | data type | details
------------|-----------|-----------------------
id          | integer   | not null, primary key
champion_id | string    | not null, foreign key(references Champions)
match_id    | string    | not null
winner      | boolean   |
team        | string    | not null
role        | string    |

#DB 2 (prepped)

## Champions
column name      | data type | details
-----------------|-----------|-----------------------
id               | integer   | not null, primary key
name             | string    | not null
pick/ban rate    | integer   |
win rate         | integer   |
metascore        | integer   |
top              | integer   | not null
mid              | integer   | not null
jungle           | integer   | not null
marksman         | integer   | not null
support          | integer   | not null

image            | img       | not null

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
role             | string    | must be between 00000 and 11111
image            | img       | not null

NB: `role` above is a binary string with digits ordered by top-mid-jungle-marksman-support,
where the digit is 1 if the champion has had a certain minimum percentage of matches
played in the role and 0 otherwise.

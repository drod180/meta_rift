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
role             | integer   | binary rep must be between 00000 and 11111 (31)
image            | img       | not null

NB: the digits in the binary representation of `role` is ordered by
top-mid-jungle-marksman-support,
where the digit is 1 if the champion has had a certain minimum percentage of matches
played in the role (calculated from DB 1) and 0 otherwise.

# 1. Select all female bears and return their name and age
select_all_female_bears_return_name_and_age = """
SELECT name, age FROM bears WHERE sex = 'F';
"""

# 2. Select all bears' names and order them alphabetically
select_all_bears_names_and_orders_in_alphabetical_order = """
SELECT name FROM bears ORDER BY name ASC;
"""

# 3. Select all bears' names and ages that are alive, order from youngest to oldest
select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
SELECT name, age FROM bears WHERE alive = 1 ORDER BY age ASC;
"""

# 4. Select the oldest bear and return their name and age
select_oldest_bear_and_returns_name_and_age = """
SELECT name, age FROM bears ORDER BY age DESC LIMIT 1;
"""

# 5. Select the youngest bear and return their name and age
select_youngest_bear_and_returns_name_and_age = """
SELECT name, age FROM bears ORDER BY age ASC LIMIT 1;
"""

# 6. Select the bear that is alive is false (i.e., not alive)
select_bear_that_is_alive_is_false = """
SELECT * FROM bears WHERE alive = 0;
"""

# 7. Select the bear with the temperament ‘goofy’
select_bear_with_goofy_temperament = """
SELECT * FROM bears WHERE temperament = 'goofy';
"""

# 8. Select the bear with id = 8 (Tim’s killer)
select_bear_that_killed_Tim = """
SELECT * FROM bears WHERE id = 8;
"""

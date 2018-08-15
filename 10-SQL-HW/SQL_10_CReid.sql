USE sakila;

SELECT first_name, last_name
FROM actor;

#######
# 1A  #
ALTER TABLE actor
ADD COLUMN actor_name VARCHAR(35) AFTER last_name;

########
#  1B  #
SET SQL_SAFE_UPDATES = 0;

# Option 1 to concatenate
UPDATE actor
SET actor_name = CONCAT(first_name, " ", last_name);

#option 2 to concatenate
SELECT 
CONCAT(first_name,' ',last_name) actor_name
FROM actor;

#########
#  2A   #

SELECT  first_name, last_name, actor_id
FROM actor
WHERE first_name = "JOE";

#########
#  2B   #

SELECT * FROM actor
WHERE last_name LIKE "%GEN%";

#########
#  2C   #

SELECT * FROM actor
WHERE last_name LIKE "%LI%"
ORDER BY last_name ASC, first_name ASC;

#########
#  2D   #

SELECT country, country_id
FROM country
WHERE country IN ("Afghanistan", "Bangladesh", "China");

#########
#  3A   #
ALTER TABLE actor
ADD COLUMN description BLOB AFTER actor_name;

#########
#  3B   #
ALTER TABLE actor
DROP COLUMN description;

#########
#  4A   #
SELECT last_name, COUNT(*)
FROM actor
GROUP BY last_name;

#########
#  4B   #
SELECT last_name, COUNT(*)
FROM actor
GROUP BY last_name
HAVING COUNT(*) >= 2;

#########
#  4C   #
UPDATE actor
SET first_name = "HARPO"
WHERE last_name = "WILLIAMS" AND first_name = "GROUCHO";

#########
#  4D   #
UPDATE actor
SET first_name = "GROUCHO"
WHERE last_name = "WILLIAMS" AND first_name = "HARPO";

#########
#  5A   #
SHOW CREATE TABLE address;

#########
#  6A   #
SELECT 
	staff.first_name,
    staff.last_name,
    address.address,
    address.postal_code,
    address.city_id,
    address.address_id,
    staff.address_id
FROM staff
INNER JOIN address
ON address.address_id = staff.address_id;

#########
#  6B   #
SELECT  staff.first_name, staff.last_name, SUM(payment.amount) AS "total_payments"
FROM payment
INNER JOIN staff
ON payment.staff_id = staff.staff_id
WHERE MONTH(payment.payment_date) = 8 AND YEAR(payment.payment_date)=2005
GROUP BY payment.staff_id;

#########
#  6C   #
SELECT film.title, COUNT(film_actor.actor_id) AS actor_count
FROM film
INNER JOIN film_actor
ON film.film_id = film_actor.film_id
GROUP BY film.title;

#########
#  6D   #
SELECT film.title, SUM(inventory.film_id) AS inventory_count
FROM film
INNER JOIN inventory
ON inventory.film_id = film.film_id
WHERE film.title = "Hunchback Impossible";

#########
#  6E   #
SELECT customer.first_name, customer.last_name, SUM(payment.amount) AS total_payment
FROM customer
INNER JOIN payment
ON customer.customer_id = payment.customer_id
GROUP BY customer.customer_id
ORDER BY last_name ASC, first_name ASC;

#########
#  7A   #
SELECT title
FROM film
WHERE title LIKE "K%" OR title LIKE "Q%"
ORDER BY title ASC;

#########
#  7B   #
SELECT first_name, last_name
FROM actor
WHERE actor_id IN (

	SELECT actor_id
	FROM film_actor
	WHERE film_id IN (

		SELECT film_id 
		FROM film
		WHERE title = "Alone Trip"
		)
	);

#########
#  7C   #
SELECT c.first_name, c.last_name, c.email
FROM customer c
JOIN address a ON a.address_id = c.address_id
JOIN city ON a.city_id = city.city_id
JOIN country ON country.country_id = city.country_id 
WHERE country = "Canada";

#########
#  7D   #
SELECT film.title
FROM film
WHERE film_id IN(

	SELECT film_category.film_id
	FROM film_category
	WHERE category_id IN(

		#CREATE VIEW family_films AS
		SELECT category_id
		FROM category
		WHERE category_id = 2 OR category_id = 3 OR category_id = 8
		)
	)
ORDER BY title ASC;

#########
#  7E   #
# Display the most frequently rented movies in descending order.
SELECT film.title, COUNT(rental.rental_id) AS rental_frequency
FROM rental
	JOIN inventory ON rental.inventory_id = inventory.inventory_id
		JOIN fiLm ON film.film_id = inventory.film_id
GROUP BY film.title
ORDER BY rental_frequency DESC;

#########
#  7F   #
#7f. Write a query to display how much business, in dollars, each store brought in.
SELECT store.store_id, sum(payment.amount) AS "total_sales"
FROM store
	JOIN staff ON store.store_id = staff.store_id
			JOIN payment ON payment.staff_id = staff.staff_id
GROUP BY store.store_id;

#########
#  7G   #
#7g. Write a query to display for each store its store ID, city, and country.
SELECT store.store_id, city.city, country.country
FROM store
	JOIN address ON store.address_id = address.address_id
		JOIN city on address.city_id = city.city_id
			JOIN country ON city.country_id = country.country_id
	;

#########
#  7H   #
##List the top five genres in gross revenue in descending order. 
#(**Hint**: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
SELECT category.name AS "Genre", sum(payment.amount) AS "Total Sales"
FROM payment
	JOIN rental ON payment.rental_id = rental.rental_id
		JOIN inventory ON rental.inventory_id = inventory.inventory_id
			JOIN film_category ON inventory.film_id = film_category.film_id
					JOIN category ON film_category.category_id = category.category_id
GROUP BY Genre 
ORDER BY "Total Sales" DESC
LIMIT 5;

#########
#  8A   #
# In your new role as an executive, you would like to have an easy way of viewing the 
#Top five genres by gross revenue. Use the solution from the problem above to create a view. 
#If you haven't solved 7h, you can substitute another query to create a view.
CREATE VIEW topFiveGenres AS
SELECT category.name AS "Genre", sum(payment.amount) AS "Total Sales"
FROM payment
	JOIN rental ON payment.rental_id = rental.rental_id
		JOIN inventory ON rental.inventory_id = inventory.inventory_id
			JOIN film_category ON inventory.film_id = film_category.film_id
					JOIN category ON film_category.category_id = category.category_id
GROUP BY Genre 
ORDER BY "Total Sales" DESC
LIMIT 5;

#########
#  8B   #
#How would you display the view that you created in 8a?
SELECT * from topFiveGenres;

#########
#  8C   #
#You find that you no longer need the view top_five_genres. Write a query to delete it.
DROP VIEW topFiveGenres;


select * from inventory;

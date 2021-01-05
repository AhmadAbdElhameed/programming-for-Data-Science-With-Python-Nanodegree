/*
Question Set #1:
*/

/*
Question 2
Now we need to know how the length of rental duration of these family-friendly movies compares to the duration that all movies are rented for.
 Can you provide a table with the movie titles and divide them into 4 levels (first_quarter, second_quarter, third_quarter, and final_quarter) 
based on the quartiles (25%, 50%, 75%) of the rental duration for movies across all categories? Make sure to also indicate the category that 
these family-friendly movies fall into.
*/
SELECT film.title,
       category.name AS category,
       film.rental_duration,
       NTILE(4) OVER(ORDER BY film.rental_duration) AS quartile
FROM category
JOIN film_category 
ON category.category_id = film_category.category_id
JOIN film
ON film.film_id = film_category.film_id
WHERE category.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')



/*
Question Set #2:
*/

/*
Question 1:
We want to find out how the two stores compare in their count of rental orders during every month for all the years we have data for. 
*/

SELECT DATE_PART('month',rental.rental_date) AS Rental_month, DATE_PART('year',rental.rental_date) AS Rental_year, staff.store_id,
count(*) AS dvd_count_rentals
FROM rental
JOIN staff
ON rental.staff_id = staff.staff_id
GROUP BY 1,2,3
ORDER BY dvd_count_rentals DESC;



/*
Question 2:
We would like to know who were our top 10 paying customers, how many payments they made on a monthly basis during 2007, 
and what was the amount of the monthly payments. Can you write a query to capture the customer name, month and year of 
payment, and total payment amount for each month by these top 10 paying customers?
*/


WITH results AS (SELECT DATE_TRUNC('month',p.payment_date) AS pay_mon,
          				c.first_name || ' ' || c.last_name AS full_name,
          				COUNT(*) AS pay_counterpermon, SUM(p.amount) AS pay_amount
          				FROM PAYMENT AS p
          				JOIN CUSTOMER AS c
          				ON p.customer_id = c.customer_id
          				WHERE DATE_TRUNC('month',p. payment_date) > '2007-01-01'
          				GROUP BY 1,2
          				ORDER BY full_name),

    	    top AS (SELECT c.first_name || ' ' || c.last_name AS full_name,
          				SUM(p.amount) AS pay_amount
          				FROM PAYMENT AS p
          				JOIN CUSTOMER AS c
          				ON p.customer_id = c.customer_id
          				GROUP BY 1
          				ORDER BY pay_amount DESC
          				LIMIT 10)

SELECT r.pay_mon, r.full_name, r.pay_counterpermon, r.pay_amount
FROM results AS r
JOIN top AS t
ON r.full_name = t.full_name
ORDER BY full_name, pay_mon;




/*
Question 3:
Finally, provide a table with the family-friendly film category, each of the quartiles, and the corresponding count of movies within each combination
of film category for each corresponding rental duration category. The resulting table should have three columns:
Category
Rental length category
Count
*/


SELECT country.country,
      COUNT(customer_id) AS customer_ct,
      CASE WHEN COUNT(customer_id) < 15 THEN 'low'
           WHEN COUNT(customer_id) < 30 THEN 'medium'
           WHEN COUNT(customer_id) < 45 THEN 'high'
           ELSE 'very high' END AS customer_ct_level
FROM country
JOIN city 
ON country.country_id = city.country_id
JOIN address 
ON city.city_id = address.city_id
JOIN customer 
ON address.address_id = customer.address_id
GROUP BY 1
ORDER BY 2 DESC



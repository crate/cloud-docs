(full-text)=

# Full-Text: Exploring the Netflix Catalog

CrateDB is an exceptional choice for handling complex queries and large-scale
data sets. One of its standout features is its full-text search capabilities,
built on top of the powerful Lucene library. This makes it a great fit for
organizing, searching, and analyzing extensive datasets.

In this tutorial, we will explore how to manage a dataset of Netflix titles,
making use of CrateDB Cloud's full-text search capabilities.
Each entry in our imaginary dataset will have the following attributes:

- `show_id`: A unique identifier for each show or movie.
- `type`: Specifies whether the title is a movie, TV show, or another format.
- `title`: The title of the movie or show.
- `director`: The name of the director.
- `cast`: An array listing the cast members.
- `country`: The country where the title was produced.
- `date_added`: A timestamp indicating when the title was added to the catalog.
- `release_year`: The year the title was released.
- `rating`: The content rating (e.g., PG, R, etc.).
- `duration`: The duration of the title in minutes or seasons.
- `listed_in`: An array containing genres that the title falls under.
- `description`: A textual description of the title, indexed using full-text search.

To begin, let's create the schema for this dataset:

## Creating the Table

CrateDB uses SQL, a powerful and familiar language for database management. To
store our weather data, we'll create a table with columns tailored to our
dataset using the `CREATE TABLE` command. Importantly, we'll also take advantage
of CrateDB's full-text search capabilities by setting up a full-text index on
the description column. This will enable us to perform complex textual queries
later on.

```sql
CREATE TABLE "netflix_catalog" (
   "show_id" TEXT PRIMARY KEY,
   "type" TEXT,
   "title" TEXT,
   "director" TEXT,
   "cast" ARRAY(TEXT),
   "country" TEXT,
   "date_added" TIMESTAMP,
   "release_year" TEXT,
   "rating" TEXT,
   "duration" TEXT,
   "listed_in"  ARRAY(TEXT),
   "description" TEXT INDEX using fulltext
);
```

Run the above SQL command in CrateDB to set up your table. With the table ready, 
you’re now set to insert the dataset.

## Inserting Data
With the table created we can now insert the data using the COPY FROM command by
using the table we just created and the source for our movie data:

```sql
COPY netflix_catalog
FROM 'https://github.com/crate/cratedb-datasets/raw/main/cloud-tutorials/data_netflix.json.gz'
WITH (format = 'json', compression='gzip');
```

Run the above SQL command in CrateDB to import the dataset. After this commands 
finishes, we are now ready to start searching in our dataset.

## Using Full-text Search

Let us start with a simple SELECT on all columns and limiting the output to 10 
results by running the following:

```sql
SELECT *
FROM netflix_catalog
LIMIT 10;
```

This gives us a glimpse into the kind of data we are dealing with.


CrateDB Cloud’s full-text search can be leveraged to find specific entries based
on text matching. In this query, we are using the `MATCH` function on the
`description` field to find all movies or TV shows that contain the word "love".
We then sort the results by relevance score, which is provided by the
`_score` field.

```sql
SELECT title, description
FROM netflix_catalog
WHERE MATCH(description, 'love')
ORDER BY _score DESC
LIMIT 10;
```

While full-text search is incredibly powerful, you can still perform more
traditional types of queries. For example, to find all titles directed by
"Kirsten Johnson", and sort them by release year, you can use:

```sql
SELECT title, release_year
FROM netflix_catalog
WHERE director = 'Kirsten Johnson'
ORDER BY release_year DESC;
```

This query uses the conventional `WHERE` clause to filter entries directed by 
Kirsten Johnson, and the `ORDER BY` clause to sort them by their release year
in descending order.

Through these examples, you can see that CrateDB Cloud offers you a wide array
of querying possibilities, from basic SQL queries to advanced full-text
searches, making it a versatile choice for managing and querying your datasets.
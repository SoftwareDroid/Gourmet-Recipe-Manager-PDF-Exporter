from search import SearchQuery
from customizing.parition_filter import time_partition, only_tag, partition_after_tag


queries = list()

# Define own search queries
queries.append(SearchQuery("Recipes After Cuisine", lambda r: r.cuisine(), lambda r: r[0].title()))
queries.append(SearchQuery("Favorites Recipes", only_tag("favorite"), lambda r: r[0].title()))
queries.append(SearchQuery("Vegetarian Partition", partition_after_tag("vegetarian"), lambda r: r[0].title()))
queries.append(SearchQuery("Time Partition", time_partition, lambda r: r[0].title()))
print("|||||||||| Installing the devtools package ||||||||||||")
# install the devtools package
install.packages("devtools",repos="http://cran.rstudio.com/")
library(devtools)

print("|||||||||| Installing the Interana Query SDK ||||||||||||")
# install the interana query sdk directly from the github repo
install_github("Interana/interana-sdk/query_sdk/R/interana.query.client")
library(interana.query.client)

print("")

# now use the interana query sdk
print(">>>>>>>>> Triggering a test query against Interana Cluster >>>>>>>>>>>")
print("+++++++++ Creating the Interana Client Object ++++++++")
interana_client("demo2.interana.com","tffZR6q0fbVqSBbeuvvLllLMLV0KHbuH+/DjXo9K=ER0PY/qNh+hdjEh+16DcL5Gc=BfHTJ7dE64x06YFWMbtbqtcdO90000")
print("+++++++++ Defining the Interana Query Object ++++++++")
interana_query("music",100)
print("+++++++++ Inserting a filter criteria and also doing a group by ++++++++")
interana_add_query_params(filter_expr = '(`artist` startswith "Cat")', group_by_column = "artist")
print("+++++++++ Retrieving Interana Query Params +++++++++++")
interana_get_params()
print("========= Retrieving Interana Query Params ===========")
interana_get_data()
print("<<<<<<<<< Completed test query execution. Fork away! <<<<<<<<<<<<<<<<<")

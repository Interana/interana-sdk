#' @import chron
#' @import httr
#' @import rjson

# Global Variables
pkg.env <- new.env()

pkg.env$interana_host <- ""
pkg.env$auth_token <- ""

pkg.env$dataset <- ""
pkg.env$days_prior <- 0

pkg.env$query_type <- ""
pkg.env$aggregator_type <- ""
pkg.env$aggregator_column <- ""
pkg.env$filter_expression <- ""
pkg.env$group_by_column <- ""

#' Establish the Interana Client Connection
#'
#' This function allows you to establish the Interana Client Connection
#' @param cluster_host Specify the cluster domain. For eg. https://<cluster-domain>/login.html. This is usually the name of your company or POC with a suffix of .interana.com.
#' @param token Provide the authorization token to validate access to the cluster above.
#' @keywords interana
#' @export
#' @examples
#' interana_client()
 
interana_client <- function(cluster_host="",token=""){
	print(paste("You have provided the cluster host as:",cluster_host,"& authorization token:",token))
  pkg.env$interana_host <- cluster_host
  pkg.env$auth_token <- token
}

#' Formulate the Interana Query 
#'
#' This function allows you to define the Interana Query
#' @param dataset Specify the Interana dataset to query against
#' @param days_prior Specify the interval to search against. In other words: end_time: now, start_time: now-days_prior
#' @keywords interana
#' @export
#' @examples
#' interana_query()

interana_query <- function(dataset="",days_prior=7){
  print(paste("Defining Query for Dataset:",dataset,"for Days Prior (to now): ",days_prior))
  pkg.env$dataset <- dataset
  pkg.env$days_prior <- days_prior
}

#' Add Interana Query Params
#'
#' This function allows you to further specify Interana Query Params
#' @param query_type Specify the Interana query type. Default=single_measurement. More details at TBD
#' @param agg_type Specify the Interana aggregator type. Default=count_star. More details at TBD
#' @param agg_column Specify the aggregator column, if any. This is dependent on the aggregator type. Default=null. More details at TBD
#' @param filter_expr Specify the filter criteria, if any. This is an URL-escaped value (example: TBD) Default=null. More details at TBD
#' @param group_by_column Specify the group by column. Default=null. More details at TBD
#' @keywords interana
#' @export
#' @examples
#' interana_add_query_params()

interana_add_query_params <- function(query_type="single_measurement",agg_type="count_star",agg_column="",filter_expr="",group_by_column=""){
  print(paste("Adding Query Params ..."))
  pkg.env$query_type <- query_type
  pkg.env$aggregator_type <- agg_type
  pkg.env$aggregator_column <- agg_column
  pkg.env$filter_expression <- filter_expr
  pkg.env$group_by_column <- group_by_column
  print(paste("Completed Adding Query Params ."))
}

#' Gets the parameters that are set so far
#'
#' This function shows all the parameters set so far.
#' @keywords get_params
#' @export
#' @examples
#' interana_get_params()

interana_get_params <- function(){
	print("----------Dumping Query Client Params ------")
  print(paste("Interana cluster:",pkg.env$interana_host))
  print(paste("Authorization Token:",pkg.env$auth_token))
  print(paste("Dataset:",pkg.env$dataset))
  print(paste("Days Prior:",pkg.env$days_prior))
  print(paste("Query Type:",pkg.env$query_type))
  print(paste("Aggregator Type:",pkg.env$aggregator_type))
  print(paste("Aggregator Column:",pkg.env$aggregator_column))
  print(paste("Filter Expression:",pkg.env$filter_expression))
  print(paste("Group By Column:",pkg.env$group_by_column))
  print("----------End Params Dump ------")
}

#' Retrieve the Interana Results from previously formulated data
#'
#' This function allows you to retrieve data from previously defined query
#' @keywords interana
#' @export
#' @examples
#' interana_get_data()

interana_get_data <- function(){
  print("Retrieving the Interana Data ...")
  end_time <- as.chron(Sys.time())
  start_time <- end_time - pkg.env$days_prior
  query_item = list("type" = pkg.env$query_type,
                    "measure"=list("aggregator" = pkg.env$aggregator_type,
                                   "column" = pkg.env$aggregator_column))

  if ( pkg.env$filter_expression != "" ){
    # now set the filter criteria as found
    query_item$filter <- pkg.env$filter_expression
  }
  else{
    query_item$filter <- ''
  }
  
  params <- list("end"=as.integer( as.POSIXct( end_time ), 
                                   tz = "UTC" )*1000, 
                 "start" = as.integer( as.POSIXct( start_time ), 
                                       tz = "UTC" )*1000, 
                 "dataset" = pkg.env$dataset, 
                 "queries" = list(query_item))
  
  if (pkg.env$group_by_column != ""){
    #print(pkg.env$group_by_column)
    params$group_by <- list(pkg.env$group_by_column)
  }
  
  cluster_url <- paste("https://",pkg.env$interana_host,"/api/v1/query",sep = "")
  auth_token = paste("Token",pkg.env$auth_token)
  
  #print(cluster_url)
  #print(auth_token)
  #print(paste("query=",URLencode(toJSON(params)),sep = ""))
  r <- GET(cluster_url, accept_json(), 
           add_headers('Authorization' = auth_token), 
           query = paste("query=",URLencode(toJSON(params)),sep = ""))

  response <- fromJSON(content(r,as = "text"))
  print(as.data.frame(response))

  print("Retrieved the Interana Data !")
}

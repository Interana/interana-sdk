#!/usr/bin/env python

import json
import datetime
import argparse
import ast
import os

from python.interana_query_sdk import Client, Query

def get_interana_data(token,url,days_prior,dataset,query_type,agg_type,
			verbose_mode=False, groupby_col='', 
			filter_expr='', output_file='', ia_col=''):
	if verbose_mode:
		print "Vars passed to get_interana_data: ", token,url,days_prior,dataset,query_type,agg_type,ia_col,verbose_mode

	client = Client(url, token)
	if verbose_mode:
		print client

	end_time = datetime.datetime.now()
	start_time = end_time - datetime.timedelta(days=days_prior)
	query = Query(dataset, start_time, end_time)
	if filter_expr:
		#filter = "(`event` != \"userlogin\")"
		query.add_query_info(type=query_type, aggregator=agg_type, column=ia_col, filter=filter_expr)
	else:
		query.add_query_info(type=query_type,aggregator=agg_type,column=ia_col)

	if groupby_col:
		query.add_params(group_by=[groupby_col])

	if verbose_mode:
		print "Query Params: ", query.get_params()

	result = client.query(query)
	if verbose_mode:
		print result

	if output_file:
		print "-----------------------\nWriting out results to file..."
		with open(output_file,"w") as fout:
			fout.write(json.dumps(ast.literal_eval(str(result))))
			fout.write("\n")
		print "Results now available in file: %s.\n----------------------" % output_file

	else:
		print "-------------------------------------------\nResults recieved from" + \
			 " Interana:\n-------------------------------------------\n%s" % result
		print "-------------------------------------------\nEnd of Results" + \
			"\n-------------------------------------------\n"

def setup_args():
    """Adds additional ARGS to allow the Token, Cluster URL, 
    and other params to be provided.
    """
    parser = argparse.ArgumentParser(description='Arguments for talking to Interana APIs')
    parser.add_argument('auth_token', help='Token issued by Interana Customer Support')
    parser.add_argument('cluster_domain',
                        help='Domain used to access the Interana Cluster')
    parser.add_argument('dataset', help='Dataset to query from')

    parser.add_argument('-d', '--days_prior', help='Days Prior to now to query from (Default: 1000)', default=1000)
    parser.add_argument('-t', '--query_type', help='Query Type (default: single_measurement)', default='single_measurement')
    parser.add_argument('-a', '--aggregator', help='Aggregator to use for the Query (default: count_star)', default='count_star')
    parser.add_argument('-c', '--column_name', help='Column to be used for the Query (default: "")', default='')

    parser.add_argument('-g', '--group_by', help='Column to be used for the Group By (default: "")', default='')
    parser.add_argument('-f', '--filters', help='Filter expression to be used.\nFor eg. \'(`event` != "userlogin")\' (default: "")', default='')
    parser.add_argument('-o', '--output_file', help='Output File to be used for storing results. (default: "")', default='')

    parser.add_argument('-v', '--verbose', help='Verbose Mode ; Provide more debugging logs', default=False, action='store_true')

    args = parser.parse_args()

    return args

def main():
    args = setup_args()

    if args.verbose:
    	print args

    #now call the downstream method to retrieve the data
    get_interana_data(token=args.auth_token, url=args.cluster_domain,
	days_prior=int(args.days_prior), dataset=args.dataset,
	query_type=args.query_type, agg_type=args.aggregator,
        verbose_mode=args.verbose, groupby_col=args.group_by, 
        filter_expr=args.filters, output_file=args.output_file,
	ia_col=args.column_name)

if __name__ == '__main__':
    main()


#!/bin/bash
echo "processing file : $1 for document type : $2"
INPUT=$1
OLDIFS=$IFS
IFS=','
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read customer_id account_number created_at lender Amount 
do
    echo "processing account : $account_number, lender :$lender, cid :$customer_id, amount:$Amount"
	NOW1=$(date +"%Y-%m-%d %H:%M:%S")
	curl -X POST \
    'http://localhost:30000/debug/add/bitxn' \
    -H 'Content-Type: application/json' \
    -d'{"customerId": '\"${customer_id}\"',"amount": '${Amount}',"lender": '\"${lender}\"',"transactionDate": '\"${NOW1}\"',"accountId": '\"${account_number}\"'}'
done < $INPUT
IFS=$OLDIFS


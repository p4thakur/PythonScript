#!/bin/bash
echo "processing file : $1 for document type : $2"
INPUT=$1
OLDIFS=$IFS
IFS=','
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read loan_account_number cif_id customer_id
do
    echo "processing account : $loan_account_number, cif :$cif_id, cid :$customer_id"
    curl --location --request GET "localhost:9010/lms/account/document/notify/$2?sendEmail=false&sendSms=false" --header "x-user-id: $customer_id" --header "cif: $cif_id" --header "lan: $loan_account_number"
done < $INPUT
IFS=$OLDIFS

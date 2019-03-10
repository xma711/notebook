#!/usr/bin/env python

import os
from dotenv import load_dotenv
from azure.storage.blob import BlockBlobService

load_dotenv('./.env')

_account_name = os.getenv('AZURE_ACCOUNT_NAME')
_account_key = os.getenv('AZURE_ACCOUNT_KEY')
_sas_token = os.getenv('AZURE_SAS_KEY')

if _account_key and _sas_token:
	print ("account key and sas token cannot both be set. please remove one of them first.")
	exit(1)

_block_blob_service = BlockBlobService(
	account_name=_account_name,
	account_key = _account_key,
	sas_token = _sas_token)


def get_file_list(container_name, prefix=None):
	has_results = True
	next_marker = None

	while has_results:
		blob_list = _block_blob_service.list_blobs(
				container_name,
				prefix=prefix,
				marker=next_marker)

		for b in blob_list:
			yield b.name
		if blob_list.next_marker:
			next_marker = blob_list.next_marker
			has_results = True
		else:
			has_results = False

container_name = 'blobstest'

file_list = get_file_list(container_name)
print ("file_list obtained from container {} is {}".format(container_name, file_list))
for f in file_list:
	print ('{}'.format(f))

from database import BUCKET_NAME, s3_client, supabase
import time
from unstructured.partition.pdf import partition_pdf
from unstructured.partition.docx import partition_docx
from unstructured.partition.html import partition_html
import os
import logging

elements =  partition_pdf(
    filename="C:\\Users\\dmanishgandhi\\Downloads\\attention-is-all-you-need.pdf",  # Path to your PDF file
    strategy="hi_res", # Use the most accurate (but slower) processing method of extraction
    infer_table_structure=True, # Keep tables as structured HTML, not jumbled text
    extract_image_block_types=["Image"], # Grab images found in the PDF
    extract_image_block_to_payload=True # Store images as base64 data you can actually use
)
print(elements)

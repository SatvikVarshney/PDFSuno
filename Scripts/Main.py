import boto3
import time

def upload_file_to_s3(file_name, bucket_name, object_name=None):
    """
    Upload a file to an S3 bucket.

    :param file_name: File to upload.
    :param bucket_name: Name of the S3 bucket.
    :param object_name: S3 object name. If not specified, file_name is used.
    :return: True if file was uploaded, else False.
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket_name, object_name)
    except Exception as e:
        print(f"Error uploading file: {e}")
        return False
    return True

def start_document_text_detection(bucket_name, document):
    """
    Start document text detection using Amazon Textract.

    :param bucket_name: Name of the S3 bucket.
    :param document: Document name in the bucket.
    :return: Job ID of the started Textract job.
    """
    textract = boto3.client('textract', region_name='us-east-1')
    try:
        response = textract.start_document_text_detection(
            DocumentLocation={'S3Object': {'Bucket': bucket_name, 'Name': document}}
        )
    except Exception as e:
        print(f"Error starting text detection: {e}")
        return None
    return response['JobId']

def is_job_complete(job_id):
    """
    Check if the Textract job is complete.

    :param job_id: Job ID to check.
    :return: Tuple of (completion status, response).
    """
    textract = boto3.client('textract', region_name='us-east-1')
    try:
        response = textract.get_document_text_detection(JobId=job_id)
        status = response["JobStatus"]
        if status == "SUCCEEDED":
            return True, response
        elif status == "FAILED":
            print("Job failed.")
            return False, response
        else:
            return False, response
    except Exception as e:
        print(f"Error checking job status: {e}")
        return False, None

def get_job_results(job_id):
    """
    Get the results of a completed Textract job.

    :param job_id: Job ID to get results for.
    :return: List of blocks representing the document content.
    """
    pages = []
    textract = boto3.client('textract', region_name='us-east-1')
    response = textract.get_document_text_detection(JobId=job_id)
    pages.extend(response["Blocks"])
    while "NextToken" in response:
        response = textract.get_document_text_detection(JobId=job_id, NextToken=response["NextToken"])
        pages.extend(response["Blocks"])
    return pages

def extract_text_from_blocks(blocks):
    """
    Extract text from Textract blocks.

    :param blocks: List of Textract blocks.
    :return: Extracted text.
    """
    return "\n".join([block["Text"] for block in blocks if block["BlockType"] == "LINE"])

def translate_text(text, source_lang, target_lang):
    """
    Translate text using Amazon Translate.

    :param text: Text to translate.
    :param source_lang: Source language code.
    :param target_lang: Target language code.
    :return: Translated text.
    """
    translate_client = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)
    try:
        result = translate_client.translate_text(Text=text, SourceLanguageCode=source_lang, TargetLanguageCode=target_lang)
    except Exception as e:
        print(f"Error translating text: {e}")
        return None
    return result.get('TranslatedText')

def synthesize_speech(text, output_file, voice_id='Aditi', language_code='hi-IN'):
    """
    Synthesize speech using Amazon Polly.

    :param text: Text to synthesize.
    :param output_file: Output file to save synthesized speech.
    :param voice_id: Polly voice ID to use.
    :param language_code: Language code for the speech.
    """
    polly_client = boto3.client(service_name='polly', region_name='us-east-1', use_ssl=True)
    try:
        response = polly_client.synthesize_speech(VoiceId=voice_id, OutputFormat='mp3', Text=text, LanguageCode=language_code)
        with open(output_file, 'wb') as file:
            file.write(response['AudioStream'].read())
    except Exception as e:
        print(f"Error synthesizing speech: {e}")


# Example usage:
bucket_name = 'your-s3-bucket-name'
document_name = 'your-document.pdf'
translated_output_file = 'speech.mp3'

# Upload file to S3
upload_successful = upload_file_to_s3('your-local-file-path.pdf', bucket_name, document_name)
if not upload_successful:
    print("Failed to upload file to S3.")
    exit()

# Start Textract job
job_id = start_document_text_detection(bucket_name, document_name)
if job_id is None:
    print("Failed to start Textract job.")
    exit()

# Wait for Textract job to complete
while True:
    job_complete, response = is_job_complete(job_id)
    if job_complete:
        break
    elif response is None or response["JobStatus"] == "FAILED":
        print("Textract job failed or encountered an error.")
        exit()
    else:
        print("Job is still in progress. Waiting before checking again...")
        time.sleep(10)

# Get Textract job results
results = get_job_results(job_id)

# Extract text
text = extract_text_from_blocks(results)
print(text)

# Translate text to Hindi
hindi_text = translate_text(text, 'en', 'hi')
if hindi_text is None:
    print("Failed to translate text.")
    exit()

print(hindi_text)

# Synthesize speech
synthesize_speech(hindi_text, translated_output_file)
print(f"Speech synthesized and saved to {translated_output_file}.")

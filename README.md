# PDF Suno

PDF Suno is an under-progress project aimed at converting English PDFs and Ebooks into Hindi audiobooks. This initiative targets the underprivileged and under-educated populations in India who lack access to reading and writing due to educational deficiencies and language barriers. The project facilitates access to information in an audio format, making it comprehensible for those who previously found it challenging due to their limitations.

## Overview

PDF Suno transforms the way we engage with documents by enabling seamless conversion of textual content into audio format. The application leverages cutting-edge AI technologies such as AWS Textract, Translate, and Polly, to extract, translate, and synthesize text from PDFs into high-quality Hindi audiobooks. The development strategy involves utilizing pre-existing training datasets, integrating TTS cloud services, and employing translation services to streamline the process cost-effectively and efficiently. This tool aims to empower Hindi-speaking audiences, especially those from underprivileged backgrounds, by providing access to educational and informational content in a user-friendly audio format.



## Sample Demonstration Overview





## Key Features

### Current Features:

1. **PDF Document Upload:** PDF Suno allows for secure uploading of PDF files, enabling users to handle multiple documents at once. This feature broadens the application's context and ensures accurate responses.

2. **Efficient Text Extraction:** Utilizing AWS Textract, PDF Suno extracts text from uploaded PDFs efficiently, laying the groundwork for informed translations and audio synthesis.

3. **Text Translation:** Leveraging AWS Translate, PDF Suno translates extracted text from English to Hindi, catering to users who prefer or require Hindi content.

4. **Audio Synthesis:** Using AWS Polly, PDF Suno synthesizes Hindi text into high-quality audio, creating an accessible and convenient audiobook format.

### Planned Enhancements

1. **Move to GCP:** Based on reviews Google Cloud Platform offers superior quality text extraction, translation, and TTS compared to aws. This move could improve quality in all these areas.

2. **Expanded Language Support:** Future updates will include support for additional languages, broadening the application's accessibility.

3. **Enhanced Audio Quality:** Improvements will focus on enhancing the quality and naturalness of synthesized audio, offering a superior listening experience. Emphasis may be placed on creating a local TTS software for Hindi. 

4. **User Interface Improvements:** The aim is to enhance the application's user interface for a more intuitive and seamless experience.

5. **Improved Extraction:** Local extraction including OCR will allow for a more cost effective solution.


## How It Works

1. **Document Upload:** Users upload their PDF documents directly through the application interface. PDF Suno accepts multiple documents simultaneously, enriching the contextual processing.

2. **Text Extraction:** Once uploaded, the documents are processed to extract text using AWS Textract. 

3. **Text Translation:** The extracted text is then translated into Hindi using AWS Translate.

4. **Audio Synthesis:** Finally, the translated text is converted into audio using AWS Polly, creating a Hindi audiobook.

## Technologies Used

1. **Boto3:** For interacting with AWS services such as Textract, Translate, and Polly.
2. **Python:** The core programming language used for the application logic.
3. **AWS Textract:** Utilized for the extraction of text from PDF documents.
4. **AWS Translate:** Used for translating text from English to Hindi.
5. **AWS Polly:** Powers the text-to-speech synthesis for creating audiobooks.

## Getting Started

### Installation

Clone the repository to get started:

```bash
git clone https://github.com/SatvikVarshney/PDFSuno.git
```

Navigate to the project directory:
```bash
cd PDF-Suno
```
Install the required Python packages:
```bash
pip install -r requirements.txt
```

To run PDF Suno on your local machine, clone the repository and ensure you have the necessary AWS credentials configured. Use the following command to launch the application:
```bash
python pdf_suno.py
```


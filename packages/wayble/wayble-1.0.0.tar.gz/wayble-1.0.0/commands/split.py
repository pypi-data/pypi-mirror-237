import json
import click

from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


@click.command()
@click.argument('input_file', type=click.Path(exists=True, readable=True))
@click.argument('output_file', type=click.Path(writable=True))
@click.option('--size', default=512, type=int, help="size of the chunks to split the text into. (512)")
@click.option('--overlap', default=128, type=int, help="number of overlapping characters between chunks. (128)")
def split(input_file: str, output_file: str, size: int, overlap: int) -> None:
    """
    Splits text from the input file into chunks and writes the result to the output file in JSON format.

    [INPUT_FILE] is the file from which text will be read.

    [OUTPUT_FILE] is the file to which the chunks will be saved.
    """
    loader = TextLoader(input_file)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_overlap=overlap, chunk_size=size)

    # Split the documents into chunks
    docs = text_splitter.split_documents(documents)

    # Extract page content from each document
    docs_list = [doc.page_content for doc in docs]

    # Save the split text chunks in JSON format
    with open(output_file, 'w') as f:
        json.dump(docs_list, f)

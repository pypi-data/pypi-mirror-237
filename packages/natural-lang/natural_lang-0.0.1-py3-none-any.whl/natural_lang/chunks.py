import re
import tiktoken

def num_tokens_from_string(string: str, model_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def split_into_paragraphs(input_string:str) -> list[str]:
    """
    Splits an input text into paragraphs, preserving asterisks as dividers.
    
    Args:
        input_string (str): The input text.
    
    Returns:
        list[str]: A list of the resulting paragraphs.
    """
    # Split by double newline or one asterisk
    paragraphs = re.split(r'\n|\*', input_string)
    # Filter out empty strings from the result
    paragraphs = [paragraph.strip() for paragraph in paragraphs if paragraph.strip()]
    return paragraphs


def divide_into_chunks(input_string: str, max_text_length: int, model_name: str) -> list[str]:
    """
    Combines paragraphs into chunks that do not exceed the specified token limit.
    
    Args:
        input_string (str): The input text.
        max_text_length (int): Maximum token limit for each chunk.
    
    Returns:
        list[str]: A list of chunks.
    """
    paragraphs = split_into_paragraphs(input_string)
    
    # Initialize variables
    chunks = []
    current_chunk = ''
    # Iterate through paragraphs and create chunks
    for paragraph in paragraphs:
        # Check if adding the current paragraph to the chunk exceeds the QUERY_LIMIT
        len_current_chunk = num_tokens_from_string(current_chunk, model_name)
        len_next_paragraph = num_tokens_from_string(paragraph, model_name)
        if len_current_chunk + len_next_paragraph <= max_text_length:
            # Add the paragraph to the current chunk
            current_chunk += paragraph + '\n'
        else:
            # Start a new chunk
            chunks.append(current_chunk.strip())
            current_chunk = paragraph + '\n'
    
    # Append any remaining content to the last chunk
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks



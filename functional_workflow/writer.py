def write_output(entry_data: str, output_file_name) -> None:
    with open(output_file_name, 'w') as output_file:
        output_file.write("*" * 80)
        output_file.write(entry_data)
        output_file.write("*" * 80)

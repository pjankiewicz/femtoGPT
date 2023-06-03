import os
import random

def concatenate_rs_files(root_dir, output_file_path, sample_rate):
    with open(output_file_path, 'w') as outfile:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            rs_files = [f for f in filenames if f.endswith('.rs')]
            sample_size = int(len(rs_files) * sample_rate)
            sampled_files = random.sample(rs_files, sample_size)

            for filename in sampled_files:
                filepath = os.path.join(dirpath, filename)
                with open(filepath, 'r') as infile:
                    outfile.write(infile.read())
                    outfile.write('\n')  # separate files by newline

cargo_home = os.path.join(os.path.expanduser('~'), '.cargo', 'registry', 'src')
concatenate_rs_files(cargo_home, 'dataset.txt', 0.1)


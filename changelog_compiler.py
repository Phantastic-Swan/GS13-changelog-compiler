import yaml
import argparse
import os

def valid_file(path):
    if not os.path.isfile(path):
        raise argparse.ArgumentTypeError(f"{path} is not a valid file")
    return path

def print_changelog(print_dates: bool = False, 
                    print_names: bool = False, 
                    input_path: str = "./", 
                    output_file_name: str = "Changelog.txt"):
    
    file = open(input_path, 'r')
    yaml_file = yaml.safe_load(file)
    file.close()
    output_file = open(output_file_name, 'w')

    changelog: dict = dict()

    for date in yaml_file:
        if print_dates:
            printed_date = date
        else:
            printed_date = "blank_date"
        
        if printed_date not in changelog:
            changelog[printed_date] = dict()

        for author in yaml_file[date]:
            if print_names:
                printed_name = author
            else:
                printed_name = "all_authors"
            
            if printed_name not in changelog[printed_date]:
                changelog[printed_date][printed_name] = list()

            for changes_dictionary in yaml_file[date][author]:
                changes = changes_dictionary.values()
                for item in changes:
                    changelog[printed_date][printed_name].append(item)
    
    for date in changelog:
        if print_dates:
            output_file.write(date.strftime("%x") + ":\n")
        for author in changelog[date]:
            if print_names:
                output_file.write("Changes by " + author + ":\n")
            for change in changelog[date][author]:
                output: str = "- " + change
                if not output.endswith("."):
                    output += "."
                output += "\n"
                output_file.write(output)

    output_file.close()

def main():
    parser = argparse.ArgumentParser(
        prog="changelog_compiler.py",
        description="This program is meant to compile GS13 changelogs \
        into easily copy-able format for news/update announcements"
    )
    parser.add_argument("input_file", type=valid_file,
                        help = "The path to the original .yml changelog file.")
    parser.add_argument("-d", "--print-dates", action="store_true", 
                        help="Optional. Whether the changes should be sorted by date. Defaults to false.")
    parser.add_argument("-n", "--print-names", action="store_true",
                        help="Optional. Whether the changes should be sorted by author. Defaults to false.")
    parser.add_argument("-o", "--output-file", default="Changelog.txt",
                        help="Optional. The name of the output file. Can be a path to a folder too. Defaults to the current directory.")

    args = parser.parse_args()

    # print("Input file:", full_input_path)
    # print("Sort by dates:", args.print_dates)
    # print("Sort by names:", args.print_names)
    # print("Output file:", args.output_file_name)

    input_path: str = args.input_file
    print_dates: bool = args.print_dates
    print_names: bool = args.print_names
    output_file_name: str = args.output_file

    if not input_path.endswith(".yaml") and not input_path.endswith(".yml"):
        print("File is not in YAML/YML format!")
        return    

    print_changelog(print_dates, print_names, input_path, output_file_name)


if __name__ == "__main__":
    main()
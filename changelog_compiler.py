import yaml
import datetime

yaml_file = 0

with open("2026-02.yml", 'r') as file:
    yaml_file = yaml.safe_load(file)

output_file = open("output_changelog.txt", 'w')

output_file.write("Changelog:\n")

for date in yaml_file:
    print(date)
    for author in yaml_file[date]:
        print(author)
        output_file.write("Changes by " + author + ":\n")
        for change_dict in yaml_file[date][author]:
            change = change_dict.values()
            for item in change:
                output_file.write("    " + item + "\n")

output_file.close()

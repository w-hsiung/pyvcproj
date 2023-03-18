# List all source and include files for each project in a solution.
#
# usage example:
#     python /custom/list_source.py solution.sln

import vcproj.solution
import vcproj.project
import os, sys


def main(argv):
    if len(argv) < 2:
        print("Usage: " + argv[0] + " <solution file>")
        sys.exit(2)

    solution_file = argv[1]
    solution = vcproj.solution.parse(solution_file)
    solution_dir = os.path.dirname(solution_file)
    for project_file in solution.project_files():
        project = vcproj.project.parse(os.path.join(solution_dir, project_file))
        print(project_file, "\t", project.configuration_type())


if __name__ == "__main__":
    main(sys.argv)

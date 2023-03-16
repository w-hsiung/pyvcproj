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
    print(solution_file)
    
    solution = vcproj.solution.parse(solution_file)
    for project_file in solution.project_files():
        print(project_file)
        project = vcproj.project.parse(os.path.join(os.path.dirname(solution_file), project_file))
        for source_file in project.source_files():
            print("\t" + source_file)
        for include_file in project.include_files():
            print("\t" + include_file)


if __name__ == "__main__":
    main(sys.argv)

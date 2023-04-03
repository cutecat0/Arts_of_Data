"""
    Reference: https://medium.com/geekculture/if-you-dont-know-what-python-libraries-to-learn-next-learn-these-d441c3729dd7
"""

from pathlib import Path

my_path = Path.cwd()
print(my_path)
# /Users/myname/github_projects/ArtsofData/data_science/basic_to_be_known/seems_u_know

print(my_path.parent)
# /Users/myname/github_projects/ArtsofData/data_science/basic_to_be_known

print(my_path.name)
# seems_u_know

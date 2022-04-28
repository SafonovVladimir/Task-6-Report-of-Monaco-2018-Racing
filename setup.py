from setuptools import setup

# [metadata]
setup(
    name='ReportOfMonaco2018Racing',
    version='1.0.2',
    author='Safonov Volodymyr',
    author_email='vladimir_safonov@ukr.net',
    description='Application print report that shows the top 15 racers and the rest after underline',
    # long_description='file: README.md',
    # long_description_content_type='text/markdown',
    url='https://git.foxminded.com.ua/Thrifty/task-6-report-of-monaco-2018-racing/',
    # project_urls=
    # 'Bug Tracker = https://git.foxminded.com.ua/Thrifty/task-6-report-of-monaco-2018-racing/-/issues',
    license='BSD 2-clause',
    packages=['D:\PythonProjects\Task 6 Report of Monaco 2018 Racing'],
    install_requires=['mpi4py>=2.0',
                      'numpy',
                      ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
#
# [options]
# package_dir =
#     = src
# packages = find:
# python_requires = >=3.6
#
# [options.packages.find]
# where = src

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sskagemo/using-opendata-from-brreg-no/main)

# A set of examples for how to use open data from BR with Python

*WARNING*: The examples are developed as part of enhancing my understanding of the content of the used registries,
as well as the functionality of the APIs, and there might be misunderstandings and examples of bad practices. Please refer to the official documentation of the relevant registries found at https://www.brreg.no/produkter-og-tjenester/apne-data/ 

Click on [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sskagemo/using-opendata-from-brreg-no/main) to have this repository opened for editing and execution using the service https://mybinder.org/ (does not require registration or account).

This repository contains three notebooks
- example using data from the search API
- example using data from full dump of data as JSON
- example using data from full dump of data as spreadsheet (xlsx)

Currently, for accessing a full dump of the National Coordination Registry for Legal Entities, you can choose between two formats, i.e. JSON, with the same structure as when using the search-API, or spreadsheet (*.xlsx). As the spreadsheet format is very slow to read with pandas, this repository also comes with a *.csv version of the dataset. This is not updated on a daily basis, but can be used to explore the dataset. The code for downloading and converting from xlsx to csv is available in these notebooks.

In addition to traditional Jupyter Notebooks, this repository also includes a *.py-file that supports the "interactive mode" in the editor VS Code. This gives a way of running individual cells of code, similar to the notebooks, but with a plain *.py file which has better support for versioning with git. This can be a good alternative for exploring the dataset, when the purpose is to create a script or part of an application, and not a Notebook.

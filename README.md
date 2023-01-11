# Overview
This is a small Python script that takes in one input file and creates an output file in SQL format. The SQL file should be executed on the phenotype.db database (from com.google.android.gms). The script was created to automate the process of this [this ticket](https://github.com/jacopotediosi/GoogleDialerMod/issues/51).

# Input file format
The input file should be formatted as follows:

Each line should contain a flag override in the format `<FlagOverrides.name>|<FlagOverrides.boolVal>`

Example:
```
bugle_phenotype__bug_192909536_supersort_classify_missing_messages_only_when_charging|0
bugle_phenotype__conversation_labels_enabled|1
```

# Output file format
The output file will be in SQL format and should be executed on the phenotype.db database. It will contain insert statement on table flagOverrides.

# Usage
```
python.exe ./generate_sql.py <input_file> <output_file>
```

This will take the input from <input_file>, convert it to SQL format, and save it to <output_file>.

# Note
It's important to make backup before executing script in your database because it will make modification on your database.

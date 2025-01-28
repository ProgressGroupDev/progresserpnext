## progresserpnext

ERPNext Customizations for Progress Software Development GmbH

## Installation

Create a new ERPNext site, if you don't have one yet:

```bash
bench new-site erp.example.org --install-app erpnext
```

Install this app:

```bash
bench --site erp.example.org install-app progresserpnext --branch version-15
```

## Features

- This app comes with a number of custom fields which are defined in the `progresserpnext/custom_fields.py` file.

## Contributing

### Update translations

Translations live in the `progresserpnext/locale` directory. The file `main.pot` holds all translatable strings. The `<locale>.po` files hold the actual translations.

To update the `main.pot` file, adding new translatable strings and removing old ones, run:

```bash
bench generate-pot-file --app progresserpnext
```

To sync the locale files with the `main.pot` file, run:

```bash
bench update-po-files --app progresserpnext
```

Add translations by editing the `msgstr` fields in the `<locale>.po` files.

#### License

gpl-3.0

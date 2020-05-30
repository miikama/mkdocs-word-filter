# mkdocs-word-filter

Strips extra content from markdown files that was added e.g. for converting the files to docx using pandoc

Stripped content can include for example:

- pagebreaks:

  <https://github.com/pandocker/pandoc-docx-pagebreak-py>

  ```markdown
  \newpage
  \toc
  ```

## Install

```bash
python -m pip install mkdocs-word-filter
```

## Usage

Active the plugin in `mkdocs.yml`. You can specify the ignorable strings as a list under the `filter-lines-with`

```yaml
plugins:
    - search 
    - mkdocs-word-filter:
        filter-lines-with:
            - \toc
            - \newpage
```

> **Note:** If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. MkDocs enables it by default if there is no `plugins` entry set, but now you have to enable it explicitly.

More information about plugins in the [MkDocs documentation][mkdocs-plugins].

## See Also

More information about templates [here][mkdocs-template].

More information about blocks [here][mkdocs-block].

[mkdocs-block]: https://www.mkdocs.org/user-guide/styling-your-docs/#overriding-template-blocks
[mkdocs-plugins]: http://www.mkdocs.org/user-guide/plugins/
[mkdocs-template]: https://www.mkdocs.org/user-guide/custom-themes/#template-variables

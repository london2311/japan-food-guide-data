# Contributing

Thank you for your interest in Japan Food Guide Data.

This project welcomes contributions that help make public restaurant information in Japan easier to structure, verify, and use responsibly for international travelers.

## Good first contributions

- Improve documentation
- Add sample HTML files from permitted sources
- Add parser tests
- Improve CSV/JSON schema validation
- Add responsible-use notes for a data source
- Add a collector for an official or tourism-association page that allows access

## Source rules

Please do not submit code or data that copies or redistributes:

- third-party review text
- user photos from review or map platforms
- proprietary scores or rankings
- content prohibited by target website terms
- private or non-public information

Prefer official restaurant websites, tourism associations, municipal pages, shopping-street pages, and other public sources that permit reuse.

## Development

```bash
pip install -r requirements.txt
python run_sample.py
pytest
```

## Pull request checklist

- [ ] The source is public and appropriate for collection
- [ ] Terms of service and robots.txt were considered
- [ ] Access frequency is respectful
- [ ] Tests were added or updated
- [ ] Documentation was updated if behavior changed
- [ ] No prohibited third-party content was copied into the repository
